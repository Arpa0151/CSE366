
import random
import matplotlib.pyplot as plt
# Constants
AVG_PRICE = 600  # Average smartphone price
THRESHOLD_DISCOUNT = 0.2  # 20% discount threshold
CRITICAL_STOCK_LEVEL = 10  # Critical stock level
DEFAULT_ORDER_QUANTITY = 10  # Minimum order for low stock

# Simulated inputs
prices = [500, 550, 600, 650, 700]  # Example prices
stocks = [5, 15, 25, 8, 30]  # Example stock levels
orders = []  # List to store order decisions

# Decision logic
for price, stock in zip(prices, stocks):
    threshold_price = AVG_PRICE * (1 - THRESHOLD_DISCOUNT)  # Calculate discounted price threshold
    if stock < CRITICAL_STOCK_LEVEL:  # Critical stock condition
        orders.append(DEFAULT_ORDER_QUANTITY)
    elif price < threshold_price:  # Price below discount threshold
        orders.append(15)  # Larger order
    else:  # No order
        orders.append(0)

# Print decisions for clarity
print("Price, Stock, Order Decision")
for price, stock, order in zip(prices, stocks, orders):
    print(f"{price} BDT, {stock} units, {order} units ordered")

# Plotting the results
plt.figure(figsize=(8, 5))
plt.bar(range(len(prices)), orders, color='blue', alpha=0.7, label='Orders')
plt.xticks(range(len(prices)), [f"{p} BDT" for p in prices])
plt.xlabel("Smartphone Price")
plt.ylabel("Units Ordered")
plt.title("Trading Agent Order Decisions")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
