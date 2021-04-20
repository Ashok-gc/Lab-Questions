# WAP which accepts marks of four subjects and display total marks, percentage and grade.
# Hint: more than 70% -> distinction, more than 60% -> first, more than 40% -> pass, less than 40% -> fail.

Science=int(input("Enter the marks of Science: "))
Math=int(input("Enter the marks Math: "))
Social=int(input("Enter the marks Social: "))
Nepali=int(input("Enter the marks Nepali: "))

Total_marks= (Science+Math+Social+Nepali)
print(f"The total marks is {Total_marks}")

percentage=(Social+Science+Math+Nepali)/4.0;
print(f"The percentage is {percentage} ")


if percentage >= 70:
    print(f"Grade: Distinction.")
elif percentage >=60:
    print(f"Grade: First Division")
elif percentage >=40:
    print(f"Pass")
elif percentage <=40:
    print(f"Grade: Fail")

print(f"The program is over.")
