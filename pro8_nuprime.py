no1=int(input("Enter number to show number is prime or not"))
flag=0
print(isprime(11))
for i in range (2,no1):
    if(i%no1!=0):
        flag=1
if (flag==1):
    print("not Prime number")
else:
    print(" Prime Number")
