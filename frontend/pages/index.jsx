"use client";
import { useState, useRef, useEffect, useCallback, useMemo } from "react";
import dynamic from "next/dynamic";
import Split from 'react-split';
import React from 'react';
import { Inter, JetBrains_Mono } from 'next/font/google';

// 1. Define the UI font
const inter = Inter({
    subsets: ['latin'],
    variable: '--font-ui'
});

// 2. Define the Code font
const jetbrainsMono = JetBrains_Mono({
    subsets: ['latin'],
    variable: '--font-code'
});

// --- STYLING CONSTANTS (Updated) ---
const BG_DEEP = '#181818';
const BG_PANEL = '#252526';
const BG_HEADER = '#1C1C1D'; // NEW: Slightly darker header for separation
const BORDER_COLOR = '#343A40';
const RED_MUTED_BG = '#3D2C2C';
const BG_ENV = '#303030';

// --- Utility Components ---

// 1. OutputLine: Renders a single line of streaming output (Memoized and styled)
const OutputLine = React.memo(({ line, isError }) => {
    const [isNew, setIsNew] = useState(true);

    useEffect(() => {
        const timer = setTimeout(() => {
            setIsNew(false);
        }, 200);
        return () => clearTimeout(timer);
    }, []);

    const textColor = isError ? 'text-red-400' : 'text-gray-200';

    // UPDATED: Use Tailwind classes for border/background
    const errorClasses = isError
        ? 'bg-red-900/30 border-l-4 border-red-500 p-2 my-1' // NEW: Added left border for strong emphasis
        : 'py-2 mb-1'; // UPDATED: Increased vertical spacing for readability

    // useMemo for performance optimization of complex formatting logic
    const formattedLine = useMemo(() => {
        if (isError) {
            return (
                <span className="flex items-start">
                    <span className="text-red-500 mr-2 font-bold">🚨</span>
                    <span>{line}</span>
                </span>
            );
        }

        return line.split(" ").map((word, index) => {
            if (word === "assert") {
                return <span key={index} className="text-red-400 font-bold">{word} </span>;
            } else if (word === "print") {
                return <span key={index} className="text-green-400 font-bold">{word} </span>;
            }
            return <span key={index}>{word} </span>;
        });
    }, [line, isError]);

    return (
        <div
            className={`
                font-mono text-lg block transition-all duration-200 whitespace-pre-wrap rounded-sm
                ${textColor}
                ${isNew ? 'output-line-flash' : ''} 
                ${errorClasses} 
            `}
        >
            {formattedLine}
        </div>
    );
});
OutputLine.displayName = 'OutputLine';

