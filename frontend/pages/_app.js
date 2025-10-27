// pages/_app.js
import '../styles/globals.css';
import { Inter, JetBrains_Mono } from 'next/font/google';

const inter = Inter({ subsets: ['latin'], variable: '--font-ui' });
const jetbrainsMono = JetBrains_Mono({ subsets: ['latin'], variable: '--font-code' });
export const metadata = {
    title: 'Expr Playground',
};
export default function App({ Component, pageProps }) {
    return <Component {...pageProps} />
}
