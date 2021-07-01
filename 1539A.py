for iters in range(int(input())):
    n,x,t=[int(i) for i in input().split(" ")]
    p=t//x
    print(int(n*p-p*p/2-p/2))