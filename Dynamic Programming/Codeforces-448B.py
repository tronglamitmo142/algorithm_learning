# - suffix automation: xoa 1 ki tu 
# - suffix array: hoan doi vi tri cua 2 ki tu bat ky trong xau
# - suffix tree: nhieu thao tac hon (bao gom ca 2 pp)

# abcde
# bcd

#automation: s[i] >= t[i] dung thu tu  
# array: s[i] == t[i]
# both: s[i] >= t[i] va khong dung thu tu 
# need tree: s[i] < t[i]
from re import T
import string

def main(s, t):
    count_letter_s = dict.fromkeys(string.ascii_lowercase, 0)
    count_letter_t = dict.fromkeys(string.ascii_lowercase, 0)
    is_array = True 
    for letter in s:
        count_letter_s[letter] += 1 
    for letter in t:
        count_letter_t[letter] += 1 
    for letter in string.ascii_lowercase: 
        if count_letter_s[letter] < count_letter_t[letter]:
            return "need tree"
        if count_letter_s[letter] > count_letter_t[letter]:
            is_array = False 
    if is_array == True:
        return "array"
# check thu tu
    i = 0
    for letter in t:
        is_found = False 
        while i < len(s):
            if s[i] == letter:
                is_found = True
                break
            i += 1 
        if is_found == False: 
            return "both"
        else: 
            i += 1 
    return "automaton" 


print(main(input(), input()))