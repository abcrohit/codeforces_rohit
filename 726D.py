def alldivisors(n):
    array=[0]*(n//2)
    current=0
    for j in range(0,n//2-1):
        i=n//2-j
        if n%i==0:
            array[current]=i
            current+=1
    return array[0:current]
def find_winner(n,DParray):
    if DParray[n]!=0:
        return DParray[n]
    else:
        for i in alldivisors(n):
            if(find_winner(n-i,DParray)==2):
                DParray[n]=1
                return 1
        DParray[n]=2
        return 2
for iters in range(int(input())):
    n=int(input())
    DParray=[0]*(n+1)
    DParray[1]=2
    if(find_winner(n,DParray)==1):
        print("Alice")
    else:
        print("Bob")