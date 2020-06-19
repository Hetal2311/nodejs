str1 = raw_input("Enter your first sentense : ")

str2 = raw_input("Enter your second sentense : ")

l = []
nstr1= str1.split()
nstr2= str2.split()

for i in nstr1:
    if i not in nstr2:
        l.append(i)
for j in nstr2:
    if j not in nstr1 and j not in l:
        l.append(j)
print (l)
