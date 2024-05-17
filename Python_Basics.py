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
