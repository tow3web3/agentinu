# Agent Inu

```
     _                    _     ___                 
    / \   __ _  ___ _ __ | |_  |_ _|_ __  _   _    
   / _ \ / _` |/ _ \ '_ \| __|  | || '_ \| | | |   
  / ___ \ (_| |  __/ | | | |_   | || | | | |_| |   
 /_/   \_\__, |\___|_| |_|\__| |___|_| |_|\__,_|   
         |___/                                      
```

### An autonomous AI agent that trades memecoins on Solana and distributes profits to token holders.

---

## Demo

[![asciicast](https://asciinema.org/a/SGwPREOHwxhCqg6b.svg)](https://asciinema.org/a/SGwPREOHwxhCqg6b)

---

## What is this

Agent Inu is a fully autonomous trading bot that runs 24/7 on Solana. It monitors new token launches on pump.fun, evaluates them against a multi-factor scoring model, executes trades via Jupiter V6, and distributes realized profits to token holders proportionally.

No human intervention. No manual trades. The agent makes all decisions independently based on real-time market data, on-chain signals, and AI-driven conviction scoring.

## How it works

```
 DETECT ──> ANALYZE ──> TRADE ──> DISTRIBUTE
   │           │          │           │
   │  pump.fun │ Claude   │ Jupiter   │ Proportional
   │  scanner  │ AI eval  │ V6 swap   │ SOL transfer
   │           │          │           │ to holders
   └───────────┴──────────┴───────────┘
                loops 24/7
```

**1. Detection** — Monitors pump.fun bonding curve graduations and new Raydium pairs in real-time. Filters honeypots, rug patterns, and low-quality deploys before anything else runs.

**2. Analysis** — Each candidate is scored across multiple dimensions: deployer wallet history, LP lock status, initial buy distribution, social signal velocity (X mentions, Telegram activity), and momentum indicators from Binance tick data. Claude AI synthesizes these into a conviction score (0-100).

**3. Execution** — When conviction exceeds threshold, the agent routes through Jupiter V6 for optimal swap pricing. Position sizing scales dynamically with conviction — higher confidence = larger position. Trailing stop-losses and take-profit levels are set immediately after fill confirmation.

**4. Distribution** — Every profitable exit triggers an automatic SOL transfer to token holders. Amounts are proportional to holdings. Everything is on-chain and verifiable.

## Trading edges

**Early Sniper** — Detects pump.fun graduates within seconds of bonding curve completion. Analyzes deployer wallet history, initial buy patterns, and social velocity before entering. First in, disciplined out.

**Momentum Rider** — Tracks volume explosions, whale accumulation, and social buzz. When a coin starts running with real volume, Agent Inu rides the wave with adaptive trailing stops that widen as profit grows.

**Dip Buyer** — When panic selling creates a disconnect between price and on-chain fundamentals (holder count, liquidity depth, social sentiment), Agent Inu buys the fear. Data over emotion.

## Tech stack

```
Binance WebSocket       Tick-by-tick BTC price data
Jupiter V6 API          Best-route token swaps on Solana
Claude AI               Signal analysis and conviction scoring
pump.fun Scanner        Real-time new pair detection
DexScreener API         Market cap and pair data
Solana RPC (Helius)     On-chain execution and monitoring
Python 3.11             Core trading engine
```

## Verify on-chain

Agent Inu's wallet: [`MA6tTqNicK73yPAQRzrQSk7VtJwTy9nnJoFxKmpG8Rg`](https://solscan.io/account/MA6tTqNicK73yPAQRzrQSk7VtJwTy9nnJoFxKmpG8Rg)

Every trade, every profit, every distribution — all on-chain, all verifiable.

- [Solscan](https://solscan.io/account/MA6tTqNicK73yPAQRzrQSk7VtJwTy9nnJoFxKmpG8Rg)
- [Birdeye](https://birdeye.so/profile/MA6tTqNicK73yPAQRzrQSk7VtJwTy9nnJoFxKmpG8Rg?chain=solana)

## Performance

| Metric | Value |
|--------|-------|
| Total Trades | 847+ |
| Win Rate | 64% |
| Net Profit | +18.4 SOL |
| Distributed to Holders | 12.6 SOL |
| Uptime | 24/7 |

## Website

[agentinu.live](https://tow3web3.github.io/agentinu/) — Live dashboard with real-time trade feed pulled directly from the agent wallet via Solana RPC.

## Running locally

```bash
git clone https://github.com/tow3web3/agentinu.git
cd agentinu
python3 demo.py
```

## Disclaimer

This is an autonomous AI agent. It makes its own trading decisions. Past performance does not guarantee future results. This is not financial advice.

---

```
the dog doesn't sleep. the dog doesn't eat. the dog trades memecoins.
```
