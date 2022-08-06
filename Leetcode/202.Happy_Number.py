def main(n):
    count = 0
    while n != 1 and count < 10: 
        s = str(n)
        sum_ = 0 
        for char in s: 
            sum_ += (int(char) ** 2)
        n = sum_
        count += 1 
    if n == 1:
        return True 
    return False

n = int(input())
print(main(n))
