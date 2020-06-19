first=0
second=1
n=input("ENTER NUMBER OF TERMS")
for c in range(0,n):
	if(c <= 1):
		next=c
	else:
		next=first+second
		first=second
		second=next
	print next

