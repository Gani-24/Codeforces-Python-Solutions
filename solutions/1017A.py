n=int(input())
a,b,c,d=map(int,input().split())
tm=a+b+c+d
tm_r=1
for i in range(n-1):
 a1,b1,c1,d1=map(int,input().split())
 om=a1+b1+c1+d1
 if(om>tm):
    tm_r+=1
print(tm_r)