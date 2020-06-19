def add(a,b):
	c=a+b
	return c

result = add(5,6)
print result

def update(lst):
	print (lst)
	lst[0]=98
	print (lst)

x=5
#update(x)
print ("x : %d"%x)

a=10
print (id(a))
a=20
print (id(a))
lst = [12,4,5,6]
print (id(lst))
#lst[1]=14
update(lst)
print (id(lst))
print lst

def sum(a,b):
	total=a+b
	return=

sum(10,20)
print total
