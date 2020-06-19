with open("test1.txt","r") as f:
    data=f.readlines()
    for line in data:
        words= line.split()
        print words
        for char in words:
             print char
             if (char.islower() == True):
                 print "true"
                 with open("test2.txt","a+") as f1:
                     f1.write(char.upper())
                     
             else:
                 print "false"
                 with open("test2.txt","a+") as f2:
                     f2.write(char.lower())

