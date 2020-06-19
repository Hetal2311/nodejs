str1= raw_input("Enter your string")

splchar= set("!@#$%^&*(){}|:<>?[]\;',./-=`~'")
count =0
for i in str1:
    if i in splchar:
        count = count +1
if count >= 1:
    print("string contain  spl character")
else:
    print("string is accepted")

