n, f= list(map(int, input().split()))
n_max=0
k_sep=[]
l_sep=[]
for j in range(n):
    k, l= list(map(int, input().split()))
    k_sep.append(k)
    l_sep.append(l)
k_sort= k_sep.sort()
k_double=[]
for i in range(n):
    if f==0:
        break
    if k_sep[i]==0:
        continue
    if k_sep[i]>=l_sep[i]:
        z=k_sep[i]
        for i in range(n):
            if z== 
        f-=1
        n_max+=k
