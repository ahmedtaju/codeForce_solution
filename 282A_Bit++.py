n=int(input())
Sum=0
for i in range(n):
    x=input()
    if x=="++x" or x=="x++":
        Sum +=1
    else:
        Sum -=1
print(Sum)