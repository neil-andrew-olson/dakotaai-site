#!/bin/bash

# ============================================
# DAB Token Deployment Script for Solana
# Dakota AI Bridge (DAB) Token
# ============================================

# Configuration
TOKEN_NAME="DAB"
TOKEN_SYMBOL="DAB"
TOKEN_DECIMALS=9
INITIAL_SUPPLY=1000000000  # 1 billion tokens (with 9 decimals = 1000.000000000)
DESCRIPTION="Dakota AI Bridge - AI-Powered DeFi Intelligence"
IMAGE_URL="https://dakotaai.us/DAB-token-logo.png"
TAG="AI DEFI Bridge Utility"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}    DAB Token Deployment Script     ${NC}"
echo -e "${BLUE}    Dakota AI Bridge (DAB)           ${NC}"
echo -e "${BLUE}========================================${NC}"

# Check prerequisites
echo -e "${YELLOW}Checking prerequisites...${NC}"

# Check if Solana CLI is installed
if ! command -v solana &> /dev/null; then
    echo -e "${RED}❌ Solana CLI not found. Install it first:${NC}"
    echo "curl -sSfL https://release.solana.com/v1.18.4/install | sh"
    echo "export PATH=\"$HOME/.local/share/solana/install/active_release/bin:$PATH\""
    exit 1
fi

# Check if spl-token CLI is installed
if ! command -v spl-token &> /dev/null; then
    echo -e "${RED}❌ spl-token CLI not found. Install it:${NC}"
    echo "cargo install spl-token-cli"
    exit 1
fi

echo -e "${GREEN}✅ Prerequisites check passed${NC}"

# Display current configuration
echo -e "${YELLOW}Current configuration:${NC}"
echo "Network: $(solana config get | grep -E '^(RPC|Cluster)' | sed 's/^.*: //' | tr '\n' ' ')"
echo "Wallet: $(solana config get | grep 'Keypair' | sed 's/^.*: //')"

# Confirmation prompt
echo -e "${RED}⚠️  WARNING: This will deploy a token to the blockchain!${NC}"
read -p "Are you sure you want to proceed? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Deployment cancelled."
    exit 1
fi

# Check wallet balance
echo -e "${YELLOW}Checking wallet balance...${NC}"
BALANCE=$(solana balance | grep -oE '[0-9]+\.[0-9]+' | head -1)
REQUIRED_BALANCE=0.5

if (( $(echo "$BALANCE < $REQUIRED_BALANCE" | bc -l) )); then
    echo -e "${RED}❌ Insufficient balance. Need at least $REQUIRED_BALANCE SOL, you have $BALANCE SOL${NC}"
    echo "Fund your wallet with SOL first."
    exit 1
fi

echo -e "${GREEN}✅ Balance check passed: $BALANCE SOL${NC}"

# Generate token mint address
echo -e "${YELLOW}Creating SPL Token...${NC}"
TOKEN_ADDRESS=$(spl-token create-token --decimals $TOKEN_DECIMALS | grep -oE '[A-Za-z0-9]{32,}' | tail -1)

if [ -z "$TOKEN_ADDRESS" ]; then
    echo -e "${RED}❌ Failed to create token${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Token created successfully!${NC}"
echo -e "${BLUE}Token Address: ${TOKEN_ADDRESS}${NC}"

# Create token account
echo -e "${YELLOW}Creating token account...${NC}"
TOKEN_ACCOUNT=$(spl-token create-account "$TOKEN_ADDRESS" | grep -oE '[A-Za-z0-9]{32,}' | tail -1)

if [ -z "$TOKEN_ACCOUNT" ]; then
    echo -e "${RED}❌ Failed to create token account${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Token account created: $TOKEN_ACCOUNT${NC}"

# Mint initial supply
echo -e "${YELLOW}Minting initial supply of ${INITIAL_SUPPLY} tokens...${NC}"
spl-token mint "$TOKEN_ADDRESS" "$INITIAL_SUPPLY"

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Successfully minted $INITIAL_SUPPLY $TOKEN_SYMBOL tokens${NC}"
else
    echo -e "${RED}❌ Failed to mint tokens${NC}"
    exit 1
fi

# Create metadata (optional, requires Metaplex)
echo -e "${YELLOW}Creating token metadata...${NC}"
echo "Note: This step requires Metaplex CLI for full metadata"

# Disable future minting (recommended)
echo -e "${YELLOW}Disabling future minting...${NC}"
spl-token authorize "$TOKEN_ADDRESS" mint --disable

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Mint authority disabled - supply is now fixed${NC}"
else
    echo -e "${RED}⚠️  Could not disable mint authority${NC}"
fi

# Save token information
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}       DAB TOKEN DEPLOYMENT COMPLETE     ${NC}"
echo -e "${BLUE}========================================${NC}"

echo "
DAB_TOKEN_INFO:
Name: $TOKEN_NAME
Symbol: $TOKEN_SYMBOL
Decimals: $TOKEN_DECIMALS
Total Supply: $INITIAL_SUPPLY (Fixed)
Token Address: $TOKEN_ADDRESS
Token Account: $TOKEN_ACCOUNT
Network: Solana Devnet/Mainnet
Deployed by: Dakota AI Bridge
" > dab-token-info.txt

echo -e "${GREEN}📄 Token information saved to dab-token-info.txt${NC}"
echo -e "${GREEN}🎉 DAB Token deployment successful!${NC}"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "1. Verify token on Solana Explorer"
echo "2. Set up DEX listing on Raydium/OpenBook"
echo "3. Create liquidity pool"
echo "4. Update your DAB wallet with token support"
echo "5. Announce token launch to community"

echo ""
echo -e "${BLUE}Token Address: ${TOKEN_ADDRESS}${NC}"
echo -e "${BLUE}Explorer URL: https://explorer.solana.com/address/${TOKEN_ADDRESS}${NC}"
