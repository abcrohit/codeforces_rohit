t=int(input())
for i in range(t):
    n=100
    m=int(input())
    if m%2==0:
        m/=2
        n//=2
    if m%2==0:
        m/=2
        n//=2
    if m%5==0:
        m/=5
        n//=5
    if m%5==0:
        m/=5
        n//=5
    print(n)
