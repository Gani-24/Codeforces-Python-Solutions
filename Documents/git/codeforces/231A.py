n = int(input())
t=0
for i in range(n):
    a,b,c= map(int,input().split())
    if (a+b+c>1):
        t+=1
print(t)
