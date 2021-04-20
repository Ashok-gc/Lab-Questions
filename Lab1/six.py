'''Solve each of the following problems using Python Scripts. Make sure you use appropriate variable
names and comments. When there is a final answer have Python print it to the screen. A person’s
body mass index (BMI) is defined as: BMI=mass in kg / (height in m)2.'''

print('Enter your weight in kilo:')
weightInKilo = float(input())

print('Enter your height in feet:')

heightInFeet = float(input())

heightInMeter = heightInFeet * 12 * 0.025

bodyMassIndex = weightInKilo / (heightInMeter ** 2)

if bodyMassIndex < 15:
    print('Your BMI = ' + str(bodyMassIndex)  + ' You are very severely underweight.')

elif bodyMassIndex >= 15 and bodyMassIndex <= 16 :
    print('Your BMI = ' + str(bodyMassIndex)     + ' You are severely underweight.')

elif bodyMassIndex > 16 and bodyMassIndex <= 18.5:
    print('Your BMI = ' + str(bodyMassIndex) + ' You are underweight.')

elif bodyMassIndex > 18.5 and bodyMassIndex <= 25:
    print('Your BMI = ' + str(bodyMassIndex) + ' You are Normal(healthy weight).')

elif bodyMassIndex > 25 and bodyMassIndex <= 30:
    print('Your BMI = ' + str(bodyMassIndex) + ' You are overweight.')


elif bodyMassIndex > 30 and bodyMassIndex <= 35:
    print('Your BMI = ' + str(bodyMassIndex) + ' You are moderately obese.')

elif bodyMassIndex > 35 and bodyMassIndex <= 40:
    print('Your BMI = ' + str(bodyMassIndex) + ' You are severely obese.')

elif bodyMassIndex > 40:
    print('Your BMI = ' + str(bodyMassIndex) + ' You are very severely obese.')

input('Please press Enter to exit')
