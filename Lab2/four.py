'''Given three integers, print the smallest one. (Three integers should be user input)'''

num1=int(input("Enter the num1: "))
num2=int(input("Enter the num2: "))
num3=int(input("Enter the num3: "))

if num1<=num2 and num1<=num3:
    print(f"{num1} is the smallest.")
elif num2<=num3 and num2<=1:
    print(f"{num2} is smallest.")
elif num3<=num2 and num3<=num1:
    print(f"{num3} is smallest")
print(f"The program is over")