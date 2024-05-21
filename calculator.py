"""
This is the first calc with int forcing the input to be recognised as an integer

x = int(input("Please enter the first number "))
y = int(input("Please enter the second number "))

print("The answer is: ", x + y)



x = float(input("Please enter the first number "))
y = float(input("Please enter the second number "))

z = round(x + y)

#by adding the f (formatting) and {} to Z, this tells the program that this is a formatted string,
#additionally adding ":," after Z tells the program to use , to seperate numbers
print(f"{z:,}")



x = float(input("Please enter the first number "))
y = float(input("Please enter the second number "))

#by adding a , 2 after the arguement x / y, it will round the result by 2 decimal places
z = round(x / y, 2)

print(z)

"""
#In this program we define a function called "Main" we then define a variable called "x" and convert the users input
#into an integer, and then print the result with the "square" function which we define afterwards.
#we define square(n) and inside the function we return n * n, other words square * square (x)
#so in "def Main" it knows to multiply the users input (x) by itself
def main():
    x = int(input("What is x? "))
    print("X squared is ", square(x))

def square(n):
    return n * n

main()
