#lcm and gcd 

def gcd(x,y):
    if x > y:
        smaller = x
        bigger = y
    else:
        smaller = y
        bigger = x

    while smaller:
        bigger , smaller = smaller, bigger%smaller
    return bigger
    
  
  
t = int(input())
while t:
    a = input()
    arr = [int(s) for s in a.split() if s.isdigit()]
    A = arr[0]
    B = arr[1]
    Gcd = gcd(A,B)
    Lcm = int((A*B)//Gcd)
    print(Lcm,Gcd)
        
    t = t-1