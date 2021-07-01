for iters in range(int(input())):
    n=int(input())
    num=[int(i) for i in input().split(" ")]
    count=0
    for i in range(n-1):
        for j in range(i+1,n):
            if(num[i]*num[j]==i+j+2):
                count+=1
    print(count)