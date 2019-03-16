#sumof digits is palindrome or not
t = int(input())
while t:
    n = int(input())
    s = 0
    count = 0
    while n>0:
        d = n%10
        s = s + d
        count = count + 1
        n = int(n/10)
    
    temp = s
    len = s
    leng = 0
    count2 = 0
    while len>0:
        e = (len%10)
        leng = leng + e
        count2 = count2 +1
        len = int(len/10)
    rev = 0
    while(temp>0):
        dig=temp%10
        rev=rev*10+dig
        temp=temp//10