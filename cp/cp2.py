n, m, a= list(map(int, input().split()))
area_s= n*m
area_f= a*a
n_s= n//a
m_s= m//a
if n%a!=0:
    n_s+=1
if m%a!=0:
    m_s+=1
print(n_s*m_s)


