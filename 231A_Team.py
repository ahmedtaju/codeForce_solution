n=int(input())
tries=[]
_sum=0
for i in range(n):
    p,v,t=map(int,input().split())
    tries.append((p,v,t))
    if sum(tries[i])>1:
        _sum +=1
    else:
        continue
print(_sum)

