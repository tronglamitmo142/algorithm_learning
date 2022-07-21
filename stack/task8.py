for t in range(int(input())):
    s = input()
    cnt, ans = 0, 0
    for i in range(len(s)):
        if s[i] == '<':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            ans = i + 1
        elif cnt < 0:
            break
    print(ans)
