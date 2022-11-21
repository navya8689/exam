def base3(n):
	if(n==0):
		return
	rem=n%3
	n//=3
	if(rem<0):
		n+=1
	base3(n)
	if (rem<0):
		print(rem+(3*-1),end="")
	else:
		print(rem,end="");
n=int(input())
if (n!=0):
	base3(n)
else:
	print("0",end="")
