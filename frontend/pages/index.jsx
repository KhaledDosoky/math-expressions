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

// --- STYLING CONSTANTS (Muted Indigo Theme) ---
const BG_DEEP = '#121212';
const BG_HEADER = '#181818';
const BG_PANEL = '#252526';
const BORDER_COLOR = '#343A40';
const PRIMARY_ACCENT = '#9370DB';
const OUTPUT_FLASH_COLOR = '#7B68EE';


// --- Utility Components ---

const OutputLine = React.memo(({ line, isError }) => {
    const [isNew, setIsNew] = useState(true);

    useEffect(() => {
        const timer = setTimeout(() => {
            setIsNew(false);
        }, 200);
        return () => clearTimeout(timer);
    }, []);

    const textColor = isError ? 'text-red-400' : 'text-gray-200';

    const errorClasses = isError
        ? 'bg-red-900/30 p-2 my-1 border-l-4 border-red-500'
        : 'py-2 mb-1';

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
            // Using React.Fragment for the implicit space to avoid extra span
            if (word === "assert") {
                return <React.Fragment key={index}><span className="text-yellow-400 font-bold">{word}</span>{' '}</React.Fragment>;
            } else if (word === "print") {
                return <React.Fragment key={index}><span className="text-green-400 font-bold">{word}</span>{' '}</React.Fragment>;
            }
            return <React.Fragment key={index}>{word}{' '}</React.Fragment>;
        });
    }, [line, isError]);

    return (
        <div
            className={`
                font-code text-lg block transition-all duration-200 whitespace-pre-wrap rounded-sm
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

// New Memoized component for the list of output events
const OutputList = React.memo(({ events }) => {
    return (
        <>
            {events.map((event, index) => (
                // index key is used here as events are only appended, never reordered or removed mid-list
                <OutputLine
                    key={index}
                    line={event.content}
                    isError={event.type.includes('error') || event.type.includes('client_error') || event.type.includes('warning')}
                />
            ))}
        </>
    );
});
OutputList.displayName = 'OutputList';


const VariableEntryComponent = ({ name, value, isRoot = false, depth = 0 }) => {
    const type = typeof value;
    const isExpandable = type === 'object' && value !== null && !Array.isArray(value) && Object.keys(value).length > 0;
    const isArray = Array.isArray(value);
    const [isExpanded, setIsExpanded] = useState(isRoot && !isArray);

    const formatValue = useCallback((val, currentType, isArr) => {
        if (isArr) return <span className="text-gray-400">[{val.length} items]</span>;
        if (val === null) return <span className="text-gray-500 font-bold">null</span>;

        switch (currentType) {
            case 'number':
                return <span className="text-cyan-400 font-bold">{String(val)}</span>;
            case 'boolean':
                return <span className={val ? "text-green-500 font-bold" : "text-red-500 font-bold"}>{String(val)}</span>;
            case 'string':
                const displayVal = val.length > 50 ? `"${val.substring(0, 47)}..."` : `"${val}"`;
                return <span className="text-yellow-400">{displayVal}</span>;
            case 'object':
                if (isArray) return null; // Handled by isArray check
                const keys = Object.keys(val).length;
                return <span className="text-gray-400">&#123;{keys} key{keys !== 1 ? 's' : ''}&#125;</span>;
            default:
                return <span className="text-gray-300">{String(val)}</span>;
        }
    }, [isArray]);

    const toggleExpand = useCallback((e) => {
        e.stopPropagation();
        if (isExpandable || isArray) {
            setIsExpanded(prev => !prev);
        }
    }, [isExpandable, isArray]);

    const indentStyle = useMemo(() => ({
        paddingLeft: `${depth * 16}px`,
    }), [depth]);

    const PRIMARY_ACCENT_TEXT = PRIMARY_ACCENT;

    // Memoize the children only if expanded
    const childrenContent = useMemo(() => {
        if (!isExpanded) return null;

        const entries = isArray
            ? value.map((item, index) => ({ key: index, name: `[${index}]`, value: item, type: typeof item }))
            : Object.entries(value).map(([key, subValue]) => ({ key, name: key, value: subValue, type: typeof subValue }));

        return (
            <div className="bg-gray-800/20">
                {entries.map((entry) => {
                    // Non-expandable array items can be rendered directly for simplicity
                    if (isArray && typeof entry.value !== 'object' || entry.value === null) {
                        return (
                            <div key={entry.key} className="flex py-1.5" style={{ paddingLeft: `${(depth + 1) * 16}px` }}>
                                <span className="text-gray-500 mr-2">{entry.name}:</span>
                                {formatValue(entry.value, entry.type, false)}
                            </div>
                        );
                    }
                    // Recursive call for objects or expandable array items
                    return (
                        <VariableEntry
                            key={entry.key}
                            name={entry.name}
                            value={entry.value}
                            depth={depth + 1}
                        />
                    );
                })}
            </div>
        );
    }, [isExpanded, value, isArray, depth, formatValue]);


    return (
        <div className="font-code text-sm">
            <div
                className={`flex items-center py-1.5 border-b border-gray-700/50 last:border-b-0 transition hover:bg-gray-700/30 ${isExpandable || isArray ? 'cursor-pointer' : 'cursor-default'}`}
                onClick={toggleExpand}
                style={indentStyle}
            >
                {(isExpandable || isArray) ? (
                    <span className="mr-1 text-gray-500 transform transition duration-150 w-3">
                        {isExpanded ? '▼' : '▶'}
                    </span>
                ) : (
                    <span className="mr-1 invisible w-3">{" "}</span>
                )}

                <span className="font-medium mr-2" style={{ color: PRIMARY_ACCENT_TEXT }}>{name}:</span>

                {formatValue(value, type, isArray)}
            </div>

            {childrenContent}
        </div>
    );
};

// Memoization relies on name, value, isRoot, and depth.
const VariableEntry = React.memo(VariableEntryComponent);
VariableEntry.displayName = 'VariableEntry';


const EnvironmentDisplayComponent = ({ env }) => {
    const keys = Object.keys(env);
    if (keys.length === 0) return (
        <span className="text-gray-600 font-code text-sm p-2 block">No variables defined. Run the code to populate.</span>
    );

    return (
        <div className="p-2 h-full overflow-y-auto">
            {Object.entries(env).map(([key, value]) => (
                <VariableEntry
                    key={key}
                    name={key}
                    value={value}
                    isRoot={true}
                    depth={0}
                />
            ))}
        </div>
    );
};

const EnvironmentDisplay = React.memo(EnvironmentDisplayComponent, (prevProps, nextProps) => {
    // Only re-render if the 'finalEnv' object reference changes
    return prevProps.env === nextProps.env;
});
EnvironmentDisplay.displayName = 'EnvironmentDisplay';


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
    const [editorFontSize, setEditorFontSize] = useState(18);

    const outputRef = useRef(null);
    const eventSourceRef = useRef(null);

    const triggerFlash = useCallback(() => {
        setFlashOutput(true);
        setTimeout(() => setFlashOutput(false), 200);
    }, []);

    const clearOutput = useCallback(() => {
        setOutputEvents([]);
        setFinalEnv(null);
    }, []);

    const runCode = useCallback(() => {
        clearOutput();
        setRunning(true);

        const evtSource = new EventSource(
            `/api/stream?code=${encodeURIComponent(code)}`
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
                    setOutputEvents((prev) => {
                        const newEvents = [...prev, event];
                        triggerFlash();
                        return newEvents;
                    });
                }

            } catch (error) {
                console.error("Failed to parse event data:", rawData, error);
                setOutputEvents((prev) => {
                    const newEvents = [...prev, { type: 'client_error', content: `[Client Error] Failed to read stream data on final event.` }];
                    triggerFlash();
                    return newEvents;
                });
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
        setOutputEvents(prev => {
            const newEvents = [...prev, { type: 'client_warning', content: 'Execution manually stopped.' }];
            triggerFlash();
            return newEvents;
        });
    }, []);


    useEffect(() => {
        if (outputRef.current) {
            outputRef.current.scrollTop = outputRef.current.scrollHeight;
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
                    background-color: ${OUTPUT_FLASH_COLOR}33 !important; 
                    border-left: 3px solid ${OUTPUT_FLASH_COLOR};
                    padding-left: 5px; 
                    transition: background-color 0.2s ease-out, border-left-color 0.2s ease-out;
                }
                
                .split-pane-wrapper { display: flex; height: 100%; }
                
                /* Update the base .gutter styles */
                .gutter {
                    background-color: ${BG_DEEP}; 
                    transition: background-color 0.2s, border-color 0.2s; 
                }

                /* Horizontal Gutter (Main Split) - Desktop */
                .gutter.gutter-horizontal { 
                    width: 10px;
                    cursor: col-resize !important; 
                    border-left: 1px solid transparent; 
                    border-right: 1px solid transparent; 
                }
                .gutter.gutter-horizontal:hover { 
                    cursor: col-resize !important;
                    background-color: ${PRIMARY_ACCENT}33; 
                    border-left: 1px solid ${PRIMARY_ACCENT};
                    border-right: 1px solid ${PRIMARY_ACCENT};
                }

                /* Vertical Gutter (Nested Split) */
                .gutter.gutter-vertical { 
                    height: 10px;
                    cursor: row-resize; 
                    border-top: 1px solid transparent; 
                    border-bottom: 1px solid transparent;
                }
                .gutter.gutter-vertical:hover {
                    background-color: ${PRIMARY_ACCENT}33;
                    cursor: row-resize; 
                    border-top: 1px solid ${PRIMARY_ACCENT};
                    border-bottom: 1px solid ${PRIMARY_ACCENT}; 
                }

                /* ======================================= */
                /* MOBILE RESPONSIVENESS STYLES      */
                /* ======================================= */
                @media (max-width: 768px) {
                    
                    /* 1. Collapse the main horizontal split to a vertical stack */
                    .split-pane-wrapper {
                        flex-direction: column !important; /* Forces stacking */
                        gap: 16px; /* Add some space between the two main panels */
                    }

                    /* 2. Hide all gutters and remove resizing functionality */
                    .gutter {
                        display: none !important; 
                        width: 0 !important;
                        height: 0 !important;
                        min-height: 0 !important;
                        min-width: 0 !important;
                        cursor: default !important;
                    }
                    
                    /* 3. Ensure panels use full width and height is managed by content/flex-grow */
                    .split-pane-wrapper > div {
                        width: 100% !important; 
                        min-width: 100%;
                    }

                    /* Make the Editor panel take up a good portion of the screen */
                    .split-pane-wrapper > div:first-child {
                        height: 50vh !important; /* Set a specific height for the Editor (50% of viewport height) */
                        min-height: 300px;
                    }
                    
                    /* Make the Console/Variables panel take the rest of the height */
                    .split-pane-wrapper > div:last-child {
                        height: auto !important;
                        flex-grow: 1;
                        overflow: hidden; /* Prevent inner splits from causing external scroll */
                    }
                }
            `}</style>


            <div
                className={`flex flex-col h-screen text-gray-100 font-ui ${inter.variable} ${jetbrainsMono.variable}`}
                style={{ backgroundColor: BG_DEEP }}
            >

                {/* === Header (Dynamic Bracket Logo) === */}
                <header
                    className={`flex items-center px-6 py-4 border-b shadow-2xl justify-between`}
                    style={{ backgroundColor: BG_HEADER, borderColor: BORDER_COLOR }}
                >
                    <div className="flex items-center">
                        {/* Logo: Stylized Dynamic Bracket {ω} */}
                        <div className="flex items-center mr-3" style={{ textShadow: `0 0 5px ${PRIMARY_ACCENT}80` }}>
                            <svg width="36" height="36" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <rect width="48" height="48" fill="transparent" />
                                <path d="M14 8L6 24L14 40" stroke={PRIMARY_ACCENT} strokeWidth="4" strokeLinecap="round" strokeLinejoin="round" />
                                <path d="M34 8L42 24L34 40" stroke={PRIMARY_ACCENT} strokeWidth="4" strokeLinecap="round" strokeLinejoin="round" />
                                <path d="M19 16L29 24L19 32V16Z" fill={PRIMARY_ACCENT} />
                            </svg>
                        </div>
                        <h1 className="text-3xl font-extrabold tracking-tight text-white font-ui drop-shadow-lg text-xl sm:text-3xl"> {/* Reduced size on mobile */}
                            Expr<span style={{ color: PRIMARY_ACCENT }}>CLI</span> Playground
                        </h1>
                    </div>

                    <div className="text-sm font-code flex items-center">
                        <span className="text-gray-400 mr-2 hidden sm:inline">Status:</span>
                        <span className={`h-3 w-3 rounded-full mr-2 ${running ? 'bg-yellow-500 animate-pulse' : 'bg-green-500'}`}></span>
                        <span className={running ? 'text-yellow-500' : 'text-green-500'}>
                            {running ? 'RUNNING' : 'IDLE'}
                        </span>
                    </div>
                </header>
                {/* === END Header === */}

                {/* Main Content using Split (Horizontal) */}
                <div className="flex-1 p-4 overflow-hidden">
                    <Split
                        className="split-pane-wrapper gap-4"
                        initialSizes={[50, 50]}
                        minSize={100}
                        gutterSize={10}
                        direction="horizontal" // Default direction (desktop)
                    >
                        {/* 1. Editor Panel (Left/Top) */}
                        <div
                            className={`flex flex-col rounded-lg shadow-xl border overflow-hidden`}
                            style={{ backgroundColor: BG_PANEL, borderColor: BORDER_COLOR }}
                        >
                            {/* Editor Header with Run/Stop Button */}
                            <div
                                // Use 'flex justify-between' and apply gap for mobile
                                className={`px-4 py-2 border-b text-gray-300 font-semibold flex justify-between items-center gap-2 sm:gap-6`}
                                style={{ borderColor: BORDER_COLOR }}
                            >
                                {/* LEFT: Editor Title - Now a standalone flex item */}
                                <span>Editor</span>

                                {/* MIDDLE: Font Slider - Centered by flex properties of the container */}
                                <div className="flex items-center text-xs sm:text-sm font-normal text-gray-400">
                                    <label htmlFor="font-slider" className="mr-1 inline-flex">
                                        Font Size:
                                    </label>
                                    <input
                                        id="font-slider"
                                        type="range"
                                        min="10"
                                        max="30"
                                        value={editorFontSize}
                                        onChange={(e) => setEditorFontSize(parseInt(e.target.value))}
                                        className="w-16 sm:w-24 h-2 rounded-lg appearance-none cursor-pointer range-lg bg-gray-700 [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:w-3 [&::-webkit-slider-thumb]:h-3 [&::-webkit-slider-thumb]:rounded-full [&::-webkit-slider-thumb]:bg-indigo-400"
                                    />
                                    <span className="ml-1 w-5 text-right font-code text-gray-300">{editorFontSize}</span>
                                </div>
                                {/* END MIDDLE */}

                                {/* RIGHT: RUN/STOP BUTTON - Now a standalone flex item */}
                                {running ? (
                                    <button
                                        onClick={stopCode}
                                        className={`px-4 py-1 text-sm rounded-md font-medium transition duration-150 ease-in-out shadow-lg bg-red-600 hover:bg-red-500 text-white`}
                                    >
                                        <span className="flex items-center">
                                            <svg className="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path fill="currentColor" d="M14 19H10V5H14V19Z"></path></svg>
                                            Stop <span className="ml-1 text-xs opacity-75 hidden sm:inline">(Ctrl+S)</span>
                                        </span>
                                    </button>
                                ) : (
                                    <button
                                        onClick={runCode}
                                        className={`px-4 py-1 text-sm rounded-md font-medium transition duration-150 ease-in-out shadow-lg text-white hover:opacity-90`}
                                        style={{ backgroundColor: PRIMARY_ACCENT, boxShadow: `0 0 10px ${PRIMARY_ACCENT}60` }}
                                    >
                                        Run <span className="ml-1 text-xs opacity-75 hidden sm:inline">(Ctrl+S)</span>
                                    </button>
                                )}
                            </div>
                            <div className="flex-1">
                                <ExprEditor code={code} onChange={setCode} fontSize={editorFontSize} />
                            </div>
                        </div>

                        {/* 2. Right Side Split (Vertical Split for Console and Environment) */}
                        <Split
                            direction="vertical" // Nested vertical split 
                            sizes={[60, 40]}
                            minSize={100}
                            gutterSize={10}
                            className="flex flex-col h-full"
                        >
                            {/* 2a. Console Output Panel (Top Right) */}
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
                                    {/* Console Output Events - Using the new memoized OutputList */}
                                    {outputEvents.length > 0 ? (
                                        <OutputList events={outputEvents} />
                                    ) : (
                                        <span className="text-gray-500 font-code text-sm flex items-center">
                                            {running ? "Connecting to stream..." : "📝 Press 'Run' or Ctrl+S to execute. Results will stream here."}
                                        </span>
                                    )}
                                </div>
                            </div>

                            {/* 2b. Environment Variables Panel (Bottom Right) */}
                            <div
                                className={`flex flex-col rounded-lg shadow-xl border overflow-hidden`}
                                style={{ backgroundColor: BG_PANEL, borderColor: BORDER_COLOR }}
                            >
                                <div
                                    className={`px-4 py-2 border-b text-gray-300 font-semibold`}
                                    style={{ borderColor: BORDER_COLOR }}
                                >
                                    Runtime Variables
                                </div>
                                <div className="flex-1 h-full overflow-y-auto" style={{ backgroundColor: BG_DEEP }}>
                                    {/* EnvironmentDisplay is memoized */}
                                    <EnvironmentDisplay env={finalEnv || {}} />
                                </div>
                            </div>

                        </Split>
                    </Split>
                </div>

                {/* Status Bar */}
                <footer
                    className={`p-1 text-xs text-gray-500 border-t flex justify-center space-x-2 sm:space-x-4 font-code`}
                    style={{ backgroundColor: BG_DEEP, borderColor: BORDER_COLOR }}
                >
                    <span className="text-gray-400 hidden sm:inline">Expr Playground | Interpreter v1.0</span>
                    <span className="text-gray-400 sm:hidden">Expr v1.0</span>
                    <span className="text-gray-500 hidden sm:inline">|</span>
                    <span>
                        <a href="https://khaled.boo/" target="_blank" rel="noopener noreferrer" className="text-indigo-400 hover:text-indigo-300">Khaled Dosoky</a>
                    </span>
                    <span className="text-gray-500">|</span>
                    <span className="truncate"> {/* Added truncate for long repo URL on small screens */}
                        <a href="https://github.com/KhaledDosoky/math-expressions" target="_blank" rel="noopener noreferrer" className="text-indigo-400 hover:text-indigo-300">GitHub 🔗</a>
                    </span>
                </footer>
            </div>
        </>
    );
}