t=int(input())
for i in range(t):
    s=input()
    a=list(s)
    b=["a","b","c","d","e","f","g","h"]
    for i in b:
        if i!=a[0]:
            print(i+a[1])
    for j in range(1,9):
        if int(a[1])!=j:
            print(a[0]+str(j))
