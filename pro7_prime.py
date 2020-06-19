sran=int(input("Enter starting number"))
lran= int(input("Enter last number"))

for i in range(sran,lran):
    for n in range(1,sran):
        if(i%2==1 and i%n!=0):
            ans=i
    print(ans)



