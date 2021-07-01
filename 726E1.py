for iters in range(int(input())):
    n,m=(int(i) for i in input().split(" "))
    array=input()
    s=n
    i=1
    while(i<s):
        temp=s
        if(ord(array[0])==ord(array[i])):
            j=0
            l=i
            while(l<s):
                if(ord(array[j])<ord(array[l])):
                    s=l
                    break
                j+=1
                l+=1
        if(temp!=s):
            break
        if(ord(array[0])<ord(array[i])):
            s=i
            break
        i+=1
    array2=array[0:s]
    output=""
    for i in range(m):
        output+=array2[i%len(array2)]
    print(output)
        