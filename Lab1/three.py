'''N students take K apples and distribute them among each other evenly. The remaining (the
undivisible) part remains in the basket. How many apples will each single student get? How many
apples will remain in the basket? The program reads the numbers N and K. It should print the two
answers for the questions above.'''

N = int(input("Enter the number of students in class: "))
K = int(input("Enter the number of apples: "))

apples_get = (K//N)

remaining_apples = (K%N)
print(f"Each student got {apples_get}")
print(f"The remaining apples are {remaining_apples}")

