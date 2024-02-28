n= int(input())
originalNumber = n
reverseNumber=0

while n > 0:
    lastDigit=n%10
    n = n // 10
    reverseNumber = (reverseNumber * 10) +lastDigit

print( reverseNumber == originalNumber )


