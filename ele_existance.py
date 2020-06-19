
list=[5,6,72,4,7,4,67,334]
length =len(list)
print list
ele=int(input("Enter any element to check existance"))
i=0
for i in range(i,length):
	if(list[i]==ele):
		print("element exist in list")
        break	
	else:
		print("There are no such element in list")
	break
