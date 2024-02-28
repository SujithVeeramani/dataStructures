n=int(input())
originalNumber = n
total = 0

while n > 0:
    lastDigit= n % 10
    n = n // 10
    total+= lastDigit**3

print( originalNumber == total)


    
