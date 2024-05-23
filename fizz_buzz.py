# If the user types in a number that is divisible by 3 then output fizz
# If the user types in a number that is divisible by 5 then output buzz
# If the user types in a number that is dibisible by 3 and 5 then output fizz_buzz
# both the input and the output will be handled by a function

def function1(number):
    if number % 3 == 0 and number % 5 == 0:
        return "fizz_buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    


# While True then ask the user to input the first number
# Until False then ask the user to make sure they input the number in base10 instead of a string

while True:
    user_input = input("Please enter a number ")
    try:
        print(function1(int(user_input)))
    except:
        print("Please make sure you type the number using base10 ")