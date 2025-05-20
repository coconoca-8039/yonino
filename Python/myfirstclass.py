class Person:
    num_legs = 2
    count = 0

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Person.count += 1

    def walk(self):  #インスタンスメソッド
        print(f"{self.name} is walking")
    
    def run(self):  #インスタンスメソッド
        print(f"{self.name} is running")


john = Person("John", 28, 'male')
print(Person.count)
taro = Person("Taro", 18, 'male')
print(Person.count)
emma = Person("Emma", 40, 'female')
print(Person.count)

print(john.name)
print(taro.age)
print(emma.gender)
print("")
john.walk()
emma.run()
# print(john.num_legs)
# Person.num_legs = 10
# print(john.num_legs)
# print(emma.num_legs)
# emma.num_legs = 100
# print(john.num_legs)
# print(emma.num_legs)