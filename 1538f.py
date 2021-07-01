for iters in range(int(input())):
    b,a=input().split(" ")
    prev=0
    b1=len(b)
    a1=len(a)
    output=0
    if(b1!=a1):
        n=a1-b1
        b="0"*n+b
    for i in range(a1):
        prev=prev*10 + int(a[i])-int(b[i])
        output+=(prev)
    print(output)