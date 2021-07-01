for iters in range(int(input())):
    n=int(input())
    m=n//2
    if(n%2==0):
        output="2 1"
        for m in range(2,m+1):
            output+=f" {2*m} {2*m-1}"
    else:
        output="3 1 2"
        for m in range(2,m+1):
            output+=f" {2*m+1} {2*m}"
    print(output)
