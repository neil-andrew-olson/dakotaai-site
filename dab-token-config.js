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
      mint: "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v", // REPLACE WITH YOUR DEPLOYED ADDRESS
      bridge: "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v" // UPDATE WHEN BRIDGE CONTRACT DEPLOYED
    },
    devnet: {
      mint: "DEVNET_ADDRESS_HERE", // For testing
      bridge: "DEVNET_BRIDGE_HERE"
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
      fee: 0.001 // ETH
    },
    {
      name: "BSC",
      networkId: "bsc",
      chainId: 56,
      bridgeAddress: "0x0000000000000000000000000000000000000000", // UPDATE
      fee: 0.001 // BNB
    },
    {
      name: "opBNB",
      networkId: "opbnb",
      chainId: 204,
      bridgeAddress: "0x0000000000000000000000000000000000000000", // UPDATE
      fee: 0.0001 // opBNB
    }
  ],

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
