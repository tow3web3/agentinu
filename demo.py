#!/usr/bin/env python3
"""Agent Inu terminal demo — for recording"""
import time, sys, random

CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
WHITE = "\033[97m"
DIM = "\033[90m"
BOLD = "\033[1m"
RESET = "\033[0m"

def slow(text, delay=0.015):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def fast(text):
    slow(text, 0.005)

def instant(text):
    print(text)

banner = f"""{CYAN}{BOLD}
     _                    _     ___                 
    / \\   __ _  ___ _ __ | |_  |_ _|_ __  _   _    
   / _ \\ / _` |/ _ \\ '_ \\| __|  | || '_ \\| | | |   
  / ___ \\ (_| |  __/ | | | |_   | || | | | |_| |   
 /_/   \\_\\__, |\\___|_| |_|\\__| |___|_| |_|\\__,_|   
         |___/                                      
{RESET}"""

print(banner)
time.sleep(0.5)

slow(f"{GREEN}Welcome to Agent Inu v1.0.0{RESET}")
time.sleep(0.3)
print()

slow(f"{WHITE}Initializing trading engine...{RESET}", 0.02)
time.sleep(0.4)

components = [
    ("Solana mainnet (Helius RPC)", 0.3),
    ("Jupiter V6 swap router", 0.2),
    ("Binance WebSocket (BTC/USDT)", 0.4),
    ("pump.fun pair scanner", 0.2),
    ("Claude AI signal processor", 0.3),
    ("DexScreener market data", 0.2),
]
for comp, delay in components:
    time.sleep(delay)
    fast(f"  {GREEN}✓{RESET} {WHITE}{comp}{RESET}")

time.sleep(0.3)
print()
fast(f"{WHITE}Wallet loaded: {CYAN}MA6t...G8Rg{RESET} {DIM}(65.09 SOL){RESET}")
time.sleep(0.5)
print()
instant(f"{GREEN}{'═'*60}{RESET}")
slow(f"{GREEN}{BOLD}  AGENT INU IS NOW HUNTING{RESET}", 0.03)
instant(f"{GREEN}{'═'*60}{RESET}")
print()
time.sleep(1)

# Simulated trading session
trades = [
    {
        "scan": ("$LIMITED", "$278K", "pump.fun graduate"),
        "eval": ["Deployer clean", "LP locked", "Social velocity high"],
        "conf": 87,
        "buy": ("0.437", "125,340", "$LIMITED"),
        "sig": "5PFGTFnH",
        "trail": ("-15%", "+40%"),
        "wait": 3,
        "momentum": "+22% in 3m",
        "avg_up": ("0.197", "54,287"),
        "sig2": "4SVr5fCC",
        "sell_trigger": "+41% from entry",
        "sell": ("179,627", "0.892"),
        "pnl": ("+0.258", "+40.7%"),
        "dist": "0.258",
    },
    {
        "scan": ("$PNUT", "$1.2M", "Raydium V4"),
        "eval": ["Deployer 12 tokens launched", "LP: 85% locked 30d", "X mentions spiking"],
        "conf": 72,
        "buy": ("0.310", "8,420", "$PNUT"),
        "sig": "3kQ9mNvT",
        "trail": ("-12%", "+35%"),
        "wait": 4,
        "momentum": None,
        "sell_trigger": "Stop-loss hit -12%",
        "sell": ("8,420", "0.273"),
        "pnl": ("-0.037", "-11.9%"),
        "pnl_loss": True,
        "dist": None,
    },
    {
        "scan": ("$GIGA", "$450K", "pump.fun graduate"),
        "eval": ["Deployer 100% clean", "LP burned", "Telegram active"],
        "conf": 93,
        "buy": ("0.520", "340,200", "$GIGA"),
        "sig": "7xRtKp2W",
        "trail": ("-18%", "+50%"),
        "wait": 5,
        "momentum": "+65% in 8m",
        "sell_trigger": "+52% from entry — TP triggered",
        "sell": ("340,200", "1.121"),
        "pnl": ("+0.601", "+115.6%"),
        "dist": "0.601",
    },
]

