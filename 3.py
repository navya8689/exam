n=int(input())
v_list=['0','1','2','5','6','8','9']
l=[]
num=1
y=1
while(y<=n):
    z=str(num)
    count=0
    for i in z:
        if(i in v_list):
            count+=1
    if(count==len(z)):
        l.append(z)
        y+=1
    num+=1
op=int(l[n-1])
print(op) 
