
'''
Counting Point Mutations:

Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t)
'''


Input_file = open("Input_Data/rosalind_hamm.txt")
Input_file = Input_file.read().splitlines()

hamm = 0
same = 0

string1 = Input_file[0]
string2 = Input_file[1]

for i in range(len(Input_file[0])):
    if string1[i]==string2[i]:
        same +=1
    else:
        hamm += 1

print(hamm)

Output_file = open("Output_Data/rosalind_HAMM_output.txt", "w+")
Output_file.write(str(hamm))
Output_file.close()

