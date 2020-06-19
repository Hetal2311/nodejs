sent=raw_input("Enter your sentense")

newsent= sent.split()
for i in newsent:
    count=0
    for j in i:
        count=count +1
    if (count % 2== 0):
        print(i)
  
