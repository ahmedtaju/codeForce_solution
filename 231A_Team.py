n=int(input())
tries=[]
Sum=0
for i in range(n):
    p,v,t=map(int,input().split())
    tries.append((p,v,t))
    if sum(tries[i])>1:
        Sum +=1
    else:
        continue
print(Sum)

