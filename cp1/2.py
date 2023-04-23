t=int(input())
for i in range(t):
    n=int(input())
    counter=0
    while True:
        if n==1:
            print(counter)
            break
        elif n%6==0:
            n=n/6
            counter+=1
        elif (n%3==0 and n%2!=0):
            n=(n*2)/6
            counter+=2
        else:
            print(-1)
            break
