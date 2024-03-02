# gcd(a,b) = gcd (a-b,b) where a>b

x,y =map(int, input().split())

def gcd(x,y):

    while (x>0 and y>0):
    
        if x>y :
            x= x%y
        else:
            y = y%x 

    print(x) if y==0 else print(y)


gcd(x,y)
