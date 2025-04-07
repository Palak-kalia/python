class Demo:
    # a=10
    def __init__(self):
        print("welcome")
    #     ()
    def sum(self,a):
        # a=10
        print(a)
        self.c=a*a
        print(self.c)
class Demo2:
    def add(self):
        print("hello world")
        print("heyy")

class Demo32(Demo,Demo2):
    def add2(self):
        print("how are you")
        "wow"
                                       
obj=Demo32()
obj.sum(10)
obj.add()
obj.add2()


# class test:
#     def __init__(self):
#         self._name=''
#     def getname(self):
#         return self._name
#     def setname(self,name):
#         self._name=name
# obj=test()
# obj.setname("testing")
# name=obj.getname()
# print(name)

# class calculator:
#     def add(self,x,y):
#         return(x+y)
#         # print(x+y)/
#     def sub(self,x,y):
#         return(x-y)
#     def multiple(self,x,y):
#         return(x*y)
#     def div(self,x,y):
#         if(y!=0):
#             return(x/y)
#         else:
#             print("cannot divide with zero")

# obj=calculator()
# result=obj.add(5,6)
# print(result)
# result1=obj.sub(5,6)
# print(result1)
# result2=obj.multiple(5,6)
# print(result2)
# result3=obj.div(5,6)
# #print(result3)

    
    
