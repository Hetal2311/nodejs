str1=raw_input("enter your string")
str2= str1.split()
word_length= int(input("Enter max number of characters in word"))

for i in str2:
        if (len(i) > word_length):
            print (i)
        

