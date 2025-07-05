from prettytable import PrettyTable as pt

# Reading the text file in from Input_Data folder:
DNA_Sequence = open("Input_Data/rosalind_rna2.txt")
DNA_Sequence = DNA_Sequence.read()

# Using answer from Question 1, number of bases in sequence before transcription
dA = DNA_Sequence.count("A")
dT = DNA_Sequence.count("T")
dG = DNA_Sequence.count("G")
dC = DNA_Sequence.count("C")

# Replacing T bases to U bases:
RNA_Sequence = DNA_Sequence.replace("T", "U")

# Number of bases in new RNA sequence:
rA = RNA_Sequence.count("A")
rU = RNA_Sequence.count("U")
rG = RNA_Sequence.count("G")
rC = RNA_Sequence.count("C")

# printing the number of bases in a table using the pretty table library:
Base_table = pt()
Base_table.field_names = ["Bases", "dA/rA", "dT/rU", "dG/rG", "dC/rC"]
Base_table.add_row(["DNA", dA, dT, dG, dC])
Base_table.add_row(["RNA", rA, rU, rG, rC])

print(Base_table)


# Save the RNA Sequence as a txt file in Output_Data folder:
rosalind_rna_output = open("Output_Data/rosalind_rna_output.txt", "w+")
rosalind_rna_output.write(RNA_Sequence)
rosalind_rna_output.close()

