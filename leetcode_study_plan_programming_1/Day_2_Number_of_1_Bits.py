# https://leetcode.com/problems/number-of-1-bits/
# Using Bitwise operator: https://www.geeksforgeeks.org/python-bitwise-operators/
# &: return 

def main(n):
    res = 0 
    while n:
        n = n & (n-1) # if last bit = 1 => remove 
        res += 1 
        print(n)
    return res
    
n = int(input())
print(main(n))