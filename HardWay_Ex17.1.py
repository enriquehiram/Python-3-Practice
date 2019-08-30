from sys import argv # Import the module argv
from os.path import exists

script, from_file, to_file = argv # unpack the given arguments (3) into script & filename variable

indata = open(from_file).read()
print(f"\nCopying from {from_file} to file {to_file}.\nThe input file is {len(indata)} bytes long\nOutput file exist? {exists(to_file)}")

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")
out_file.close()
