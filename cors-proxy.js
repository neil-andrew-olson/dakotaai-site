const express = require('express');
const request = require('request');
const cors = require('cors');

const app = express();
const PORT = 3000;

// Enable CORS for all routes
app.use(cors());

// CORS proxy for Polymarket API
app.use('/api/polymarket', (req, res) => {
  const targetUrl = `https://gamma-api.polymarket.com${req.url.replace('/api/polymarket', '')}`;
  console.log(`Proxying: ${req.method} ${req.url} -> ${targetUrl}`);

  req.pipe(request({
    url: targetUrl,
    headers: {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
      'Accept': 'application/json',
      ...req.headers
    }
  })).pipe(res);
});

// CORS proxy for Polymarket Data API
app.use('/api/polymarket-data', (req, res) => {
  const targetUrl = `https://data-api.polymarket.com${req.url.replace('/api/polymarket-data', '')}`;
  console.log(`Proxying: ${req.method} ${req.url} -> ${targetUrl}`);

  req.pipe(request({
    url: targetUrl,
    headers: {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
      'Accept': 'application/json',
      ...req.headers
    }
  })).pipe(res);
});

// Serve static files from current directory
app.use(express.static('.'));

app.listen(PORT, () => {
  console.log(`🚀 Polymarket CORS Proxy Server running!`);
  console.log(`📡 Local proxy: http://localhost:${PORT}`);
  console.log(`🎯 Scanner URL: http://localhost:${PORT}/demos/polymarket-scanner.html`);
  console.log(`\n📋 API endpoints:`);
  console.log(`   Markets: http://localhost:${PORT}/api/polymarket/markets?...`);
  console.log(`   Trades: http://localhost:${PORT}/api/polymarket-data/trades?...`);
  console.log(`\n🛑 Press Ctrl+C to stop the server`);
});
