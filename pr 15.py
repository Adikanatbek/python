a=17391 
b=546
c=934
d=17
n=a%d
m=b%d
v=c%d
if n<(m or v):
	print (n)
if m<(n or v):
	print (m)
if v<(n or m):
	print (v)