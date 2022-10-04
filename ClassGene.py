## Exercise 1 - Class Gene

# Generate your own class called “Gene” that has the following five attributes:
# __Name: a string (private)
# __Nr_Nucleotide: a positive whole number (private)
# __Nr_ReadingFrame: a positive whole number (private)
# _Nucleotide: a positive whole number (protected)
# _ReadingFrame: a positive whole number (protected)
# __Nr_Nucleotid and __Nr_ReadingFrame are the maximum number and _Nucleotide and _ReadingFrame are the positions
# All attributes should be given to the constructor of the class if a new object is generated

class Gene():
    def __init__(self, name, nr_nucleotide, nr_reading_frame, nucleotide, reading_frame):
        self.__name = name
        self.__nr_nucleotide = nr_nucleotide
        self.__nr_reading_frame = nr_reading_frame
        self._nucleotide = nucleotide
        self._reading_frame = reading_frame


## Exercise 2 - Glass gene 2

# Expand the class from the first exercise by adding several methods to it.
# One getter() for each attribute defined in the class
# The methods up_nucleotide(), down_nucleotide(), up_readingframe() and down_readingframe()
# that allow the user to change the nucleotide and readingframe accordingly but only if possible
# A method print_state() that prints out the name of the Gene the used Nucleotide and the used ReadingFrame.

    def get_name(self):
        return self.__name

    def get_nr_nucleotide(self):
        return self.__nr_nucleotide

    def get_nr_reading_frame(self):
        return self.__nr_reading_frame

    def get_nucleotide(self):
        return self._nucleotide

    def get_reading_frame(self):
        return self._reading_frame

    def up_nucleotide(self, value):
        if value >= 0:
            self._nucleotide += value
        else:
            print("Error: Invalid Input")

    def down_nucleotide(self, value):
        if value >= 0:
            if value <= self._nucleotide:
                self._nucleotide -= value
            else:
                print("Error: Value schould be >= 0")
        else:
            print("Error: Invalid Input")

    def up_reading_frame(self, value):
        if value >= 0:
            self._reading_frame += value
        else:
            print("Error: Invalid Input")

    def down_reading_frame(self, value):
        if value >= 0:
            if value <= self._reading_frame:
                self._reading_frame -= value
            else:
                print("Error: Value schould be >= 0")
        else:
            print("Error: Invalid Input")

    def print_status(self):
        print(f"Gene name: {self.get_name()}")
        print(f"Nucleotide: {self.get_nucleotide()}")
        print(f"Reading frame: {self.get_reading_frame()}")


## Exercise 21 - Class Gene 3

# Add a String-method to your class, so that the contents of
# your objects can be printed out in a good manor

    def __str__(self):
        name = f"\n{'':<5}name = {self.__name}"
        max_nucleotide = f"\n{'':<5}nr_nucleotide = {self.__nr_nucleotide}"
        max_reading_frame = f"\n{'':<5}nr_reading_frame = {self.__nr_reading_frame}"
        nucleotide = f"\n{'':<5}nucleotide = {self._nucleotide}"
        reading_frame = f"\n{'':<5}reading_frame = {self._reading_frame}"

        return f"Gene({name}, {max_nucleotide}, {max_reading_frame}, {nucleotide}, {reading_frame}\n)"

test = Gene("hi", 1, 2, 3, 4)
print(test.__str__())
