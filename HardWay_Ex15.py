from sys import argv # Import the module argv

script, filename = argv # unpack the given arguments (2) into script & filename variable

txt = open(filename) # open the file with name equal to filename string & then store it txt variable THIS IS A FILE OBJECCT

print(f"Here's your file {filename}:") # Print a message and the filename string
print(txt.read()) # print the content of the FILE OBJECT (txt variable), calling the funcion read for 'txt' variable
txt.close()
# print("Type the filename again:") # print a message asking to open the file txt_again
# file_again = input ("> ") # Waiting user responce, computer store customer typing in 'file_again' through input command.

# txt_again = open(file_again) # open the file which name is stored in file_again and holds it in txt_again.

# print(txt_again.read()) # print what is read in variable txt_again
print(" ")
