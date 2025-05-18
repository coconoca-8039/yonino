def deco(func):
    def inner(*args, **kwargs):
        #print("#-------------------------------")
        func(*args, **kwargs)  #func → gas
        #print("#-------------------------------")
    return inner

def create(func):
    def inner(*args, **kwargs):
        print("#-------------------------------")
        func(*args, **kwargs)  #func → gas
    return inner

class Car():
    @create
    def __init__(self, model_name, mileage, manufacturer):
        self.model_name = model_name
        self.mileage = mileage
        self.manufacturer = manufacturer
    
    @deco
    def gas(self):
        print(f"{self.manufacturer} : {self.model_name}")
        print("     Accelerator pressed")

    @deco
    def brakes(self):
        print(f"{self.manufacturer} : {self.model_name}")
        print("     Brakes applied")

if __name__ == "__main__":
    prius = Car("Prius", 20, "TOYOTA")
    prius.gas()
    prius.brakes()
    gtr = Car("GTR", 5, "Nissan")
    gtr.gas()
    gtr.brakes()
