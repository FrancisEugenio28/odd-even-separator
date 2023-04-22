#Francis Niño A. Eugenio
#BSCPE 1-5 | Object Oriented Programing
#Even & Odd Separator

#Write a Python program that reads a text file named numbers.txt that contains 20 integers. The program will create two other 
#text file; the first text file will be named even.txt that will contains all even numbers extracted from the numbers.txt. 
#The second text file will be named odd.txt that will contains all odd numbers extracted from the numbers.txt.

# create empty list for even and odd
even = []
odd = []
# read input file
with open("numbers.txt", "r") as input_file, open("even.txt", "a") as even_file, open("odd.txt", "a") as odd_file: 
    # for each line
    for line in (input_file):
        # remove all the \n 
        input_line = line.strip()
        # separate the even from the list
        if (int(line) % 2 == 0):
            even.append(input_line)
        # else, store the odd from the list
        else:
            odd.append(input_line)
    # write it in the txt file
    even_file.write(','.join(even))
    odd_file.write(','.join(odd))