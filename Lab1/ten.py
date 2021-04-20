'''Write a Python program to convert seconds to day, hour, minutes and seconds.'''

second = int(input("Enter the value for seconds: "))

day = (((second // 60) // 60) // 24)

hour = ((second // 60) // 60)

minutes = (second // 60)

remain_second = (second % 60)

print(f"Total day for given seconds:{day}")
print(f"Total hour for given seconds:{hour}")
print(f"Total minutes for given seconds:{minutes}")
print(f"Total remaining second:{remain_second}")