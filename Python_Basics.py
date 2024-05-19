import random

Animals = ["Koalas", "Tigers", "Dogs", "Platypuses", "Sloths"]
Humans = ["Dave", "Ian", "Frank", "Susan", "Carole"]
Emotion = ["loves", "enjoys", "prefers"]
Verbs = ["eating", "making"]
Food = ["Eggs", "Beef", "Sausages", "Bacon", "Chicken"]
com = ","
Conjunction = ["and", "also they"]
Active_Verbs = ["dancing", "running", "fighting", "cooking"]

#print(type(Animals))
Animals.append ("Elephant")
#print(Animals[1], Verbs[1], Food[3])

print(random.choice(Animals), random.choice(Emotion), random.choice(Verbs), random.choice(Food),com, random.choice(Conjunction), random.choice(Emotion), random.choice(Active_Verbs))
print(random.choice(Humans), random.choice(Emotion), random.choice(Verbs), random.choice(Food),com, random.choice(Conjunction), random.choice(Emotion), random.choice(Active_Verbs))

# I would like to write some code in order to remove the last "s" from the second random.choice(Emotion) so it types "love" instead of "loves", 
# this is what I found on the internet but coul not make it work
# Emotion = [ x[:-1] for x in Emotion ]


#I used chatgpt to produce large lists
import random

people = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack", "Kate", "Liam", "Mia", "Noah", "Olivia", "Piper", "Quinn", "Ryan", "Sophia", "Tyler", "Uma", "Victoria", "William", "Xavier", "Yasmine", "Zoe"]
emotion_verbs = ["admires", "adores", "appreciates", "cherishes", "delights", "enjoys", "loves", "treasures", "values", "worships", "admires", "envies", "covets", "desires", "fancies", "likes", "prefers", "yearns", "aspires", "craves", "lusts", "misses", "needs", "wants", "requires", "seeks", "longs", "hopes"]
t = "to"
activity_verbs = ["play", "run", "walk", "jump", "skip", "dance", "sing", "swim", "cycle", "skate", "ski", "hike", "climb", "surf", "kayak", "paddle", "row", "sail", "dive", "bungee jump", "paraglide", "skydive", "fly", "ride", "drive", "race", "compete", "compete", "compete", "compete", "compete", "compete", "compete", "compete", "compete", "compete", "compete", "compete", "compete", "compete", "compete", "compete", "compete", "compete", "compete", "compete"]
a = "and"

print(random.choice(people), random.choice(emotion_verbs),t, random.choice(activity_verbs),a, random.choice(emotion_verbs),t, random.choice(activity_verbs))


#I researched how to generate random integers as well, and then added them together to make random numbers
random_number1 = random.randint(1, 10000000)
random_number2 = random.randint(1, 10000000)
random_number3 = random.randint(1, 10000000)
Total = random_number1 + random_number2 + random_number3
print(Total)

#Print and sep examples
print("Hello", "world", sep="---", end="!!!")
print(" How are you?")

#CS50 lesson on inputs
name = input("Hello, what's your name? ").strip().title()
print("Nice to meet you, ", end="")
print(name)
age = input("And how old are you? ").strip().title()
print("Okay so you are " + age + " years old")
location = input("And where do you live? ").strip().title()
print("Okay, so you are " + name + " who is " + age + " years old, and lives in " + location)