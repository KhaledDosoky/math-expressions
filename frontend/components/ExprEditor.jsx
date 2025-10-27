"use client";

import { useEffect, useRef } from "react";
import Editor, { useMonaco } from "@monaco-editor/react";
import { registerExprLanguage } from "../lib/exprLanguage";

export default function ExprEditor({ code, onChange, fontSize }) {
    const monaco = useMonaco();

    const editorRef = useRef(null);

    // Function to store the editor instance
    function handleEditorDidMount(editor, monaco) {
        editorRef.current = editor;
    }

    useEffect(() => {
        if (monaco) registerExprLanguage(monaco);
    }, [monaco]);

    useEffect(() => {
        if (editorRef.current) {
            editorRef.current.updateOptions({
                fontSize: fontSize // <-- This line updates Monaco
            });
        }
    }, [fontSize]); // Rerun effect when fontSize changes

    return (
        <Editor
            height="100%"           // fill parent container
            language="expr"
            value={code}
            onChange={(value) => onChange(value ?? "")}
            theme="vs-dark"
            options={{
                automaticLayout: true,
                fontSize: fontSize,
                minimap: { enabled: false },
                scrollBeyondLastLine: false,
                renderWhitespace: "none",
            }}
        />
    );
}
