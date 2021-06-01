T=int(input())
def sorted(array):
    for i in range(len(array)-1):
        if array[i]>array[i+1]:
            return False
        return True
for i in range(T):
    L=int(input())
    array=input()
    array1= [int(x) for x in input().split(" ")]
    # print(array1)
    min=array1.index(min(array1))
    max=array1.index(max(array1))
    n=len(array1)
    if(sorted(array1)):
        print("0")
    # elif()
    elif(min==0 or max==n-1):
        print("1")
    elif(min==n-1 and max==0):
        print("3")
    else:
        print("2")

