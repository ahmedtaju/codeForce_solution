test_cases = int(input())
for i in range(test_cases):
    n=int(input())
    s=input()
    if s==s[::-1]:
        print("YES")
    else:
        print("NO")
