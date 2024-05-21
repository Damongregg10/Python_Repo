
# using  def (define) to create a function called "hello"
#when you print using hello(variable) what you put inside the bracket is copied over "to"
#the ="world" will print "world" if nothing is input into "name" and hello() is called

def hello(to="world"):
    print("Hello there, ", to)

hello()
name = input("what is your name? ")
hello(name)