// 2. EnvironmentDisplay (with collapse/expand and type-based coloring)
const EnvironmentDisplay = ({ env }) => {
    const [isCollapsed, setIsCollapsed] = useState(false);

    const formatValue = (value) => {
        const type = typeof value;

        switch (type) {
            case 'number':
                return <span className="text-cyan-400 font-bold">{String(value)}</span>;
            case 'boolean':
                return <span className={value ? "text-green-500 font-bold" : "text-red-500 font-bold"}>{String(value)}</span>;
            case 'string':
                return <span className="text-yellow-400">{`"${value}"`}</span>;
            default:
                return <span className="text-gray-300">{String(value)}</span>;
        }
    };

    const keys = Object.keys(env);
    if (keys.length === 0) return null;

    return (
        <div
            className="mt-4 border border-blue-900/50 rounded-lg shadow-xl overflow-hidden"
            style={{ backgroundColor: BG_ENV }}
        >
            <h4
                className="px-3 py-2 text-sm font-semibold text-gray-100 bg-[#404040] border-b border-blue-900/50 flex justify-between items-center cursor-pointer hover:bg-[#505050] transition"
                onClick={() => setIsCollapsed(!isCollapsed)}
            >
                <span>Final Environment Variables ({keys.length})</span>
                <span>{isCollapsed ? '🔽' : '🔼'}</span>
            </h4>

            {!isCollapsed && (
                <div className="p-3 text-sm">
                    {keys.map(key => (
                        <div
                            key={key}
                            className="flex justify-between font-mono py-1 border-b border-gray-600/50 last:border-b-0"
                        >
                            <span className="text-blue-400 font-medium mr-4">{key}</span>
                            <span className="text-right">{formatValue(env[key])}</span>
                        </div>
                    ))}
                </div>
            )}
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
    const [editorFontSize, setEditorFontSize] = useState(24);

    const outputRef = useRef(null);
    const eventSourceRef = useRef(null);

    const clearOutput = useCallback(() => {
        setOutputEvents([]);
        setFinalEnv(null);
    }, []);

    const runCode = useCallback(() => {
        clearOutput();
        setRunning(true);

        const backendUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

        const evtSource = new EventSource(
            `${backendUrl}/stream?code=${encodeURIComponent(code)}`
        );
        eventSourceRef.current = evtSource;

        evtSource.onmessage = (e) => {
            const rawData = e.data.replace(/^data:\s*/, '');

            try {
                const event = JSON.parse(rawData);

                if (event.type === 'env_snapshot') {
                    setFinalEnv(event.content);
                    evtSource.close();
                    setRunning(false);
                    eventSourceRef.current = null;
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
            eventSourceRef.current = null;
        });


        evtSource.onerror = (e) => {
            if (evtSource.readyState === 2) {
                console.warn("SSE Stream closed or failed irreversibly. Assuming execution finished.");
                setRunning(false);
                evtSource.close();
                eventSourceRef.current = null;
            } else if (evtSource.readyState === 0) {
                console.warn("SSE Connection warning: Retrying or initial connection issue.");
            } else {
                console.error("Unresolved SSE Error:", e);
                setRunning(false);
                evtSource.close();
                eventSourceRef.current = null;
            }
        };

        return () => evtSource.close();
    }, [code, clearOutput]);

    const stopCode = useCallback(() => {
        if (eventSourceRef.current) {
            console.log("Stopping SSE stream manually.");
            eventSourceRef.current.close();
            eventSourceRef.current = null;
        }
        setRunning(false);
        setOutputEvents(prev => [...prev, { type: 'client_warning', content: 'Execution manually stopped.' }]);
    }, []);


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

    // Handles Ctrl + S shortcut
    useEffect(() => {
        const handleSaveShortcut = (event) => {
            const isCtrlOrCmd = event.ctrlKey || event.metaKey;
            const isSKey = event.key === 's' || event.key === 'S';

            if (isCtrlOrCmd && isSKey) {
                event.preventDefault();

                if (!running) {
                    runCode();
                } else {
                    stopCode();
                }
            }
        };

        document.addEventListener('keydown', handleSaveShortcut);

        return () => {
            document.removeEventListener('keydown', handleSaveShortcut);
        };
    }, [running, runCode, stopCode]);

    return (
        <>
            <style jsx global>{`
                .output-line-flash {
                    background-color: rgba(59, 130, 246, 0.3) !important;
                    border-left: 3px solid #60A5FA;
                    padding-left: 5px; 
                    transition: background-color 0.2s ease-out, border-left-color 0.2s ease-out;
                }
                
                .split-pane-wrapper { display: flex; height: 100%; }
                .gutter {
                    background-color: ${BG_DEEP}; 
                    cursor: col-resize;
                    transition: background-color 0.2s;
                    border-left: 1px solid ${BORDER_COLOR};
                    border-right: 1px solid ${BORDER_COLOR}; 
                }
                .gutter:hover { background-color: ${BORDER_COLOR}; }
                .gutter.gutter-horizontal { width: 10px; }
            `}</style>


            <div
                className={`flex flex-col h-screen text-gray-100 font-ui ${inter.variable} ${jetbrainsMono.variable}`}
                style={{ backgroundColor: BG_DEEP }}
            >
                {/* Header (UPDATED Background) */}
                <header
                    className={`flex items-center px-6 py-4 border-b shadow-md justify-between`}
                    style={{ backgroundColor: BG_HEADER, borderColor: BORDER_COLOR }}
                >
                    <h1 className="text-2xl font-bold text-white">Expr Playground</h1>
                    <div className="text-sm font-mono flex items-center">
                        <span className="text-gray-400 mr-2">Status:</span>
                        <span className={`h-3 w-3 rounded-full mr-2 ${running ? 'bg-yellow-500 animate-pulse' : 'bg-green-500'}`}></span>
                        <span className={running ? 'text-yellow-500' : 'text-green-500'}>
                            {running ? 'RUNNING' : 'IDLE'}
                        </span>
                    </div>
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
                            {/* Editor Header with Run/Stop Button */}
                            <div
                                className={`px-4 py-2 border-b text-gray-300 font-semibold flex justify-between items-center`}
                                style={{ borderColor: BORDER_COLOR }}
                            >
                                <span>Editor</span>

                                {/* === START: New Slider Input === */}
                                <div className="ml-6 flex items-center text-sm font-normal text-gray-400">
                                    <label htmlFor="font-slider" className="mr-2 hidden sm:inline">
                                        Font Size:
                                    </label>
                                    <input
                                        id="font-slider"
                                        type="range"
                                        min="10"
                                        max="24"
                                        value={editorFontSize}
                                        onChange={(e) => setEditorFontSize(parseInt(e.target.value))}
                                        className="w-24 h-2 bg-gray-700 rounded-lg appearance-none cursor-pointer range-lg"
                                    />
                                    <span className="ml-2 w-5 text-right font-mono text-gray-300">{editorFontSize}</span>
                                </div>
                                {/* === END: New Slider Input === */}

                                {/* RUN/STOP BUTTON (UPDATED Shortcut Styling) */}
                                {running ? (
                                    <button
                                        onClick={stopCode}
                                        className={`px-4 py-1 text-sm rounded-md font-medium transition duration-150 ease-in-out shadow-md bg-red-600 hover:bg-red-500 text-white`}
                                    >
                                        <span className="flex items-center">
                                            <svg className="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path fill="currentColor" d="M14 19H10V5H14V19Z"></path></svg>
                                            Stop <span className="ml-1 text-xs opacity-75">(Ctrl+S)</span>
                                        </span>
                                    </button>
                                ) : (
                                    <button
                                        onClick={runCode}
                                        className={`px-4 py-1 text-sm rounded-md font-medium transition duration-150 ease-in-out shadow-md bg-blue-600 hover:bg-blue-500 text-white`}
                                    >
                                        Run <span className="ml-1 text-xs opacity-75">(Ctrl+S)</span>
                                    </button>
                                )}

                            </div>
                            <div className="flex-1">
                                <ExprEditor code={code} onChange={setCode} fontSize={editorFontSize} />
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
                                <span className="flex items-center">
                                    Console Output
                                    {running && (
                                        <span className="text-sm text-yellow-400 flex items-center ml-4">
                                            <span className="h-2 w-2 rounded-full bg-yellow-400 mr-2 animate-pulse"></span>
                                            Streaming...
                                        </span>
                                    )}
                                </span>

                                {/* Clear Console Button */}
                                <button
                                    onClick={clearOutput}
                                    className={`px-3 py-0.5 text-xs rounded font-medium text-gray-300 hover:bg-[#505050] transition`}
                                    title="Clear Console Output"
                                >
                                    Clear 🗑️
                                </button>
                            </div>
                            <div
                                ref={outputRef}
                                className={`flex-1 p-4 overflow-y-auto`}
                                style={{ backgroundColor: BG_DEEP }}
                            >
                                {/* Rendering based on structured events */}
                                {outputEvents.length > 0 || finalEnv ? (
                                    <>
                                        {outputEvents.map((event, index) => (
                                            <OutputLine
                                                key={index}
                                                line={event.content}
                                                isError={event.type.includes('error') || event.type.includes('client_error')}
                                            />
                                        ))}
                                        {/* Dedicated Display for Final Environment */}
                                        {finalEnv && <EnvironmentDisplay env={finalEnv} />}
                                    </>
                                ) : (
                                    <span className="text-gray-500 font-mono text-sm flex items-center">
                                        {running ? "Connecting to stream..." : "📝 Press 'Run' or Ctrl+S to execute. Results will stream here."}
                                    </span>
                                )}


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