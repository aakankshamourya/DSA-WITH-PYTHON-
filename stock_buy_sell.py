def stock_buy_and_Sell(prices):
    n=len(prices)
    max_profit=0
    min_prices= float('-inf')
    for i in range(1,n):
        for j in range(i+1,n):
            min_prices=max(min_prices,prices[i])
            profit=prices[j]-prices[i]
            max_profit=max(max_profit,profit)
    return max_profit   
print(stock_buy_and_Sell([7,1,5,3,6,4]))
print(stock_buy_and_Sell([7,6,4,3,1]))
        