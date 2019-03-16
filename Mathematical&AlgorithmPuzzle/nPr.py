#nPr
#code
def nPr(n, r):
    return (fact(n) /fact(n - r))

# Returns factorial of n
def fact(n):
    if n==0:
        res = 1

    else:
        res=n*fact(n-1)
    return res

# Driver code
t = int(input())
while t:
    #string 
    n = input()
    #splitting string to get n and r
    arr =[int(s) for s in n.split() if s.isdigit()]
    N = arr[0]
    R = arr[1]
    print(int(nPr(N,R)))
    t=t-1