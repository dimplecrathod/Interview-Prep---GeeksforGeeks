#armstrong numbers
t= int(input())
while t:
    num = int(input())
    n = num
    s = 0
    order = 3

    while n>0:
        d = n%10
        s = s + (d**order)
        n = int(n /10)
    if s == num:
        print('Yes')
    else:
       print('No')
    t= t-1

  