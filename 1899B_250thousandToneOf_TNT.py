t=int(input())
for i in range(t):
    arr=[]
    n=int(input())
    a=input().split()
    for j in range(n):
        arr.append(int(a[j]))
    print(max(arr)-min(arr))