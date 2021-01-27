a_set = set()
i = 0
while i<=10:
	num=int(input("Enter Number: "))
	a_set.add(num)
	i += 1
	a_typ = tuple(a_set)	
print(a_typ)