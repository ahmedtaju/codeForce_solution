n,k=map(int,input().split())
a=input().split()
Sum=0
for i in range(n):
    if int(a[i])==0 and int(a[k-1])==0:
        break
    elif int(a[k-1])<=int(a[i]):
        Sum +=1
print(Sum)
