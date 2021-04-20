''' For given integer x, print ‘True’ if it is positive, print ‘False’ if it is negative and print ‘zero’
if it is 0 '''


print("Process one: If, else, elif")
num=float(input("Enter the number: "))
if num >0:
    print(f"The given number {num} is true ")
elif num == 0:
    print(f"The given number {num} is Zero")
else:
    print(f"The given number {num} is False")

print("Process one is over, now we will go with method 2")

print(" Process two: Nested if")
number=float(input("Enter the number: "))

if number >= 0:
   if num == 0:
       print(f"The given {number} is Zero")
   else:
       print(f"The given number {number} is true")
else:
   print(f"The given number {number} is false ")

print("The program is over")