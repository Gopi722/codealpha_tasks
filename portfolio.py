
# Simple Stock Portfolio Tracker

# Define your portfolio as a dictionary
# Format: "Stock Symbol": (price_per_share, number_of_shares)
portfolio = {
    "AAPL": (175, 10),    # Apple: price $175, 10 shares
    "GOOGL": (140, 5),    # Google: price $140, 5 shares
    "TSLA": (250, 4),     # Tesla: price $250, 4 shares
    "AMZN": (135, 8)      # Amazon: price $135, 8 shares
}

# Function to calculate total investment
def calculate_investment(portfolio):
    total = 0
    print("\nYour Portfolio:")
    print("----------------")
    for stock, (price, shares) in portfolio.items():
        value = price * shares
        print(f"{stock}: {shares} shares × ${price} = ${value}")
        total += value
    return total

# Run the tracker
total_investment = calculate_investment(portfolio)
print("----------------")
print(f"💰 Total Investment Value = ${total_investment}")