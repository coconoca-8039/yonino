#-----------------------------------------------------
#関数のネスト化 Nested Function
def outer(outer_param):
    outer_param1 = "Kotoha"

    def inner():
        print("This is inner function")
        print(outer_param)
        print(outer_param1)

    inner()

#outer("outer arg")

#-----------------------------------------------------
#カプセル化 Encapsulation
def casino_entrance(age, min_age=21):
    if age <= min_age:
        print("Sorry you are too young")
        return
    
    def inner_casino_entrance():
        print("Welcome to Casino")
    
    return inner_casino_entrance()

#casino_entrance(2)

#-----------------------------------------------------
#クロージャ Clasure 状態をキープした関数を作ることができる
def power(exponent):
    def inner_power(base):
        return base ** exponent
    return inner_power

power_four = power(4)
#print(power_four(2))    #16
power_five = power(5)
#print(power_five(2))    #32

def average():
    nums = []
    def inner_average(num):
        nums.append(num)
        return sum(nums) / len(nums)
    return inner_average

average_nums = average()
# print(average_nums(5))
# print(average_nums(15))
# print(average_nums(2))
# print(average_nums(2))

#-----------------------------------------------------
#デコレーター Decorator
def greeting(func):
    def inner(*args, **kwargs):
        print("Hello")
        func(*args, **kwargs)  #func → say_name
        print("Nice to meet you")
    return inner

@greeting
def say_name(name):
    print(f"I'm {name} !")

@greeting
def say_name_and_origin(name, origin):
    print(f"I'm {name} !")
    print(f"I was born and raised in {origin} !")

# say_name("Sasaki")
# print("")
# say_name_and_origin("Maika", "Nagoya")