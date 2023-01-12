# link para o problema: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        # declara preço mínimo como um número infinito
        min_price = float('inf')
        for price in prices:
            min_price = min(min_price, price)  # encontra o preço mínimo
            profit = price - min_price  # encontra a posição do dia para melhor venda
            max_profit = max(max_profit, profit)
        return max_profit


if __name__ == "__main__":
    resposta = Solution()
    print(resposta.maxProfit([7, 1, 5, 3, 6, 4]))
