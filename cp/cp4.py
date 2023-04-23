n, f= list(map(int, input().split()))
n_max=0
complete=[]
complete_1=[]
final=[]
for j in range(n):
    k, l= list(map(int, input().split()))
    complete.append([k,l])
    complete_1.append([2*k,l])

for i in range(n):
    a=min(complete[i])
    b=min(complete_1[i])
    n_max+=a
    final.append(b-a)
final.sort(reverse=True)

for h in range(f):
    n_max+=final[h]
print(n_max)
