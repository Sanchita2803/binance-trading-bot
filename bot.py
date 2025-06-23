from binance.client import Client
from config import API_KEY, API_SECRET, BASE_URL
from logger import log_info, log_error

class BasicBot:
    def __init__(self):
        self.client = Client(API_KEY, API_SECRET, testnet=True)
        self.client.FUTURES_URL = BASE_URL

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            order_data = {
                "symbol": symbol.upper(),
                "side": side.upper(),
                "type": order_type.upper(),
                "quantity": quantity
            }
            if order_type.upper() == "LIMIT" and price:
                order_data["price"] = price
                order_data["timeInForce"] = "GTC"
            order = self.client.futures_create_order(**order_data)
            log_info(f"Order placed: {order}")
            return order
        except Exception as e:
            log_error(f"Order failed: {e}")
            return {"error": str(e)}