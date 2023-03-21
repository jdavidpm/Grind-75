def maxProfit(prices):
    buy_index = 0
    sel_index = 0
    best_price = 0
    
    for i in range(1, len(prices)):
        if prices[i] < prices[buy_index]:
            buy_index = i
            sel_index = i
        if prices[i] > prices[sel_index]:
            sel_index = i
        if (buy_index <= sel_index):
            best_price = max(prices[sel_index] - prices[buy_index], best_price)
            
    return best_price
