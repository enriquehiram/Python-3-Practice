types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." # String inside string x2

print(x)
print(y)

print(f"I said: {x}") # String inside a string
print(f"I also said: '{y}'") # String inside a string

hilarious = False

joke_evaluation = "Isn't that joke so funny?! {}"
# con el .format puedes llenar con cualquier {} variable embebida, solo aguas con el formato
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
