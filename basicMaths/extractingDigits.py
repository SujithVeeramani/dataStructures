n=int(input())
while n > 0:
    lastDigit=n%10
    n = n // 10
    print(lastDigit)
    
# time complexity = O( log n base 10)
# base 10 for dividing by 10 , if n //2 then 
# tc = O(log n base 2)