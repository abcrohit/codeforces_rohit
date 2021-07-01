for iters in range(int(input())):
    n=int(input())
    array=[int(i) for i in input().split(" ")]
    sum=0
    for i in range(n):
        sum+=array[i]
    if(sum<n):
        print(1)
    elif(sum>n):
        print(sum-n)
    else:
        print(0)
    
