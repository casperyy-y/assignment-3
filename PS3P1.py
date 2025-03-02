stock_symbol = input("Enter stock ticker symbol ")
shares = int(input("Enter number of shares "))
cost_per_share = float(input("Enter cost per share "))
amount_invested = shares * cost_per_share
print("Stock Symbol: ", stock_symbol)
print("Total Amount Invested: ", amount_invested)
