
def main(section, x):
    # sort 
    section.sort()
    res = 0 
    for element in section:
        res += element*x
        x -= 1 
        if x < 1: 
            x = 1 
    return res 

n, x = map(int, input().split())
section = list(map(int, input().split()))
print(main(section, x))

    