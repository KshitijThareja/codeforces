t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    
    if i in a and i==a[0] or i==a[n]:
        print("YES")
    
