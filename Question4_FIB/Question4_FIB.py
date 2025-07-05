"""
Name: Pradeep Kumar
Date: 11/24/2019

Question: Wascally Wabbits

.....
When finding the n-th term of a sequence defined by a recurrence relation, we can simply use the recurrence relation to
 generate terms for progressively larger values of n. This problem introduces us to the computational technique of
 dynamic programming, which successively builds up solutions by using the answers to smaller cases.

Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each
generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
"""

from prettytable import PrettyTable as pt

# Conditions:

conditions = open("Input_Data/rosalind_fib.txt")
conditions = conditions.read()

n = int(conditions.split()[0])       # No. of Years
k = int(conditions.split()[1])       # No. of babies each rabbit pair can have per year.

"""
The trick over here is to read the additional info in the "click to Expand" under the heading on the rosalind page. It gives you the
conditions for solving the problem. 

The conditions are: 
1) The population begins in the first month with a pair of newborn rabbits.
2) Rabbits reach reproductive age after one month.
3) In any given month, every rabbit of reproductive age mates with another rabbit of reproductive age.
4) Exactly one month after two rabbits mate, they produce one male and one female rabbit.
5) Rabbits never die or stop reproducing.

"""

# In the first year, we start with one pair of young rabbits.

Young_Rabbit = 1
Adult_Rabbit = 0
One_month_rabbit = 0

# Lets make a pretty table to see how the code is performing:
Fibonacci_table = pt()
Fibonacci_table.field_names = ["Year", "i", "Young Rabbit", "One month old rabbit", "Adult Rabbit", "Total Rabbit"]
Fibonacci_table.add_row([1, "-",Young_Rabbit,One_month_rabbit,Adult_Rabbit,Young_Rabbit+One_month_rabbit+Adult_Rabbit])

# Here the for loop starts from 2 (represented by n = 1) and ends at i = 4 (represented by n = 5)

for i in range(1, n):
    New_one_month = Young_Rabbit
    Young_Rabbit = 0
    Total_Adult_rabbit = One_month_rabbit + Adult_Rabbit
    Young_Rabbit = Total_Adult_rabbit * k
    Adult_Rabbit = Total_Adult_rabbit
    One_month_rabbit = New_one_month
    Rabbits = Young_Rabbit + One_month_rabbit + Adult_Rabbit

    Fibonacci_table.add_row([i+1,
                             i,
                             Young_Rabbit,
                             One_month_rabbit,
                             Adult_Rabbit,
                             Rabbits])

print(Fibonacci_table)

# Lets write the final total rabbit count into a txt file to submit.

file_save = open("Output_Data/rosalind_fib_output.txt", "w+")
file_save.write(str(Rabbits))
file_save.close()
