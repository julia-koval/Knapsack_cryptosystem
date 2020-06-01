######## Merkle–Hellman knapsack cryptosystem ########

##Key generation

#Create a super-growing sequence of elements in a knapsack
import random
from random import randint
a=[1]
r=randint(3,10)
for i in range(1,r):
    a.append(randint(1,20))

for i in range(1,len(a)):
    while a[i]<=sum(a[:i]):
        a[i]=sum(a[:i+1])
         
print('Заданный сверхрастущий рюкзак: ',a)

#Choose number k (k > a1+a2+...+an)
k=randint(sum(a)+1,10000)

#Choose a number c that is coprime with k
lst=[] 
for i in range(2,k):
    if k%i!=0:
        lst.append(i)
        

lst1=[] #coprime numbers - remainder of division = 1
for i in lst:
    i1=i
    k1=k
    while k1>i1 and (k1-i1)>=0:
        k1-=i1
        while k1<i1 and (i1-k1)>=0:
            i1-=k1
    if i1==1 and k1==1:
        lst1.append(i)
    else:
        continue
c=lst1[0]
b=[] #knapsack-trap (b1,b2,...bn)=c(a1,a2,...an)  (mod  k) - public key
for i in range(len(a)):
    b.append((c*a[i])%k)
print('Открытый ключ: ',b)
print('Секретные ключи: c = ',c,', k = ',k)

## Encryption algorithm

open_text=list(input('Введите двоичную последовательность: '))
for i in range(len(open_text)):
    open_text[i]=int(open_text[i])
split=lambda x,r: x if not x else [x[:r]]+[split([] if not -(len(x)-r) else x[-(len(x)-r):],r)][0]
print('Разбивка последовательности на блоки: ',split(open_text,r))

blocks=split(open_text,r)
norm_blocks=[]
for i in range(len(blocks)):
    if len(blocks[i])==r:
        norm_blocks.append(blocks[i])
    else:
        continue

import numpy as np
for i in range(len(norm_blocks)):
    a1=np.array(a)
    b1=np.array(norm_blocks[i])
    norm_blocks[i]=np.sum(a1*b1)
    if ValueError:
        continue
m=norm_blocks

print('Веса: ',m)


## Decryption Algorithm

a_find=[]

for i in range(len(b)):
    a_find.append(int((c**-1*b[i])%k))
print("Исходный (расшифрованный) сверхрастущий рюкзак: ",a_find)
m_new=[]
for i in range(len(m)):
    m_new.append(int(c**-1*m[i]))
print("m' тяжесть вещей в рюкзаке: ",m_new)
import itertools
block_open_text=[]
combo = list(itertools.product([1,0],repeat=len(a_find)))
for i in range(len(m_new)):
    for tuple in combo:
        if sum(np.array(tuple)*np.array(a_find))==m_new[i]:
            block_open_text.append(tuple)
print('Наличие вещей в рюкзаке: ',block_open_text)


