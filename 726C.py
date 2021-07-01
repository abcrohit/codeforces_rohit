for iters in range(int(input())):
    n=int(input())
    array=[int(i) for i in input().split(" ")]
    array.sort()
    current=array[1]-array[0]
    j=0
    for i in range(n-1):
        if(array[i+1]-array[i]<=current):
            j=i
    a=array.pop(j)
    b=array.pop(j)
    semiout1=""
    if(j<n-2):
        semiout1=' '.join(map(str, array[j:]))+' '
    semiout2=' '.join(map(str,array[0:j]))
    # print(str(a)+*array+str(b))
    print(str(a)+" "+semiout1+semiout2+" "+str(b))