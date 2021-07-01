for iters in range(int(input())):
    n=int(input())
    num=[int(i) for i in input().split(" ")]
    num.sort()
    negative=0
    for i in range(0,n):
        negative+=(n-2*i-1)*num[i]
    negative+=num[n-1]
    print(negative)
