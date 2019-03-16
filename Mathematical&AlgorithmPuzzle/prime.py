#prime
t = int(input())
while t:
    n = int(input())
    flag = 0
    for i in range(2, n-1):
        if(n%i ==0):
            flag = 1
            break
    
    if(flag == 1):
        print('No')
    else:
        print('Yes')
        
    t = t-1
            