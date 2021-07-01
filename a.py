iter=int(input())
for iters in range(iter):
    a,b,c,d=(int(i) for i in input().split(" "))
    a,b,c,d=int(a),int(b),int(c),int(d)
    if(min(a,b)<max(c,d) and min(c,d)<max(a,b)):
        print("YES")
    else:
        print("NO")
