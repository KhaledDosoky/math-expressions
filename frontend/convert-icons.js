import sharp from 'sharp';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

async function convertSvgToPng() {
  const publicDir = path.join(__dirname, 'public');

  // Convert 192x192 icon
  await sharp(path.join(publicDir, 'icon-192x192.svg'))
    .png()
    .toFile(path.join(publicDir, 'icon-192x192.png'));

  // Convert 512x512 icon
  await sharp(path.join(publicDir, 'icon-512x512.svg'))
    .png()
    .toFile(path.join(publicDir, 'icon-512x512.png'));

  console.log('Icons converted successfully!');
}

convertSvgToPng().catch(console.error);