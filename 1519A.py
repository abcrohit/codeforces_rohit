t=int(input())
for i in range(t):
    inp=input()
    t=inp.split(" ")
    dis=abs(int(t[0])-int(t[1]))
    m=min(int(t[0]),int(t[1]))
    # print(f"{dis},{m},{t}")
    if (dis/m > int(t[2])):
        print("NO")
    else:
        print("YES")
    