my_name = 'Enrique De la Cruz'
my_age = 35 # not a lie
my_height = 69.5 # inches
my_weight = 180 # lbs
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'

height = my_height * 2.54
weight = my_weight * 0.453592

# This is valuable: if you need to add a variable into a string then you need to add a f (inside parenthesis after print) and refer to the variable inside the qoutes marks involved in {}
# f indicates python that those text need to be format first
print(f"Let's talk about {my_name}.")
print(f"He's {height} centimeters tall.")
print(f"he's {round(weight)} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the food.")

# This line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height} and {my_weight} I get {total}.")
