t=int(input())
for i in range(t):
    N = input()
    M=input()
    T=0
    J=0
    ANS=0
    for i in M:
        if i=="*":
            T+=1
    for i in M:
        if i=="*":
            J+=1
        else:
            ANS+=min(J,T-J)
    print(ANS)





