T = int(input())
def gcd(a,b):
    if(a==b):
        return a
    else:
        return(gcd(min(a,b),abs(b-a)))
    
for iter in range(T):
    n=int(input())
    operations=[0]*n
    k=0
    number_array1=(input().split(" "))
    number_array=[int(i) for i in number_array1]
    a=number_array[0]
    b=number_array[1]
    if(gcd(a,b)!=1):
        number_array[0]=min(a,b)
        number_array[1]=number_array[0]+1
        operations[k]=(f"{1} {2} {number_array[0]} {number_array[1]}")
        k+=1
    for i in range(1,n-1):
        a=number_array[i]
        b=number_array[i+1]
        d=number_array[i-1]
        c=min(a,b)
        if (gcd(a,b)!=1):
            if(gcd(c,d)!=1):
                number_array[i+1]=c
                number_array[i]=c+1
                operations[k]=(f"{i+1} {i+2} {c+1} {c}")
                k+=1
            else:
                number_array[i]=c
                number_array[i+1]=c+1
                operations[k]=(f"{i+1} {i+2} {c} {c+1}")
                k+=1
    print(k)
    for i in range(k):
        print(operations[i])
    print(operations)


        

# ['1 2 3 4', '4 5 4 5', '10 11 12 13', '12 13 8 9', '13 14 7 6', 0, 0, 0, 0, 0, 0, 0, 0, 0]