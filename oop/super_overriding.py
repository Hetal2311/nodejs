class A(object):
    def function1(self):
        print 'function of class A'

class B(A):
    def function1(self):
        print 'function of class B'
        super(B,self).function1()

class c(B):
    def function1(self):
        print 'function of class C'
        super(c,self).function1()

j=c()
j.function1()
