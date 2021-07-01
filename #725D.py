iter=int(input())
for iters in range(iter):
    length=int(input())
    stones_array=[int(i) for i in input().split(" ")]
    min_index=stones_array.index(min(stones_array))
    max_index=stones_array.index(max(stones_array))
    a=min(min_index,max_index)
    b=max(min_index,max_index)
    d=max(a-0,b-a-1,length-b-1)
    print(length-d)
    