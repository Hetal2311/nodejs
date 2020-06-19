#dictionary

d={}
print len(d)
#d[Name]='hetal'
print d
d=dict(name='',age='')
print d
d['name']='hetal'
print d
d.update(course='sce',phn='54545454',email='jfhjfj@fj.com')
print d


keys=['a','b','c']
values=[1,2,3]
newd=dict(zip(keys,values))
print newd

ewd=dict.fromkeys(['a','b'])
#print ewd

#print ewd.get('a',non)

print cmp(d,newd)
print str(d)
print type(d)

print d.copy()
d.update(newd)
print d
print newd
