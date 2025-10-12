// ============================================
// DAB Token Configuration
// Dakota AI Bridge (DAB) Token
// ============================================

const DAB_TOKEN_CONFIG = {
  // Token Metadata
  name: "DAB",
  symbol: "DAB",
  fullName: "Dakota AI Bridge",
  description: "AI-Powered DeFi Intelligence & Cross-Chain Bridge Token",
  decimals: 9,
  initialSupply: "1000000000", // 1 billion tokens with 9 decimals

  // Network Addresses (UPDATE AFTER DEPLOYMENT)
  addresses: {
    mainnet: {
      mint: "DAB_TOKEN_ADDRESS_MAINNET", // Will be updated after deployment
      bridge: "DAB_BRIDGE_ADDRESS_MAINNET"
    },
    devnet: {
      mint: "DAB_TOKEN_ADDRESS_DEVNET", // For testing
      bridge: "DAB_BRIDGE_ADDRESS_DEVNET"
    },
    testnet: {
      mint: "TESTNET_ADDRESS_HERE",
      bridge: "TESTNET_BRIDGE_HERE"
    }
  },

  // Token Economics
  economics: {
    totalSupply: 1000000000, // Fixed supply
    circulatingSupply: 0, // Updated as tokens are distributed
    maxSupply: 1000000000, // No max supply limit

    // Distribution (example - customize as needed)
    distribution: {
      team: 100000000, // 10% - Team allocation
      community: 300000000, // 30% - Community rewards
      liquidity: 200000000, // 20% - DEX liquidity
      treasury: 200000000, // 20% - Treasury/reserve
      marketing: 100000000, // 10% - Marketing/development
      airdrop: 100000000  // 10% - Airdrop program
    }
  },

  // Bridge Configuration
  bridges: [
    {
      name: "Ethereum",
      networkId: "ethereum",
      chainId: 1,
      bridgeAddress: "0x0000000000000000000000000000000000000000", // UPDATE
      fee: 0.001, // ETH
      supportedTokens: ["ETH", "USDC", "USDT", "DAI", "WBTC", "LINK", "UNI", "AAVE", "MATIC"],
      nativeToken: "ETH"
    },
    {
      name: "BSC",
      networkId: "bsc",
      chainId: 56,
      bridgeAddress: "0x0000000000000000000000000000000000000000", // UPDATE
      fee: 0.001, // BNB
      supportedTokens: ["BNB", "BUSD", "USDT", "USDC", "CAKE", "BAKE", "DOT", "ADA"],
      nativeToken: "BNB"
    },
    {
      name: "opBNB",
      networkId: "opbnb",
      chainId: 204,
      bridgeAddress: "0x0000000000000000000000000000000000000000", // UPDATE
      fee: 0.0001, // opBNB
      supportedTokens: ["BNB", "USDT", "USDC", "OP", "SHIB", "DOGE"],
      nativeToken: "BNB"
    }
  ],

  // Supported Tokens for Multi-Token Exchange
  supportedTokens: {
    solana: [
      { symbol: "SOL", name: "Solana", address: "So11111111111111111111111111111111111111112", decimals: 9, logo: "https://cdn.jsdelivr.net/gh/solana-labs/token-list@main/assets/mainnet/So11111111111111111111111111111111111111112/logo.png" },
      { symbol: "USDC", name: "USD Coin", address: "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v", decimals: 6, logo: "https://cdn.jsdelivr.net/gh/solana-labs/token-list@main/assets/mainnet/EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v/logo.png" },
      { symbol: "USDT", name: "Tether", address: "Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB", decimals: 6, logo: "https://cdn.jsdelivr.net/gh/solana-labs/token-list@main/assets/mainnet/Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB/logo.png" },
      { symbol: "RAY", name: "Raydium", address: "4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R", decimals: 6, logo: "https://cdn.jsdelivr.net/gh/solana-labs/token-list@main/assets/mainnet/4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R/logo.png" },
      { symbol: "JITOSOL", name: "Jito Staked SOL", address: "J1toso1uCk3RLmjorhTtrVwY9HJ7X8V9yYac6Y7kGCPn", decimals: 9, logo: "https://cdn.jsdelivr.net/gh/solana-labs/token-list@main/assets/mainnet/J1toso1uCk3RLmjorhTtrVwY9HJ7X8V9yYac6Y7kGCPn/logo.png" },
      { symbol: "BONK", name: "Bonk", address: "DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263", decimals: 5, logo: "https://cdn.jsdelivr.net/gh/solana-labs/token-list@main/assets/mainnet/DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263/logo.png" },
      { symbol: "WIF", name: "dogwifhat", address: "EKpQGSJtjMFqKZ9KQanSqYXRcF8fBopzLHYxdM65zcjm", decimals: 6, logo: "https://cdn.jsdelivr.net/gh/solana-labs/token-list@main/assets/mainnet/EKpQGSJtjMFqKZ9KQanSqYXRcF8fBopzLHYxdM65zcjm/logo.png" },
      { symbol: "PYUSD", name: "PayPal USD", address: "2b1kV6DkPAnxd5ixfnxCpjxmKwqjjaYmCZfHsFu24GXo", decimals: 6, logo: "https://cdn.jsdelivr.net/gh/solana-labs/token-list@main/assets/mainnet/2b1kV6DkPAnxd5ixfnxCpjxmKwqjjaYmCZfHsFu24GXo/logo.png" },
      { symbol: "WBTC", name: "Wrapped Bitcoin", address: "3NZ9JMVBmGAqocybic2c7LQCJScmgsAZ6vQqTDzcqmJh", decimals: 8, logo: "https://cdn.jsdelivr.net/gh/solana-labs/token-list@main/assets/mainnet/3NZ9JMVBmGAqocybic2c7LQCJScmgsAZ6vQqTDzcqmJh/logo.png" },
      { symbol: "JUP", name: "Jupiter", address: "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN", decimals: 6, logo: "https://cdn.jsdelivr.net/gh/solana-labs/token-list@main/assets/mainnet/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN/logo.png" },
      { symbol: "DAB", name: "Dakota AI Bridge", address: "DAB_TOKEN_ADDRESS_MAINNET", decimals: 9, logo: "/DAB-token-logo.png" }
    ],

    ethereum: [
      { symbol: "ETH", name: "Ethereum", address: "0x0000000000000000000000000000000000000000", decimals: 18, logo: "https://assets.coingecko.com/coins/images/279/large/ethereum.png" },
      { symbol: "USDC", name: "USD Coin", address: "0xa0b86a33e6fe17541a473d7637b828b8ef9cc3b04", decimals: 6, logo: "https://assets.coingecko.com/coins/images/6319/large/USD_Coin_icon.png" },
      { symbol: "USDT", name: "Tether", address: "0xdac17f958d2ee523a2206206994597c13d831ec7", decimals: 6, logo: "https://assets.coingecko.com/coins/images/325/large/Tether-logo.png" },
      { symbol: "DAI", name: "Dai", address: "0x6b175474e89094c44da98b954eedeac495271d0f", decimals: 18, logo: "https://assets.coingecko.com/coins/images/9956/large/4943.png" },
      { symbol: "WBTC", name: "Wrapped Bitcoin", address: "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599", decimals: 8, logo: "https://assets.coingecko.com/coins/images/7598/large/wrapped_bitcoin_wbtc.png" },
      { symbol: "LINK", name: "Chainlink", address: "0x514910771af9ca656af840dff83e8264ecf986ca", decimals: 18, logo: "https://assets.coingecko.com/coins/images/877/large/chainlink-new-logo.png" },
      { symbol: "UNI", name: "Uniswap", address: "0x1f9840a85d5af5bf1d1762f925bdaddc4201f984", decimals: 18, logo: "https://assets.coingecko.com/coins/images/12504/large/uni.jpg" },
      { symbol: "AAVE", name: "Aave", address: "0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9", decimals: 18, logo: "https://assets.coingecko.com/coins/images/12645/large/AAVE.png" }
    ],

    bsc: [
      { symbol: "BNB", name: "BNB", address: "0x0000000000000000000000000000000000000000", decimals: 18, logo: "https://assets.coingecko.com/coins/images/825/large/bnb-icon2_2x.png" },
      { symbol: "BUSD", name: "Binance USD", address: "0xe9e7cea3dedca5984780bafc599bd69add087d56", decimals: 18, logo: "https://assets.coingecko.com/coins/images/9576/large/BUSD.png" },
      { symbol: "USDT", name: "Tether", address: "0x55d398326f99059ff775485246999027b3197955", decimals: 18, logo: "https://assets.coingecko.com/coins/images/325/large/Tether-logo.png" },
      { symbol: "USDC", name: "USD Coin", address: "0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d", decimals: 18, logo: "https://assets.coingecko.com/coins/images/6319/large/USD_Coin_icon.png" },
      { symbol: "CAKE", name: "PancakeSwap", address: "0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82", decimals: 18, logo: "https://assets.coingecko.com/coins/images/12632/large/pancakeswap-cake-logo.png" },
      { symbol: "BAKE", name: "BakeryToken", address: "0xe02df9e3e622debdd4012bb38da18a11543ce821", decimals: 18, logo: "https://assets.coingecko.com/coins/images/12588/large/3842.png" }
    ]
  },

  // DEX Integrations
  dexes: {
    solana: {
      raydium: {
        name: "Raydium",
        router: "675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8",
        factory: "675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8",
        supportedTokens: ["SOL", "USDC", "USDT", "RAY", "WBTC", "JUP"]
      },
      orca: {
        name: "Orca",
        router: "9W959DqEETiGZocYWCQPaJ6sBmUzgfxXfqGeTEdp3aQP",
        factory: "9W959DqEETiGZocYWCQPaJ6sBmUzgfxXfqGeTEdp3aQP",
        supportedTokens: ["SOL", "USDC", "USDT", "JITOSOL"]
      },
      jupiter: {
        name: "Jupiter Aggregator",
        api: "https://quote-api.jup.ag/v4",
        supportedTokens: ["ALL_SOLANA_TOKENS"]
      }
    },

    ethereum: {
      uniswap: {
        name: "Uniswap V3",
        router: "0xE592427A0AEce92De3Edee1F18E0157C05861564",
        factory: "0x1F98431c8aD98523631AE4a59f267346ea31F984",
        supportedTokens: ["ETH", "USDC", "USDT", "DAI", "WBTC", "LINK", "UNI", "AAVE"]
      },
      sushiswap: {
        name: "SushiSwap",
        router: "0xd9e1cE17f2641f24aE83637ab66a2cca9C378B9F",
        factory: "0xC0AEe478e3658e2610c5F7A4A2E1777cE9e4f2Ac",
        supportedTokens: ["ETH", "USDC", "USDT", "SUSHI"]
      }
    },

    bsc: {
      pancakeswap: {
        name: "PancakeSwap",
        router: "0x10ED43C718714eb63d5aA57B78B54704E256024E",
        factory: "0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73",
        supportedTokens: ["BNB", "BUSD", "USDT", "USDC", "CAKE", "BAKE"]
      }
    }
  },

  // Price Feed Providers
  priceFeeds: {
    coingecko: {
      api: "https://api.coingecko.com/api/v3",
      ids: {
        "solana": "solana",
        "ethereum": "ethereum",
        "bitcoin": "bitcoin",
        "tether": "tether",
        "usd-coin": "usd-coin",
        "dai": "dai",
        "chainlink": "chainlink",
        "uniswap": "uniswap",
        "aave": "aave",
        "matic-network": "matic-network",
        "binancecoin": "binancecoin",
        "pancakeswap-token": "pancakeswap-token",
        "raydium": "raydium",
        "bonk-inu": "bonk",
        "dogwifcoat": "dogwifhat"
      }
    },
    coinmarketcap: {
      api: "https://pro-api.coinmarketcap.com/v1",
      symbols: {
        "SOL": "SOL",
        "ETH": "ETH",
        "BTC": "BTC",
        "USDT": "USDT",
        "USDC": "USDC",
        "DAI": "DAI",
        "LINK": "LINK",
        "UNI": "UNI",
        "AAVE": "AAVE",
        "MATIC": "MATIC",
        "BNB": "BNB",
        "CAKE": "CAKE"
      }
    }
  },

  // Exchange Settings
  exchange: {
    maxSlippage: 0.5, // 0.5% max slippage
    defaultSlippage: 0.3, // 0.3% default slippage
    deadline: 1200, // 20 minutes deadline
    gasMultiplier: 1.1, // 10% gas buffer

    // DAB holder discount tiers
    dabHolderDiscounts: {
      bronze: 0.0025, // 0.25% discount
      silver: 0.0050, // 0.50% discount
      gold: 0.0075, // 0.75% discount
      platinum: 0.0100 // 1.00% discount
    }
  },

  // DEX Configuration
  dex: {
    raydium: {
      poolAddress: "POOL_ADDRESS_HERE", // UPDATE AFTER CREATE
      ammId: "AMM_ID_HERE"
    },
    serum: {
      marketAddress: "MARKET_ADDRESS_HERE"
    }
  },

  // AI Agent Rewards (example configuration)
  aiRewards: {
    bridgeFeeDiscount: 0.25, // 25% discount for DAB holders
    yieldBoost: 1.5, // 50% boost on AI-generated yields
    feeShare: 0.1, // 10% of bridge fees go to DAB stakers

    // Reward tiers
    tiers: [
      { minBalance: 0, multiplier: 1.0, name: "Bronze" },
      { minBalance: 10000, multiplier: 1.25, name: "Silver" },
      { minBalance: 50000, multiplier: 1.5, name: "Gold" },
      { minBalance: 100000, multiplier: 2.0, name: "Platinum" }
    ]
  },

  // Token Utility Features
  utilities: {
    bridgeDiscounts: true,
    aiAgentRewards: true,
    governanceRights: true,
    feeSharing: true,
    crossChainVoting: true,
    stakingRewards: true
  },

  // Social Links
  social: {
    website: "https://dakotaai.us",
    discord: "https://discord.gg/dakotaai",
    twitter: "https://twitter.com/DakotaAi64396",
    telegram: "https://t.me/dakotaai",
    github: "https://github.com/neil-andrew-olson/dakota-ai-bridge"
  },

  // Development Roadmap
  roadmap: {
    phase1: {
      name: "Launch",
      status: "active",
      items: [
        "Token deployment on Solana",
        "Basic bridge functionality",
        "DAB wallet integration"
      ]
    },
    phase2: {
      name: "Growth",
      status: "planned",
      items: [
        "Multi-chain bridge expansion",
        "DEX listing and liquidity",
        "Community rewards program"
      ]
    },
    phase3: {
      name: "Expansion",
      status: "future",
      items: [
        "AI agent marketplace",
        "Cross-chain governance",
        "DeFi protocol integrations"
      ]
    }
  },

  // Technical Specifications
  technical: {
    blockchain: "Solana",
    standard: "SPL-Token",
    decimals: 9,
    totalSupply: "1,000,000,000",
    contractType: "Fixed Supply",
    mintAuthority: "Disabled", // No more tokens can be minted
    freezeAuthority: "None"
  }
};

// Helper functions
DAB_TOKEN_CONFIG.getCurrentSupply = function() {
  // Calculate current circulating supply
  return this.economics.circulatingSupply || 0;
};

DAB_TOKEN_CONFIG.getRewardMultiplier = function(balance) {
  for (const tier of this.aiRewards.tiers.slice().reverse()) {
    if (balance >= tier.minBalance) {
      return tier.multiplier;
    }
  }
  return 1.0;
};

DAB_TOKEN_CONFIG.formatAmount = function(amount) {
  return (amount / Math.pow(10, this.decimals)).toFixed(2);
};

DAB_TOKEN_CONFIG.getTokenTier = function(balance) {
  for (const tier of this.aiRewards.tiers.slice().reverse()) {
    if (balance >= tier.minBalance) {
      return tier.name;
    }
  }
  return "Community";
};

// Export for use in wallet
if (typeof module !== 'undefined' && module.exports) {
  module.exports = DAB_TOKEN_CONFIG;
}

// Make available globally for web use
if (typeof window !== 'undefined') {
  window.DAB_TOKEN_CONFIG = DAB_TOKEN_CONFIG;
}
