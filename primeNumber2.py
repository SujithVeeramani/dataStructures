n=int(input())
count=0
i=1

while (i*i <=n):

    if n%i ==0:
        count+=1

        if n//i != 0:
            count+=1
    i+=1
print(True) if count==2 else print(False)
