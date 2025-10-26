"use client";

import { useEffect } from "react";
import Editor, { useMonaco } from "@monaco-editor/react";
import { registerExprLanguage } from "../lib/exprLanguage";

export default function ExprEditor({ code, onChange }) {
    const monaco = useMonaco();

    useEffect(() => {
        if (monaco) registerExprLanguage(monaco);
    }, [monaco]);

    return (
        <Editor
            height="100%"           // fill parent container
            language="expr"
            value={code}
            onChange={(value) => onChange(value ?? "")}
            theme="vs-dark"
            options={{
                automaticLayout: true,
                fontSize: 14,
                minimap: { enabled: false },
                scrollBeyondLastLine: false,
                renderWhitespace: "all",
            }}
        />
    );
}
