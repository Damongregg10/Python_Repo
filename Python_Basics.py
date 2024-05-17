import random

Animals = ["Koalas", "Tigers", "Dogs", "Platypuses", "Sloths"]
Food = ["Eggs", "Beef", "Sausages", "Bacon", "Chicken"]
Verbs = ["eating", "making"]
Active_Verbs = ["dancing", "running", "fighting", "cooking"]
Emotion = ["love", "enjoy", "prefer"]
Conjunction = ["and", "also they"]
com = ","
#print(type(Animals))
Animals.append ("Elephant")
#print(Animals[1], Verbs[1], Food[3])
print(random.choice(Animals), random.choice(Emotion), random.choice(Verbs), random.choice(Food),com, random.choice(Conjunction), random.choice(Emotion), random.choice(Active_Verbs))