ts_base = 1108  # 11:08
for i, t in enumerate(trades):
    ts = ts_base + i * 7
    h, m = 11, ts % 60
    
    # Scan
    name, mc, source = t["scan"]
    fast(f"  {DIM}[{h}:{m:02d}:40]{RESET} {YELLOW}SCAN{RESET}   New pair detected: {CYAN}{name}{RESET} {DIM}(MC: {mc} via {source}){RESET}")
    time.sleep(0.5)
    
    # Eval
    for ev in t["eval"]:
        fast(f"  {DIM}[{h}:{m:02d}:41]{RESET} {WHITE}EVAL{RESET}   {ev} {GREEN}✓{RESET}")
        time.sleep(0.15)
    
    # Confidence
    conf = t["conf"]
    color = GREEN if conf >= 80 else YELLOW if conf >= 60 else RED
    fast(f"  {DIM}[{h}:{m:02d}:41]{RESET} {color}CONF{RESET}   Conviction: {color}{conf}%{RESET} — {'ENTERING' if conf >= 60 else 'SKIP'}")
    time.sleep(0.3)
    
    # Buy
    sol, amt, token = t["buy"]
    fast(f"  {DIM}[{h}:{m:02d}:42]{RESET} {GREEN}BUY {RESET}   {sol} SOL → {amt} {token}")
    time.sleep(0.2)
    fast(f"  {DIM}[{h}:{m:02d}:42]{RESET} {GREEN}  ✓{RESET}    Fill confirmed {DIM}| tx: {t['sig']}...{RESET}")
    
    lo, hi = t["trail"]
    fast(f"  {DIM}[{h}:{m:02d}:42]{RESET} {WHITE}TRAIL{RESET}  Stop: {RED}{lo}{RESET} | TP: {GREEN}{hi}{RESET}")
    print()
    time.sleep(t["wait"])
    
    m2 = m + 4
    
    # Momentum / avg up
    if t.get("momentum") and t.get("avg_up"):
        fast(f"  {DIM}[{h}:{m2:02d}:04]{RESET} {YELLOW}SCAN{RESET}   {t['scan'][0]} momentum building ({t['momentum']})")
        sol2, amt2 = t["avg_up"]
        fast(f"  {DIM}[{h}:{m2:02d}:04]{RESET} {GREEN}BUY {RESET}   {sol2} SOL → {amt2} {t['scan'][0]} {DIM}(averaging up){RESET}")
        fast(f"  {DIM}[{h}:{m2:02d}:04]{RESET} {GREEN}  ✓{RESET}    Fill confirmed {DIM}| tx: {t.get('sig2','')}...{RESET}")
        print()
        time.sleep(2)
        m2 += 3
    
    # Sell
    is_loss = t.get("pnl_loss", False)
    trigger_color = GREEN if not is_loss else RED
    fast(f"  {DIM}[{h}:{m2+1:02d}:33]{RESET} {trigger_color}ALERT{RESET}  {t['sell_trigger']}")
    time.sleep(0.3)
    
    sell_amt, sell_sol = t["sell"]
    fast(f"  {DIM}[{h}:{m2+1:02d}:34]{RESET} {RED if is_loss else YELLOW}SELL{RESET}   {sell_amt} {t['scan'][0]} → {sell_sol} SOL")
    
    pnl_sol, pnl_pct = t["pnl"]
    pnl_color = GREEN if not is_loss else RED
    fast(f"  {DIM}[{h}:{m2+1:02d}:34]{RESET} {pnl_color}  P&L{RESET}  {pnl_color}{pnl_sol} SOL ({pnl_pct}){RESET}")
    
    if t.get("dist"):
        fast(f"  {DIM}[{h}:{m2+1:02d}:35]{RESET} {GREEN}DIST{RESET}   {t['dist']} SOL → holder distribution pool")
    
    print()
    time.sleep(1.5)

# Summary
print()
instant(f"  {DIM}{'─'*56}{RESET}")
fast(f"  {WHITE}SESSION:{RESET}  847 trades | 64% WR | {GREEN}+18.4 SOL{RESET} profit")
fast(f"  {WHITE}SENT:{RESET}     {GREEN}12.6 SOL{RESET} distributed to token holders")
instant(f"  {DIM}{'─'*56}{RESET}")
print()
time.sleep(1)
slow(f"  {DIM}Scanning for next opportunity...{RESET}", 0.03)
