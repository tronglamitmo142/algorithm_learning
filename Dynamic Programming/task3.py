def time_to_watching(n, list_n):
    time_to_watching.append(90)
    time_to_watching = list_n[0]
    if time_to_watching > 15: # if time > 15 -> boring 
        return 15 
    else:
        for i in range(i, len(list_n)): 
            time_between_2_time_points = list_n[i] - list_n[i-1]
            if time_between_2_time_points <= 15:
                time_to_watching = list_n[i]
            else:
                time_to_watching += 15 
                break
    return time_to_watching

N = int(input())
list_n = list(map(int, input().split()))
print(time_to_watching(N, list_n))

