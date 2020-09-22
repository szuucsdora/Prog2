import numpy as np

#
# n=np.random.randint(0,100,30)
# setA=set(n)
#
# minv=np.inf
# maxv=-np.inf
#
# for i in setA:
#     if i > maxv:
#         maxv=i
#     if i < minv:
#         minv=i
#
# print(setA)
# print('A minimum érték: {} és a maximum: {}'.format(minv,maxv))

import math

# str='*  '
# N=9
# for i in range(1,N+1):
#     if i<= math.ceil(float(N)/2):
#         print(i*str)
#     else:
#         print((N+1-i)*str)

r=int(input('Adja meg a sorok számát: '))
c=int(input('Adja meg az oszlopok számát: '))

M=np.zeros((r,c))

for i in range(0,r):
    for j in range (0,c):
        M[i,j]=(i+1)*(j+1)

print(M)