lst=['abc',4,'4d']
print(lst)
length=len(lst)
swap=lst[0]
lst[0]=lst[length-1]
lst[length-1]=swap
print(lst)
