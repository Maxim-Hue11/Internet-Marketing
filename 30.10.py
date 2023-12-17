#Задача N

#def decomp(n): # функция разложения числа на простые множители
#    ans = []
#    d = 2
#    while d * d <= n:
#        if n % d == 0:
#            ans.append(d)
#            n //= d
#        else:
#            d += 1
#    if n > 1:
#        ans.append(n)
#    return ans
# 
#def cnt_same(A):
#    B = []
#    cnt = 1
#    Ap=A[0]
#    for i in range(1,len(A)):
#        if A[i] == Ap:
#            cnt+=1
#        else:
#            B.append(cnt)
#            cnt=1
#            Ap = A[i]
#    B.append(cnt)
#    return B
 
#n = int(input())
#A = cnt_same(decomp(n))
#x = 1
#for p in A:
#    x *= 2*p+1
#x = (x-1)//2
#print(x)








#Задача O

#def get_sum(n):
#    s=0
#    for i in range(1,n):
#        if n%i==0:
#            s+=i
#    return s
#def gen_friendlys(n):
#    res=[]
#    for i in range(1,n):
#        if i not in res:
#            tmp=get_sum(i)
#            if i==get_sum(tmp) and i!=tmp:
#                res.append(i)
#                res.append(tmp)
#    return res
#print(sum(gen_friendlys(10000)))