import argparse

from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

from bot.logging_config import setup_logging


def main():

    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price")

    args = parser.parse_args()

    symbol = args.symbol.upper()
    side = validate_side(args.side)
    order_type = validate_order_type(args.type)
    quantity = validate_quantity(args.quantity)
    price = validate_price(args.price)

    if order_type == "LIMIT" and price is None:
        raise ValueError("LIMIT order requires price")

    print("\nOrder Request Summary")
    print("---------------------")
    print("Symbol:", symbol)
    print("Side:", side)
    print("Type:", order_type)
    print("Quantity:", quantity)
    print("Price:", price)

    order = place_order(symbol, side, order_type, quantity, price)

    print("\nOrder Response")
    print("Order ID:", order.get("orderId"))
    print("Status:", order.get("status"))
    print("Executed Qty:", order.get("executedQty"))
    print("Avg Price:", order.get("avgPrice"))

    print("\nOrder placed successfully")


if __name__ == "__main__":
    main()