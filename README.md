# Binance Futures Testnet Trading Bot

This is a simplified crypto trading bot built in Python for the Binance Futures Testnet.  
It allows users to place **market** and **limit** buy/sell orders using the Binance API via command-line interface.

---

## ✅ Features

- Connects to Binance Futures **Testnet** using API keys
- Places **MARKET** and **LIMIT** orders (Buy/Sell)
- Uses official `python-binance` library
- Logs all actions, responses, and errors in a file (`bot.log`)
- User-friendly command-line interface (CLI)
- Structured for clarity and modular code

---

## 🚀 How to Run the Bot

### 1. Clone or Download the Project

```bash
git clone https://github.com/Sanchita2803/binance-trading-bot.git
cd binance-trading-bot
```
**Install Required Library**
```bash
pip install python-binance
```
### ⚠️ Configure Your API Keys
Go to `config.py` and insert your own Binance Futures Testnet API key and secret:

```python
API_KEY = "your_api_key_here"
API_SECRET = "your_secret_here"
BASE_URL = "https://testnet.binancefuture.com"
```
### ▶️ Run the Bot

After setting up your API keys, run the bot using the following command:

```bash
python cli.py
```
