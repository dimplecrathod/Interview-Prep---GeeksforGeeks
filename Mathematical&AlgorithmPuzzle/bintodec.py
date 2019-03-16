#binary to decimal

t = int(input())
while t:
    b = int(input())
    temp = b
    dec = 0
    count = 0
    while ( temp >0):
        d = temp % 10
        dec = dec + d*(2**count)
        count = count + 1
        temp = int(temp/10)
    
    print(dec)
    t = t-1