# --- Stock Portfolio Tracker ---

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 200
}

total_portfolio_value = 0
summary_lines = []

print('--- Stock Portfolio Tracker ---')
print("Available stocks: ['AAPL', 'TSLA', 'GOOGL', 'MSFT']")
print("Enter stock and quantity (e.g., AAPL 5) or type 'DONE' to finish.")

while True:
    user_input = input("\n >> Input (TICKER QUANTITY): ").upper()

    if user_input == "DONE":
        break
 
    # main logic of the code 
    try:
        ticker, quantity = user_input.split()
        quantity = int(quantity)

        if ticker in stock_prices:
            price = stock_prices[ticker]
            added_value = price * quantity
            total_portfolio_value += added_value

            print(f"✅ Added {quantity} shares of {ticker}. Current Total: ${total_portfolio_value:}")

            # Save to summary
            summary_lines.append(f"{ticker} - {quantity} shares → ${added_value:}")

        else:
            print("❌ Unknown stock ticker. Try again.")

    except ValueError:
        print("❌ Invalid input format! Example: AAPL 5")

# ----- Final Output -----


print(f"📊 FINAL TOTAL INVESTMENT VALUE: ${total_portfolio_value:.2f}")
print("=============================================")

# ----- Save to file -----

with open("portfolio_summary.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    for line in summary_lines:
        file.write(line + "\n")
    file.write("\n")
    file.write(f"TOTAL: ${total_portfolio_value:}")

print("💾 Summary successfully saved to portfolio_summary.txt")
print("(✿◕‿◕✿) Thank you for using the Stock Portfolio Tracker!")