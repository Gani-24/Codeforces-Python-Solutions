a,b = map(int,input().split())
y=0
if 1<=a<=b<=10:
    while(a<=b):
        a*=3
        b*=2
        y+=1
print(y)