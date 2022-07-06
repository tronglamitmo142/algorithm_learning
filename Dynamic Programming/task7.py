# 1 
# nhaapj sai k lan -> mat 5 giay 
# n, k 
# count 
# check len
# cba bb1 => 1 + 1 + 5 
# abC ABC => 1 + 1 +5 
# abc => 1 

def main(N, K, password, true_password):
    lower_password = 0 
    equal_password = 0 
    for each_password in password:
        if len(each_password) < len(true_password):
            lower_password += 1 
        if len(each_password) == len(true_password):
            equal_password += 1 
    min_attemp = lower_password//K*5 + lower_password + 1 
    max_attemp = (lower_password + equal_password - 1)//K*5 + lower_password + equal_password

    return min_attemp, max_attemp

N, K = map(int, input().split())
password =[]
for i in range(N):
    password.append(input())
true_password = input()
min_attemp, max_attemp = main(N, K, password, true_password)
print(min_attemp, max_attemp)
        
# 1 2 3 4 5 6 k -> +5 



# check do dai so voi password
# 3 so 
 # Best options: nhập len(password) < len(true_password) -> len(password) == len(true_password) -> =  => return min_attemp
# worst option: len(password) < len(true_password) -> len(password) == len(true_password) -> 