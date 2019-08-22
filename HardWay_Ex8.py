print("")

formatter = "{} {} {} {}"

# .format is a function, you are applying the format funciton to formatter variable, .format funcion  has four arguments
# which match with the four {} in the formatter variable.
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, 'False', False, 'True'))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
"Try your",
"Ouw text here",
"Maybe a poem",
"Or a song about fear"
))
print("")
