#rev number
#code
t=int(input())
while t>0:
    n=int(input())
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    print(rev)
    t-=1