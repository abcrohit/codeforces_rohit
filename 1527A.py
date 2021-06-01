T=int(input())
for i in range(T):
    m=int(input())
    p=m
    j=0
    while(m//2!=0):
        j+=1
        m=m//2
    print(2**j-1)