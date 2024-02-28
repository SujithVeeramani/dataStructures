n=int(input())
reverseNumber=0
while n > 0:
    lastDigit=n%10
    n = n // 10
    reverseNumber = (reverseNumber * 10) +lastDigit

print(reverseNumber)

# 1234500 -> 0054321 == 54321
