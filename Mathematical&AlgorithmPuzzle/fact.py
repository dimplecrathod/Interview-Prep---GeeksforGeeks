#factorial 

def fact(x):
    if x==0:
        fac = 1
    else:
        fac =1
        while (x>0):
            fac = fac*(x)
            x = x-1
        
    return fac


t = int(input())

while t:
    n = int(input())
    res = int(fact(n))
    print(res)
    t = t-1