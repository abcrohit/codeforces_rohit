T = int(input())
def gcd(a,b):
    if(a==b):
        return a
    else:
        return(gcd(min(a,b),abs(b-a)))
    
for i in range(T):
    n=int(input())
    number_array1=(input().split(" "))
    number_array2=[int(i) for i in number_array1]
    K=0
    for i in range(n-1):
        number_array=number_array2.copy()
        a=number_array[i]
        b=number_array[i+1]
        c=min(a,b)
        # print(gcd(a,b))
        if (gcd(a,b)!=1):
            number_array[i]=c
            number_array[i+1]=c+1
            # print(f"{i} {i+1} {c} {c+1}")
            K+=1
    print(K)
    for i in range(n-1):
        number_array=number_array2
        a=number_array[i]
        b=number_array[i+1]
        c=min(a,b)
        # print(gcd(a,b))
        if (gcd(a,b)!=1):
            number_array[i]=c
            number_array[i+1]=c+1
            print(f"{i} {i+1} {c} {c+1}")

        
