n, f= list(map(int, input().split()))
n_max=0
complete=[]
for j in range(n):
    k, l= list(map(int, input().split()))
    a=min(k,l)
    b=min(2*k,l)
    n_max+=a
    complete.append(b-a)
complete.sort(reverse=True)
for i in range(f):
    n_max+=max(complete[i], 0)
print(n_max)