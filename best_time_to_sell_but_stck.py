def buy_sell_stcok(prices):
    l=0
    r=1
    max_profit=0
    while r<len(prices):
        if prices[l]<prices[r]:
            profit=prices[r]-prices[l]
            max_profit=max(max_profit,profit)   
        else:
            l=r
        r+=1
    return max_profit
print(buy_sell_stcok([7,1,5,3,6,4]))
print(buy_sell_stcok([7,6,4,3,1]))
    