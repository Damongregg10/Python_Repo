import random

#I installed Python Imagery Library (Pillow)

from PIL import Image 
image_paths = ["funny_cat1.jpg", "funny_cat2.jpg", "funny_cat3.jpg"]

random_number1 = random.randint(0, 1)
random_number2 = random.randint(0, 1)
random_number3 = random.randint(0, 1)

total = random_number1 + random_number2 + random_number3

#The code below is from chatgpt

# Use the total to select an image from the list
image_index = total % len(image_paths)  # Use modulo operator to ensure index stays within bounds
selected_image_path = image_paths[image_index]

# Open and display the selected image
selected_image = Image.open(selected_image_path)
selected_image.show()