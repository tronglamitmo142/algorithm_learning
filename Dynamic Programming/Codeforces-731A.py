def find_min(list_letter):
    list_letter = "a" + list_letter ## In the beginning, pointer at "a"
    sum_letter = 0
    for i in range(len(list_letter) - 1): # -1 because we add "a" in list_letter
        distance = abs(ord(list_letter[i]) - ord(list_letter[i+1]))
        sum_letter += min(26-distance, distance) # We always have two option, turn left and turn right
    return sum_letter

list_letter = input()
print(find_min(list_letter))
