
lst=['sdd','34',34,67,8,'def','/0']
print(lst)
pos1=int(input("Enter first element positions between 1 to 7 elements"))
pos2= int(input("Enter second element position between 1 to 7"))
lst[pos1-1],lst[pos2-1]=lst[pos2-1],lst[pos1-1]
print (lst)
