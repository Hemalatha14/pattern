n=int(input("enter no of rows"))
m=int(n/2)
N=int(n+1/2)
for i in range(1,m+2):
    print(" "*(N-i-1)+"* "*(i))
for j in range(n-m-1,0,-1):
    print(" "*(N-j-1)+"* "*(j))
    
