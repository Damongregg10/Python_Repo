import random

Animals = ["Koala", "Tiger", "Dog", "Platypus", "Sloth"]
Food = ["Eggs", "Beef", "Protien Powder", "Bacon", "Chicken"]
Verbs = ["Eats", "Makes"]
#print(type(Animals))
Animals.append ("Elephant")
#print(Animals[1], Verbs[1], Food[3])
print(random.choice(Animals), random.choice(Verbs), random.choice(Food))