from bot import BasicBot

def main():
    print("Welcome to the Binance Testnet Trading Bot 💹")
    symbol = input("Enter trading pair (e.g. BTCUSDT): ").strip()
    side = input("Buy or Sell: ").strip().upper()
    order_type = input("Order type (MARKET or LIMIT): ").strip().upper()
    quantity = float(input("Enter quantity: "))
    price = None
    if order_type == "LIMIT":
        price = float(input("Enter limit price: "))

    bot = BasicBot()
    response = bot.place_order(symbol, side, order_type, quantity, price)
    print("\nResponse:")
    print(response)

if __name__ == "__main__":
    main()
