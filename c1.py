t= int(input())
test_cases=[]
given_nums=[]
for i in range(t):
    a= list(map(int, input().split()))
    b= int(input(""))
    test_cases.append(a)
    given_nums.append(b)

for i in range(t):
    a= test_cases[i][0]
    b= test_cases[i][1]
    c= given_nums[i]
    d= list(map(int, str(c)))
    e= max(d)
    if d[0]<b :
        d.insert(0,b)
    elif  b<=min(d):
        d.insert(len(d),b)
    else:
        for j in range(1,len(d)):
            if d[j]>b:
                continue
            elif d[j]<b:
                d.insert(j,b)
                break
    string=""
    for digits in d:
        string+=str(digits)
            
    print(int(string))
        