def main(s1, s2):
# check string letter is different or not
# check index different = 2 or not
    dict_s1 = {}
    dict_s2 = {}
    count = 0 
    for char in s1:
        if char not in dict_s1:
            dict_s1[char] = 1
        else: 
            dict_s1[char] += 1 
    for char in s2: 
        if char not in dict_s2:
            dict_s2[char] = 1 
        else:
            dict_s2[char] += 1 
    if dict_s1 != dict_s2:
        return False
    else:
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            else:
                count += 1 
        if count == 2:
            return True
    return False         

s1 = input()
s2 = input()
print(main(s1, s2))