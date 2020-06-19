pri_ammount= float(input("Enter principal amount"))
rate= float(input("Enter rate"))
time= int(input("Enter time"))

coum_interest =pri_ammount*((1+rate/100)**time)

print("compound interest:",coum_interest)
