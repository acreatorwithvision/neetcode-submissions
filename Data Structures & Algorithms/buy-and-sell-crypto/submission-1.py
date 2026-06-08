class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        max_profit=0

        for i in prices:
            buy=min(buy,i)
            

            price=i-buy
            max_profit=max(max_profit, price)

        return max_profit