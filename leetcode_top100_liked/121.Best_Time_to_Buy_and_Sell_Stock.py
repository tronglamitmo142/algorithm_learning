# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Solution: 2 pointer 
def main(prices):
    left, right = 0, 1 
    max_profit = 0 
    while right < len(prices): 
        if prices[left] < prices[right]:
            current_profit = prices[right] - prices[left]
            max_profit = max(max_profit, current_profit)
        else:
            left= right 
        right += 1 
    return max_profit

prices = list(map(int, input().split()))
print(main(prices))