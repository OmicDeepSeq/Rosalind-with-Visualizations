"""
Name: Pradeep Kumar
Date: 11/21/2019

Question:
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s,
then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement sc of s.
Sample Dataset AAAACCCGGT
Sample Output ACCGGGTTTT
"""
from prettytable import PrettyTable as pt

# reading in the Input data from Input_Data Folder:
Forward_strand = open("Input_Data/rosalind_revc2.txt")
Forward_strand = Forward_strand.read()

# Now lets declare a function that will process any strand into its reverse complement:
def rev_comp_strand(Seq):
    Sam_Dataset = Seq                   # Sam_Dataset takes in the entering strand data
    Sam_Output = ""                     # Sam_Ouput is initiated to build the reverse strand from the input strand in the for loop
    for i in Sam_Dataset:
        if i == "A":
            Sam_Output += "T"           # if the for loop sees an A, it inputs a T to the Sam_Output variable
        if i == "T":
            Sam_Output += "A"           # same goes for T  and so on.....
        if i == "G":
            Sam_Output += "C"
        if i == "C":
            Sam_Output += "G"

    return Sam_Output[::-1]             # this code flips the string in reverse. Thereby ending with a Reverse Complement of the input strand


# Now lets use the function RevCompStrand for the input data Forward_strand:
Reverse_complement_strand = rev_comp_strand(Forward_strand)

file_save = open("Output_Data/rosalind_revc_output.txt", "w+")
file_save.write(Reverse_complement_strand)
file_save.close()

# we can also check the number of bases in both the forward and the reverse complement strand to see if everything got procesed right:

# printing the number of bases in a table using the pretty table library:
# we are processing the count code in the table code itself:
Base_table = pt()
Base_table.field_names = ["Bases", "dA/rcA", "dT/rcT", "dG/rcG", "dC/rcC"]
Base_table.add_row(["Forward Strand",
                    Forward_strand.count("A"),
                    Forward_strand.count("T"),
                    Forward_strand.count("G"),
                    Forward_strand.count("C")])
Base_table.add_row(["Reverse Complement Strand",
                    Reverse_complement_strand.count("A"),
                    Reverse_complement_strand.count("T"),
                    Reverse_complement_strand.count("G"),
                    Reverse_complement_strand.count("C")])

print(Base_table)

# in the printed out table, the data is interchanged between A and T, and G and C since they are reverse complement.
