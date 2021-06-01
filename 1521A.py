T=int(input())
for i in range(T):
    a,b=(input().split(" "))
    a=int(a)
    b=int(b)
    if(b==1):
        print("NO")
    else:
        print("YES")
        print(f"{a} {a*b} {a*b+a}")