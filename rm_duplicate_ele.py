list=['greeks','for','greeks','for','teksun','tek','Tek']
newlist=[]

length = len(list)
print length
for i in range(0,length-1):
	print i
	for j in range(i+1,length-1):
		print list[i]
		print list[j]
	  	if(list[i]==list[j]):
			newlist.append(list[i])
			break
	print newlist
                    
