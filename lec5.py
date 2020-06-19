x={'Name':'Hetal','Age':25,'course':['sci','comp']}
print x
print (len(x))
print (x.get(12))
x['Name']='Teksun'
print x
x.update({'Name':'TLAB','phone_no':'124-2344'})
print x
del x['Name']
print x
age=x.pop('Age')
print x
print age
print x.keys()
print x.values()
print x.items()
for keys,values in x.items():
	print keys,values
x={'food':{'ham':1,'egg':2}}
print x
print x.keys()
print x['food'].keys()
