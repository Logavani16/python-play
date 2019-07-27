r1,r2=map(str,input().split())
if(len(r1)!=len(r2)):
    print("no")
else :
    s1=[r1.count(j) for j in r1]
    s2=[r2.count(j) for j in r2]
if(s1==s2):
    print("yes")
else:
    print("no")
