jesika={'ass':45, 'lab':56, 'test':67}
jay={'ass':67,'lab':98,'test':90}
yami={'ass':98,'lab':87,'test':67}

def avg_ass(d):
    marks= float((d['ass']*10)/100)
    return marks
def avg_lab(d):
    marks=float((d['lab']*20)/100)
    return marks
def avg_test(d):
    marks=float((d['test']*70)/100)
    return marks
def avg(a,b,c):
     avg=(a+b+c)
     if (avg >= 90):
         print "A"
     elif (avg >= 80):
         print "B"
     elif (avg >= 70):
         print "c"
     elif(avg >=60):
         print "D"
     else:
         print "Fail"
marks_ass=avg_ass(jesika)
marks_lab=avg_lab(jesika)
marks_test= avg_test(jesika)
print jesika
average =avg(marks_ass,marks_lab,marks_test)
print("______________________________________")
marks_ass=avg_ass(jay)
marks_lab=avg_lab(jay)
marks_test=avg_test(jay)
print (jay)
average=avg(marks_ass,marks_lab,marks_test)
#print ("%s 's average marks are %d",jesika,average)


