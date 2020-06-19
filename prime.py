no= input("Enter any number")

if no>1:
	for i in range(2,no//2):
		if(no% i)==0 :
			print("not prime")
			break
  		else:
			print("Prime number")
			break
else:
	print("Enter proper number")
