s=input()
t=input()
v=["a","e","i","o","u"]
if len(s)==len(t):
    for i in range(len(s)):
        if s[i] not in v and t[i] in v:
            print("NO")

        elif s[i] in v and t[i] not in v:
            print("NO")
    else:
          print("yes")

else:
    print("NO")