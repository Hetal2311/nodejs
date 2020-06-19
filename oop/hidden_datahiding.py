class Myclass:

    __hiddenVariable=0

    def add(self,increment):
        self.__hiddenVariable +=increment
        print(self.__hiddenVariable)

obj1=Myclass()
obj1.add(2)
obj1.add(5)
print(obj1._Myclass__hiddenVariable)
print(obj1.__hiddenVariable)
