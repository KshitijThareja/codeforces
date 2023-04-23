t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    counter=0
    
    while True:
        res = [*set(a)] 
        if len(res)>=len(a):      
            break
        else:
            a.pop(0)
            counter+=1
    print(counter)
