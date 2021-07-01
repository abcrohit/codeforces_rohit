iter=int(input())
for iters in range(iter):
    n,k=input().split(" ")
    n,k=int(n),int(k)
    array=[int(i) for i in input().split(" ")]
    pointer=0
    while(pointer!=n-1 and k!=0):
        print(pointer)
        d=array[pointer]
        if d==0:
            pointer+=1
        else:
            a=min(k,d)
            k=k-a
            array[pointer]-=a
            array[n-1]+=a
            pointer+=1
    print(array)
    
