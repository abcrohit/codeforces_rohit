def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
def combinatorics(n,m):
    return factorial(n)/factorial(m)/factorial(n-m)
m=input()
k=m.split(" ")

n=int(k[0])
k=int(k[1])
ans=0
for i in range(1,n+1):
    ans+=combinatorics(n,i)*((n-1)**(n-i))*((i)**k)
ans*=n
print(ans)