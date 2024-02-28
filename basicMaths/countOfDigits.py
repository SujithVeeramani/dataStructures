n=int(input())
count=0
while n > 0:
    lastDigit=n%10
    n = n // 10
    count+=1

print(f"Count of digits :{count}")