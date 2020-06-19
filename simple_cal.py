# simple calculator for addition subtraction,Division,Multiplication


def add(no1,no2):
	return no1+no2

def sub(no1,no2):
	return no1-no2

def multi(no1,no2):
	return no1*no2

def division(no1,no2):
	return no1/no2

print("Please Select Operation- \n"\
	"1. Add\n"\
	"2. Sub\n"\
	"3. Multiply\n"\
	"4. Divide\n")
select=input("Select operations form 1,2,3,4:")
no1=int(input("Enter First number:"))
no2=int(input("Enter Second number:"))

if select=='1':
	print(no1,"+",no2,"=",add(no1,no2))
elif select=='2':
	print(no1,"-",no2,"=",sub(no1,no2))
elif select=='3':
	print(no1,"*",no2,"=",multi(no1,no2))
elif select=='4':
	print(no1,"/",no2,"=",division(no1,no2))
else:
	print("invalid input")
