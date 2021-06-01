T = int(input())
for i in range(T):
    f=input()
    palindrome=input()
    m=palindrome.replace("1","")
    a=len(m)
    res = a%4
    if(res == 0):
        print("DRAW")
    elif (res == 3):
        print("ALICE")
    else:
        print("BOB")