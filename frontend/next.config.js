/** @type {import('next').NextConfig} */
const nextConfig = {
  // ... other configurations
  output: 'standalone', // 👈 This is the critical line
  // ...
};

module.exports = nextConfig;