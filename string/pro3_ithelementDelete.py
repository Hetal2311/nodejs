ch = raw_input("Enter your string")
nth_ele = int(input("Enter your nth elemnet number that you want to delete from string:"))

#print (nth_ele)

nch=''
count=0
for i in ch:
         count = count +1
        
         if count == nth_ele:
             nch =nch
         else:
             nch=nch + i
print("New word:",nch)
             
    
