class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1 
        sum = 0 
        while n != 0:
            a = n % 10 
            n = n // 10
            product *= a 
            sum += a 
        return product - sum 
            