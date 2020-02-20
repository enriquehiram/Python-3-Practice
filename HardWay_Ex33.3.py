# from sys import argv
# script, k = argv


def contador(k,incr):
    i= 0
    numbers = []
    while i < k:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + incr
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print(" The numbers: ")

    for num in numbers:
        print(num)
