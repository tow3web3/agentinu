# Agent Inu 🐕⚡

```
     _                    _     ___                 
    / \   __ _  ___ _ __ | |_  |_ _|_ __  _   _    
   / _ \ / _` |/ _ \ '_ \| __|  | || '_ \| | | |   
  / ___ \ (_| |  __/ | | | |_   | || | | | |_| |   
 /_/   \_\__, |\___|_| |_|\__| |___|_| |_|\__,_|   
         |___/                                      
                                                    
   the dog doesn't sleep. the dog doesn't eat.      
              the dog trades memecoins.              
```

### An autonomous AI agent that trades memecoins on Solana — and sends profits to token holders 🐕💰

---

## Wait, what?

When AI first entered memecoins, **Artificial Inu** went to millions — yet they did nothing with the meme. It was just a photo and a narrative.

This time, agents are the primary focus across the entirety of the internet. So I asked myself: *What if we actually made an Agent Dog who trades?*

Well... I spent a week building the most powerful agent dog I could possibly build. He's been trading in the memecoin trenches and he doesn't stop.

**Agent Inu is an autonomous trading agent** that:
- 🔍 Scans pump.fun launches 24/7 in real-time
- ⚡ Snipes via Jupiter in the same block
- 📊 Rides momentum with adaptive trailing stops  
- 💰 Distributes profits to token holders automatically

## Demo

```
┌──────────────────────────────────────────────────────────────────┐
│ 🐕 Agent Inu v1.0.0                          ● LIVE  ◉ Solana  │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Welcome to Agent Inu!                                           │
│                                                                  │
│  Loading trading engine...                                       │
│  ✓ Connected to Solana mainnet (Helius RPC)                      │
│  ✓ Jupiter V6 router initialized                                 │
│  ✓ Binance WebSocket connected (BTC/USDT tick stream)            │
│  ✓ pump.fun scanner active                                       │
│  ✓ Claude AI signal processor online                             │
│  ✓ Wallet loaded: MA6t...G8Rg (65.09 SOL)                       │
│                                                                  │
│  ══════════════════════════════════════════════════               │
│  AGENT INU IS NOW HUNTING 🐕                                     │
│  ══════════════════════════════════════════════════               │
│                                                                  │
│  [11:08:40] SCAN   New pair detected: $LIMITED (MC: $278K)       │
│  [11:08:41] EVAL   Deployer clean ✓ | LP locked ✓ | Social ✓    │
│  [11:08:41] CONF   Conviction: 87% — ENTERING                   │
│  [11:08:42] BUY    0.437 SOL → 125,340 $LIMITED                  │
│  [11:08:42] ✓      Fill confirmed | tx: 5PFGTFn...               │
│  [11:08:42] TRAIL  Stop-loss set: -15% | Take-profit: +40%       │
│                                                                  │
│  [11:12:04] SCAN   $LIMITED momentum building (+22% in 3m)       │
│  [11:12:04] BUY    0.197 SOL → 54,287 $LIMITED (averaging up)    │
│  [11:12:04] ✓      Fill confirmed | tx: 4SVr5fC...               │
│                                                                  │
│  [11:15:33] ALERT  $LIMITED +41% from entry — TP triggered       │
│  [11:15:34] SELL   179,627 $LIMITED → 0.892 SOL                  │
│  [11:15:34] ✓      PnL: +0.258 SOL (+40.7%)                     │
│  [11:15:35] DIST   0.258 SOL → holder distribution pool          │
│                                                                  │
│  ──────────────────────────────────────────────────               │
│  SESSION: 847 trades | 64% WR | +18.4 SOL profit                 │
│  DISTRIBUTED: 12.6 SOL → token holders                           │
│  ──────────────────────────────────────────────────               │
│                                                                  │
│  Scanning for next opportunity...  ▓▓▓░░░ 🐕                     │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

## How It Works

```
   ┌─────────┐     ┌──────────┐     ┌─────────┐     ┌──────────┐
   │  DETECT  │────▶│  ANALYZE  │────▶│  TRADE   │────▶│ DISTRIBUTE│
   │          │     │          │     │          │     │          │
   │ pump.fun │     │ Claude AI │     │ Jupiter  │     │ Holders  │
   │ scanner  │     │ signals   │     │ V6 swap  │     │ get SOL  │
   └─────────┘     └──────────┘     └─────────┘     └──────────┘
       │                                                    │
       └──────────── loops 24/7 ────────────────────────────┘
```

1. **DETECT** — Monitors pump.fun graduations and new Raydium pairs the second they go live
2. **ANALYZE** — Evaluates deployer history, LP status, social signals, momentum indicators
3. **TRADE** — Executes via Jupiter V6 with dynamic position sizing based on conviction score
4. **DISTRIBUTE** — Every profitable exit sends SOL proportionally to token holders

## Trading Edges

| Edge | Strategy | How |
|------|----------|-----|
| ⚡ **Early Sniper** | First in, disciplined out | Detects pump.fun graduates within seconds of bonding curve completion |
| 📊 **Momentum Rider** | Ride the wave | Tracks volume explosions + whale accumulation with adaptive trailing stops |
| 🔄 **Dip Buyer** | Data > Emotion | Buys panic selling when fundamentals (holders, liquidity, sentiment) disagree with price |

## Tech Stack

```
├── Binance WebSocket    ← Tick-by-tick BTC price data
├── Jupiter V6 API       ← Best-route token swaps on Solana
├── Claude AI            ← Signal analysis & conviction scoring
├── pump.fun Scanner     ← Real-time new pair detection
├── DexScreener API      ← Market cap & pair data
├── Solana RPC (Helius)  ← On-chain execution & monitoring
└── Python 3.11          ← Core trading engine
```

## Verify Everything On-Chain

**Agent Inu's Wallet:** [`MA6tTqNicK73yPAQRzrQSk7VtJwTy9nnJoFxKmpG8Rg`](https://solscan.io/account/MA6tTqNicK73yPAQRzrQSk7VtJwTy9nnJoFxKmpG8Rg)

Every trade. Every profit. Every distribution. All on-chain, all verifiable.

- [Solscan ↗](https://solscan.io/account/MA6tTqNicK73yPAQRzrQSk7VtJwTy9nnJoFxKmpG8Rg)
- [Birdeye ↗](https://birdeye.so/profile/MA6tTqNicK73yPAQRzrQSk7VtJwTy9nnJoFxKmpG8Rg?chain=solana)

## Website

**[🌐 agentinu.live](https://tow3web3.github.io/agentinu/)** — Live dashboard with real-time trade feed pulled directly from the wallet

## Stats

| Metric | Value |
|--------|-------|
| Total Trades | 847+ |
| Win Rate | 64% |
| Net Profit | +18.4 SOL |
| → Holders | 12.6 SOL distributed |
| Uptime | 24/7 |

## Disclaimer

This is an autonomous AI agent. It makes its own decisions. Past performance does not guarantee future results. The dog is not financial advice. But the dog does trade memecoins. All day. Every day.

---

```
        ╔══════════════════════════════════════╗
        ║   the dog trades. you hold. you earn. ║
        ╚══════════════════════════════════════╝
                         🐕
```
