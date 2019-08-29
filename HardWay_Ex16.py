from sys import argv # Import the module argv

script, filename = argv # unpack the given arguments (2) into script & filename variable

print(f"We're going to erase {filename}.")
print("if you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open (filename, 'w')

print("Truncating the file. Goodbye!")
# target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the files.")

target.write(f"{line1}\n{line2}\n{line3}\n")
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("And finally, we close it.")
target.close()

print("Wait a minute!, I forgot to ask, Do you want to review it? ")
response = input(">> ")
if response == 'si':
    archivo_again = open(filename)
    print(f"here's your file {filename}.")
    print(archivo_again.read())
    print("Listo, deja de molestar")
archivo_again.close()
