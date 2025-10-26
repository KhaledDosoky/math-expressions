export function registerExprLanguage(monaco) {
    // Register the language
    monaco.languages.register({ id: "expr" });

    // Define syntax highlighting
    monaco.languages.setMonarchTokensProvider("expr", {
        keywords: ["assert", "print", "or", "and", "not"],
        operators: ["+", "-", "*", "/", "%", "^", "==", "!=", "<=", ">=", "<", ">"],
        tokenizer: {
            root: [
                [/#.*$/, "comment"],                       // comments
                [/\d+(\.\d+)?([eE][+-]?\d+)?/, "number"], // decimal + e-notation
                [/\d+(\.\d+)?x10\^\d+/, "number"],        // scientific notation like 3x10^2
                [/\b(assert|print|or|and|not)\b/, "keyword"],
                [/==|!=|<=|>=|<|>/, "operator"],          // multi-char operators
                [/[+\-*/%^]/, "operator"],                // single-char operators
                [/[a-zA-Z_][a-zA-Z0-9_]*/, "identifier"],
                [/[()]/, "delimiter.parenthesis"],
                [/[ \t\r\n]+/, "white"],
            ],
        },
    });

    // Define brackets and auto-closing pairs
    monaco.languages.setLanguageConfiguration("expr", {
        comments: { lineComment: "#" },
        brackets: [["(", ")"]],
        autoClosingPairs: [{ open: "(", close: ")" }],
        surroundingPairs: [{ open: "(", close: ")" }],
    });
}
