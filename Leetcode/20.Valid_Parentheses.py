# https://leetcode.com/problems/valid-parentheses/
# Solution: Using stack 

def main(s):
    stack_open_parentheses = [] # If find open parentheses => put to stack 
    open_paren = ['(', '{', '[']
    close_paren = [')', '}', ']']
    for i in s:
        if i in open_paren:
            stack_open_parentheses.append(i)
        elif i == ')' and stack_open_parentheses and stack_open_parentheses[-1] == '(':
            stack_open_parentheses.pop(-1)
        elif i == ']' and stack_open_parentheses and stack_open_parentheses[-1] == '[':
            stack_open_parentheses.pop(-1)
        elif i == '}' and stack_open_parentheses and stack_open_parentheses[-1] == '{':
            stack_open_parentheses.pop(-1)
        else:
            return False
    if len(stack_open_parentheses) == 0:
        return True
    return False

s = input()
print(main(s))