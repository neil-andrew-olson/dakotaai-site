export default async function handler(req, res) {
  // Enable CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');

  // Handle preflight requests
  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }

  try {
    // Build the Polymarket API URL
    const baseUrl = 'https://gamma-api.polymarket.com';
    const queryString = new URLSearchParams(req.query).toString();
    const apiUrl = `${baseUrl}${req.url.replace('/api/polymarket', '').split('?')[0]}${queryString ? '?' + queryString : ''}`;

    console.log('Proxying Polymarket request:', apiUrl);

    // Make the request to Polymarket
    const response = await fetch(apiUrl, {
      method: req.method,
      headers: {
        'User-Agent': 'Mozilla/5.0 (compatible; DakotaAI/1.0)',
        'Accept': 'application/json',
        ...req.headers
      },
      body: req.method !== 'GET' && req.method !== 'HEAD' ? JSON.stringify(req.body) : undefined
    });

    // Get the response data
    const data = await response.text();

    // Set the response headers and status
    res.status(response.status);

    // Copy relevant headers from Polymarket response
    const contentType = response.headers.get('content-type');
    if (contentType) {
      res.setHeader('Content-Type', contentType);
    }

    // Return the data
    res.send(data);

  } catch (error) {
    console.error('Polymarket API proxy error:', error);
    res.status(500).json({
      error: 'Failed to proxy request to Polymarket API',
      details: error.message
    });
  }
}
