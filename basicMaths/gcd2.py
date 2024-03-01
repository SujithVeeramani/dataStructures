x,y =map(int, input().split())

for i in range(min(x,y),0,-1):
    if (x % i == 0) and (y % i == 0):
        print(i)
        break
    else: 
        pass
