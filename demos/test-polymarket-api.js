const fetch = require('node-fetch');

async function testPolymarketAPI() {
  console.log('🔍 Testing Polymarket API access...\n');

  try {
    // Test 1: Get recent resolved markets
    console.log('📊 Testing markets endpoint...');
    const marketsUrl = 'https://gamma-api.polymarket.com/markets?closed=true&active=false&limit=10&order_by=end_date&desc=true';
    console.log('URL:', marketsUrl);

    const marketsResponse = await fetch(marketsUrl, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'application/json'
      }
    });

    if (!marketsResponse.ok) {
      throw new Error(`Markets API failed: ${marketsResponse.status} ${marketsResponse.statusText}`);
    }

    const markets = await marketsResponse.json();
    console.log(`✅ Found ${markets.length} markets\n`);

    // Show sample market data
    if (markets.length > 0) {
      const sample = markets[0];
      console.log('📋 Sample market data:');
      console.log(`   Question: ${sample.question?.substring(0, 60)}...`);
      console.log(`   Tags: ${JSON.stringify(sample.tags)}`);
      console.log(`   End Date: ${sample.end_date}`);
      console.log(`   Resolution: ${sample.resolution}\n`);

      // Test 2: Get trades for first market
      if (sample.clobTokenIds && sample.outcomes) {
        console.log('💰 Testing trades endpoint...');
        try {
          const tokenIds = JSON.parse(sample.clobTokenIds);
          if (tokenIds.length > 0) {
            const tradesUrl = `https://data-api.polymarket.com/trades?token_id=${tokenIds[0]}&limit=5&sortBy=TIMESTAMP&sortDirection=DESC`;
            console.log('URL:', tradesUrl);

            const tradesResponse = await fetch(tradesUrl, {
              headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept': 'application/json'
              }
            });

            if (tradesResponse.ok) {
              const trades = await tradesResponse.json();
              console.log(`✅ Found ${trades.length} trades for market`);
              if (trades.length > 0) {
                const sampleTrade = trades[0];
                console.log('📋 Sample trade data:');
                console.log(`   Side: ${sampleTrade.side}`);
                console.log(`   Price: ${sampleTrade.price}`);
                console.log(`   Size: ${sampleTrade.size}`);
                console.log(`   Value: $${(parseFloat(sampleTrade.size) * parseFloat(sampleTrade.price)).toFixed(2)}`);
                console.log(`   Address: ${sampleTrade.maker_address?.substring(0, 10)}...`);
              }
            } else {
              console.log(`❌ Trades API failed: ${tradesResponse.status}`);
            }
          }
        } catch (tradeError) {
          console.log('❌ Error testing trades:', tradeError.message);
        }
      }
    }

    console.log('\n🎉 Polymarket API is accessible! The issue is browser CORS restrictions.');
    console.log('💡 Use this data to configure your scanner or CORS proxy properly.');

  } catch (error) {
    console.log('❌ API Test Failed:', error.message);
    console.log('\n🔧 Possible issues:');
    console.log('   - Network connectivity');
    console.log('   - Polymarket API down');
    console.log('   - Firewall blocking requests');
    console.log('   - Rate limiting');
  }
}

// Run the test
testPolymarketAPI();
