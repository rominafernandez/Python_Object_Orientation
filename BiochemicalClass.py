## Group Exercise 1 - A biochemical class

# Create a bigger biochemical or biological class with
# At least 10 different attributes
# At least three have to be handed over to the constructor
import re

class Primer():
    def __init__(self, sequence, length, direction, melting_temp = 0, annealing_temp = 0):

        # Allows only ACTG as characters for sequence
        if re.search("^[A,C,T,G]+$", sequence):
            self.__sequence = sequence
        else:
            print("Invalid sequence input")
            self.__sequence = ""

        # length of Primer in bases (int) Calculate from sequence!
        if isinstance(length, int):
            self.__length = int(length)
        else:
            print("Primer length must be integer")
            self.__length = 0

        # possible directions: rev, fwd
        if direction == "rev" or direction == "fwd":
            self.__direction = direction
        else:
            print("Primer direction must be fwd or rev")
            self.__direction = ""

        # melting temperatur of protein. Default is 0
        if isinstance(melting_temp, int) and melting_temp > 0:
            self.melting_temp = melting_temp
        elif (melting_temp == 0):
            pass
        else:
            print("Melting temperature must be integer and bigger than zero")

        # annealing temperature is either -3°C lower than denaturing temperature or 0
        if isinstance(annealing_temp, int) and annealing_temp > 0:
            self.annealing_temp = annealing_temp
        elif annealing_temp = 0 and melting_temp >=3:
            self.annealing_temp = self.melting_temp -3
        elif annealing_temp = 0 and melting_temp < 3:
            pass
        else:
            print("Annealing temperature must be integer and bigger than zero")

        self.temp_unit = "Celsius"
        self.organism = "Homo sapiens"
        self.target_gene = "GeneName"
        self.target_region = "Exon"



test = Primer("ATGG",direction = "rev", length = 5)
print(test.sequence)
# Generate at least 15 different member methods for your class, that allow you
# To modify the data in the object
# Work with the data
# Give back some information of your object

'''
set Sequences
get sequence
'''
