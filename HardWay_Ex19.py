# Here is when function is defined def, name, parenthesis, arguments, parenthesis, colon
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")  # first line function output
    print(f"You have {boxes_of_crackers} boxes of crackers!")  # 2nd line function output
    print("Man that's enough for a party!")  # 3rd line function output
    print("Get a blanket.\n")  # 4th line function output

# Using the function with numbers
print("We can just give the function number directly:")
cheese_and_crackers(20, 30)

# Using the function with variables
print("OR, we can use variables form our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Using the funcions with aritmethic arguments
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Using the function combining previous learned ways.
print("And We can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
