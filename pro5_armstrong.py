
no1=int(input("Enter number"))
no2= no1
number =0
while ( no1 >= 1):
    number= (number + pow((no1%10),3))
    no1=no1/10
if (number == no2):
    print "Armstrong number"
else:
    print "No armstrong number"
    
