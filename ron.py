#関数のネスト化 Nested Function
def outer(outer_param):
    outer_param1 = "Kotoha"

    def inner():
        print("This is inner function")
        print(outer_param)
        print(outer_param1)

    inner()

#outer("outer arg")

#カプセル化 Encapsulation
def casino_entrance(age, min_age=21):
    if age <= min_age:
        print(f"{min_age} Sorry you are too young")
        return
    
    def inner_casino_entrance():
        print("Welcome to Casino")
    
    inner_casino_entrance()

casino_entrance(2)