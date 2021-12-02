l,h=int(input()),int(input())
s1=l-1
s2=1
for i in range(l,l+1):
    print(" "*s1+'*",end='')
    if(i==h):
          print("*"*s2,end='')
    else:
        print(" "*s2,s2,end='')
    s1-=1
    if(i>1):
        s2+=2
        print("*")
    else:
        print()
