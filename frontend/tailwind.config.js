/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./app/**/*.{js,ts,jsx,tsx}",       // Next.js 13+ app dir
        "./pages/**/*.{js,ts,jsx,tsx}",     // pages dir
        "./components/**/*.{js,ts,jsx,tsx}" // components
    ],
    theme: { extend: {} },
    plugins: [],
}
