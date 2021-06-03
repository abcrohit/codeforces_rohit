T=int(input())
def twentyFifty(n):
    if (n%2050==0):
        return sumOfDigits(n/2050)
    else :
        return -1
def sumOfDigits(F):
    s=0
    while(F!=0):
        # print(F%10)
        s=s+(F%10)
        F=F//10
    return int(s)
# print(sumOfDigits(50)
for i in range(T):
    # print(twentyFifty())
    print(twentyFifty(int(input())))
