s=input()
s1=input()
c=0
res=s1[::-1]
l=res[0]
for i in s:
    if(i==l):
        c+=1
print(c)
