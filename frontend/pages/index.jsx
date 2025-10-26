"use client";
import { useState, useRef, useEffect, useCallback } from "react"; // 👈 ADD useCallback
import dynamic from "next/dynamic";
import Split from 'react-split';

import { Inter, JetBrains_Mono } from 'next/font/google';

export const metadata = {
    title: 'Expr Playground',
};

// 1. Define the UI font (Inter is a great default for the system stack)
const inter = Inter({
    subsets: ['latin'],
    variable: '--font-ui'
});

// 2. Define the Code font (JetBrains Mono)
const jetbrainsMono = JetBrains_Mono({
    subsets: ['latin'],
    variable: '--font-code'
});

// --- STYLING CONSTANTS (Used for Inline Styles and Global CSS) ---
const BG_DEEP = '#181818';
const BG_PANEL = '#252526';
const BORDER_COLOR = '#343A40';
const RED_MUTED_BG = '#3D2C2C';
const BG_ENV = '#303030';

// --- Utility Components (OutputLine remains as previously fixed) ---

// 1. OutputLine: Renders a single line of streaming output (print or error)
const OutputLine = ({ line, isError }) => {
    const [isNew, setIsNew] = useState(true);

    useEffect(() => {
        const timer = setTimeout(() => {
            setIsNew(false);
        }, 200);
        return () => clearTimeout(timer);
    }, []);

    const textColor = isError ? 'text-red-400' : 'text-gray-200';
    const style = isError ? { backgroundColor: RED_MUTED_BG, padding: '8px' } : {};

    const formattedLine = isError
        ? line
        : line.split(" ").map((word, index) => {
            if (word === "assert") {
                return <span key={index} className="text-red-400 font-bold">{word} </span>;
            } else if (word === "print") {
                return <span key={index} className="text-green-400 font-bold">{word} </span>;
            }
            return <span key={index}>{word} </span>;
        });

    return (
        <div
            className={`
                font-mono text-sm block transition-all duration-200 whitespace-pre-wrap rounded-sm
                ${textColor}
                ${isNew ? 'output-line-flash' : ''} 
                ${isError ? 'p-2 my-1' : 'py-0.5'}
            `}
            style={style}
        >
            {formattedLine}
        </div>
    );
};

// 2. EnvironmentDisplay (remains the same)
const EnvironmentDisplay = ({ env }) => {
    // ... (rest of EnvironmentDisplay logic) ...
    const formatValue = (value) => {
        if (typeof value === 'number') {
            return String(value);
        }
        return String(value);
    };

    const keys = Object.keys(env);
    if (keys.length === 0) return null;

    return (
        <div
            className="mt-4 border border-blue-900/50 rounded-lg shadow-xl overflow-hidden"
            style={{ backgroundColor: BG_ENV }}
        >
            <h4 className="px-3 py-2 text-sm font-semibold text-gray-100 bg-[#404040] border-b border-blue-900/50">
                Final Environment Variables
            </h4>
            <div className="p-3 text-sm">
                {keys.map(key => (
                    <div
                        key={key}
                        className="flex justify-between font-mono py-1 border-b border-gray-600/50 last:border-b-0"
                    >
                        <span className="text-blue-400 font-medium mr-4">{key}</span>
                        <span className="text-yellow-300 text-right">{formatValue(env[key])}</span>
                    </div>
                ))}
            </div>
        </div>
    );
};


// --- Main Component ---

const ExprEditor = dynamic(() => import("../components/ExprEditor"), { ssr: false });

