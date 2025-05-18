class Myclass():

    classmethod_count = 0

    def __init__(self):
        pass

    def mymethod(self):
        print("This is normal method")

    @staticmethod
    def mystaticmethod():
        print("This is staticmethod")
    
    @classmethod
    def myclassmethod(cls):
        cls.classmethod_count += 1
        print(f"This is my classmethod and now the count is {cls.classmethod_count}")

c = Myclass()
c.mymethod()
Myclass.mystaticmethod()
Myclass.myclassmethod()
c.myclassmethod()