# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 170,
    "MSFT": 420
}

total_investment = 0
portfolio = []

print("===== Stock Portfolio Tracker =====")

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available!")
        continue

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    portfolio.append([stock, quantity, price, investment])

# Display portfolio
print("\n===== Portfolio Summary =====")
print("Stock\tQuantity\tPrice\tInvestment")

for item in portfolio:
    print(f"{item[0]}\t{item[1]}\t\t₹{item[2]}\t₹{item[3]}")

print("--------------------------------")
print(f"Total Investment: ₹{total_investment}")

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("-----------------------\n")

    for item in portfolio:
        file.write(
            f"{item[0]} - Quantity: {item[1]}, "
            f"Price: ₹{item[2]}, Investment: ₹{item[3]}\n"
        )

    file.write(f"\nTotal Investment: ₹{total_investment}")

print("\nPortfolio saved successfully to portfolio.txt")