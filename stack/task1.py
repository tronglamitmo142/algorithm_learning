def main(s):
    stack = []
    rpn = ''
    for i in range(len(s)):
        if s[i].isalpha():
            rpn += s[i]
        elif s[i] == ')':
            rpn += stack.pop()
        elif s[i] != '(': 
            stack.append(s[i])
    return rpn 

n = int(input())
for i in range(n): 
    s = input()
    print(main(s))

