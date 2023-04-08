n=int(input())
a=list(map(int, input().split()))
b=[]
for i in range(1, n+1):
    c=a.index(i) +1
    b.append(c)
# str1 = ""
 
# for ele in b:
#     str1 += str(ele)
# print(str1)
print(*b)