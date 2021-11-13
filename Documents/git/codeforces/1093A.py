x=int(input())
for i in range(x):
    y=int(input())
    if y>=2 and y<=7:
        print(1)
    elif y%7==0:
        print(y//7)
    else:
        print(y//7+1)