export default function HomePage() {
    const [code, setCode] = useState(`# Example Expr code
x = 1.23e4
y = 3x10^2
print x + y
assert x > 0
`);
    const [outputEvents, setOutputEvents] = useState([]);
    const [finalEnv, setFinalEnv] = useState(null);
    const [running, setRunning] = useState(false);
    const [flashOutput, setFlashOutput] = useState(false);

    const outputRef = useRef(null);

    // 👇 1. WRAP runCode in useCallback to stabilize the function
    const runCode = useCallback(() => {
        // These three lines already clear the output and reset state!
        setOutputEvents([]);
        setFinalEnv(null);
        setRunning(true);

        // use the environment variable for backend URL: NEXT_PUBLIC_API_URL
        const backendUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

        const evtSource = new EventSource(
            `${backendUrl}/stream?code=${encodeURIComponent(code)}`
        );

        // --- EventSource handlers (onmessage, addEventListener, onerror) remain the same ---
        evtSource.onmessage = (e) => {
            const rawData = e.data.replace(/^data:\s*/, '');

            try {
                const event = JSON.parse(rawData);

                if (event.type === 'env_snapshot') {
                    setFinalEnv(event.content);
                    evtSource.close();
                    setRunning(false);
                } else if (event.type === 'stream_start') {
                    setOutputEvents((prev) => [...prev, event]);
                } else {
                    setOutputEvents((prev) => [...prev, event]);
                }

            } catch (error) {
                console.error("Failed to parse event data:", rawData, error);
                setOutputEvents((prev) => [...prev, { type: 'client_error', content: `[Client Error] Failed to read stream data on final event.` }]);
            }
        };

        evtSource.addEventListener('close', () => {
            console.log("SSE Stream received 'close' event. Terminating connection.");
            evtSource.close();
            setRunning(false);
        });


        evtSource.onerror = (e) => {
            if (evtSource.readyState === 2) {
                console.warn("SSE Stream closed or failed irreversibly.");
                setRunning(false);
            } else if (evtSource.readyState === 0) {
                console.warn("SSE Connection warning: Retrying or initial connection issue.");
            } else {
                console.error("Unresolved SSE Error:", e);
            }
        };
    }, [code]); // 👈 Dependency on 'code' because it's used in the query string


    useEffect(() => {
        if (outputRef.current) {
            outputRef.current.scrollTop = outputRef.current.scrollHeight;
        }

        if (outputEvents.length > 0) {
            setFlashOutput(true);

            const timer = setTimeout(() => {
                setFlashOutput(false);
            }, 200);

            return () => clearTimeout(timer);
        }
    }, [outputEvents]);

    // 👇 2. UPDATED EFFECT: Handles Ctrl + S shortcut with stable dependencies
    useEffect(() => {
        const handleSaveShortcut = (event) => {
            const isCtrlOrCmd = event.ctrlKey || event.metaKey;
            const isSKey = event.key === 's' || event.key === 'S';

            if (isCtrlOrCmd && isSKey) {
                // Prevent the default browser save dialog
                event.preventDefault();

                // Call the runCode function, which is now stable and clears the output
                if (!running) {
                    runCode();
                }
            }
        };

        document.addEventListener('keydown', handleSaveShortcut);

        return () => {
            document.removeEventListener('keydown', handleSaveShortcut);
        };
    }, [running, runCode]); // 👈 Dependencies include 'running' and 'runCode'

    return (
        <>
            {/* Global Styles for Fonts, Splitter, and Background */}
            <style jsx global>{`
                /* ... (existing styles) ... */
                /* NEW: Individual Line Flash Effect */
                .output-line-flash {
                    background-color: rgba(59, 130, 246, 0.3) !important;
                    border-left: 3px solid #60A5FA;
                    padding-left: 5px; 
                    transition: background-color 0.2s ease-out, border-left-color 0.2s ease-out;
                }
                
                .split-pane-wrapper {
                    display: flex;
                    height: 100%;
                }
                .gutter {
                    background-color: ${BG_DEEP}; 
                    cursor: col-resize;
                    transition: background-color 0.2s;
                    border-left: 1px solid ${BORDER_COLOR};
                    border-right: 1px solid ${BORDER_COLOR}; 
                }
                .gutter:hover {
                    background-color: ${BORDER_COLOR};
                }
                .gutter.gutter-horizontal {
                    width: 10px;
                }
            `}</style>


            <div
                className={`flex flex-col h-screen text-gray-100 font-ui ${inter.variable} ${jetbrainsMono.variable}`}
                style={{ backgroundColor: BG_DEEP }}
            >
                {/* Header */}
                <header
                    className={`flex items-center px-6 py-4 border-b shadow-md`}
                    style={{ backgroundColor: BG_PANEL, borderColor: BORDER_COLOR }}
                >
                    <h1 className="text-2xl font-bold text-white">Expr Playground</h1>
                </header>

                {/* Main Content using Split */}
                <div className="flex-1 p-4 overflow-hidden">
                    <Split
                        className="split-pane-wrapper gap-4"
                        sizes={[50, 50]}
                        minSize={300}
                        gutterSize={10}
                        direction="horizontal"
                    >
                        {/* 1. Editor Panel */}
                        <div
                            className={`flex flex-col rounded-lg shadow-xl border overflow-hidden`}
                            style={{ backgroundColor: BG_PANEL, borderColor: BORDER_COLOR }}
                        >
                            {/* Editor Header with Run Button */}
                            <div
                                className={`px-4 py-2 border-b text-gray-300 font-semibold flex justify-between items-center`}
                                style={{ borderColor: BORDER_COLOR }}
                            >
                                <span>Editor</span>

                                {/* RUN BUTTON */}
                                <button
                                    onClick={runCode}
                                    disabled={running}
                                    className={`px-4 py-1 text-sm rounded-md font-medium transition duration-150 ease-in-out shadow-md
                                    ${running ? "bg-gray-600 cursor-not-allowed text-gray-400" : "bg-blue-600 hover:bg-blue-500 text-white"}`}
                                >
                                    {running ? (
                                        <span className="flex items-center">
                                            <svg className="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                                                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                                                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                                            </svg>
                                            Running...
                                        </span>
                                    ) : (
                                        "Run"
                                    )}
                                </button>

                            </div>
                            <div className="flex-1">
                                <ExprEditor code={code} onChange={setCode} />
                            </div>
                        </div>

                        {/* 2. Output Panel */}
                        <div
                            className={`flex flex-col rounded-lg shadow-xl border overflow-hidden transition-all duration-200 ${flashOutput ? 'output-flash' : ''}`}
                            style={{ backgroundColor: BG_PANEL, borderColor: BORDER_COLOR }}
                        >
                            <div
                                className={`px-4 py-2 border-b text-gray-300 font-semibold flex justify-between items-center`}
                                style={{ borderColor: BORDER_COLOR }}
                            >
                                <span>Console Output</span>
                                {running && (
                                    <span className="text-sm text-yellow-400 flex items-center">
                                        <span className="h-2 w-2 rounded-full bg-yellow-400 mr-2 animate-pulse"></span>
                                        Streaming...
                                    </span>
                                )}
                            </div>
                            <div
                                ref={outputRef}
                                className={`flex-1 p-4 overflow-y-auto`}
                                style={{ backgroundColor: BG_DEEP }}
                            >
                                {/* Rendering based on structured events */}
                                {outputEvents.length > 0 ? (
                                    outputEvents.map((event, index) => (
                                        <OutputLine
                                            key={index}
                                            line={event.content}
                                            isError={event.type.includes('error')}
                                        />
                                    ))
                                ) : (
                                    <span className="text-gray-500 font-mono text-sm">
                                        {running ? "Connecting to stream..." : "Press 'Run' or Ctrl+S to see output..."}
                                    </span>
                                )}

                                {/* Dedicated Display for Final Environment */}
                                {finalEnv && <EnvironmentDisplay env={finalEnv} />}
                            </div>
                        </div>
                    </Split>
                </div>

                {/* Status Bar */}
                <footer
                    className={`p-1 text-xs text-gray-500 border-t text-center`}
                    style={{ backgroundColor: BG_DEEP, borderColor: BORDER_COLOR }}
                >
                    Expr Playground | Interpreter v1.0
                </footer>
            </div>
        </>
    );
}