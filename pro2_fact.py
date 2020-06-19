no1=int(input("Enter number"))


def factorial(no1):
    fact_no=1
    for no2 in range(1,no1):
        fact_no = fact_no * (no2+1)
    print(fact_no)

factorial(no1)
