def is_pattern(s):
    n=len(s)
    m=n//2
    if(n==0 or n==1):
        return True
    if(s[0:m]==s[-m:]):
        return is_pattern(s[0:m])
    else:
        return False
for iters in range(int(input())):
    if(is_pattern(input())==True):
        print("YES")
    else:
        print("NO")