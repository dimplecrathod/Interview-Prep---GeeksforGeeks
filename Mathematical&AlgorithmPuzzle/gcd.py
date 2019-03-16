#gcd

def gcd(x,y):
    if x>y:
        smaller = y
    else:
        smaller = x
        
    for i in range(1,smaller+1):
        if(( x%i==0) and (y%i)==0):
            gcd = i
    return gcd
    
t = int(input())
while t:
    a = input()
    arr = [int(s) for s in a.split() if s.isdigit()]
    A = arr[0]
    B = arr[1]
    res = gcd(A,B)
    print(res)
    t = t-1