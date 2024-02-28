n = int(input())
divisors=[]

for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        divisors.append(i)
        if n // i != i:
            divisors.append(n//i)

for i in sorted(divisors):
    print(i, end=' ')


