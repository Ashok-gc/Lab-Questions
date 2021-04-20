''' Check whether the user input number is even or odd and display it to user'''

num = int(input("Enter the number: "))
if num % 2==0:
    print(f" {num} is even")
else:
    print(f"{num} is odd")
print("The program is over.")