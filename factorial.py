"""i=5
while i>=1:
	i*=i
	print i
print i
"""

def factorial(i):
	 if(i==1 or i==0):
		return 1
	 else:
	  return  i*factorial(i-1)
ans=5
print(factorial(ans))
