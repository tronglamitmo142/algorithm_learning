# We will compare S + 1 with T, if S + 1 > T => no such string, else: return S+1 

def check_string(S,T):
    check = False 
    for i in range(len(S) -1, -1, -1):
        if S[i] == "a":
            S[i] = "z"
        else:
            S[i] = chr(ord(S[i]) + 1)
            check = True
            break 
    if check == False:
        return "No such string"
    for i in range(len(S)):
        if S[i] > T[i]:
            return "No such string"
        elif S[i] < T[i]:
            return "".join(S)
    return "No such string"

S = list(input())
T = list(input())
print(check_string(S, T))