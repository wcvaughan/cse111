import math
from datetime import datetime
"""
The size of a car tire in the United States is represented with three numbers like this: 205/60R15. 
The first number is the width of the tire in millimeters. The second number is the aspect ratio. 
The third number is the diameter in inches of the wheel that the tire fits. The volume of space inside a tire can be approximated with this formula:

v = (math.pi * (w ** 2) * a * (w * a + 2450 * d)) / 10000000000

v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.

"""

print('I can calculate the volume of your tire!')

width = int(input('Enter the width of the tire in mm (ex 205): '))

aspect = int(input('Enter the aspect ratio of the tire (ex 60): '))

diameter = int(input('Enter the diameter of the tire in inches (ex 15): '))

volume = (math.pi * (width ** 2) * aspect * ((width * aspect) + (2540 * diameter))) / 10000000000

print(f'The approximate volume is: {volume:.2f}')

user_buy = input('Would you like to buy some tires?')

if user_buy.lower() == 'yes':
    user_phone_num = int(input('Please enter your phone number'))
    user_phone_num = '{:0>10}'.format(user_phone_num)  # Pad with zeros to the left if needed
    user_phone_num = '({}{}{}) {}{}{}-{}{}{}{}'.format(*user_phone_num)


"""
The previous lesson’s prove milestone required you to write a program named tire_volume.py that computes the approximate volume of air inside a tire. Add code near the end of that program that does the following:

Gets the current date from the computer’s operating system.
Opens a text file named volumes.txt for appending.
Appends to the end of the volumes.txt file one line of text that contains the following five values:
current date
width of the tire
aspect ratio of the tire
diameter of the wheel
volume of the tire

"""


with open("week01\\volumes.txt", "at") as volumes_file:
    
    current_date_and_time = datetime.now()

    current_date_and_time = current_date_and_time.strftime("%Y-%m-%d")
    
    customer_data = [current_date_and_time, width, aspect, diameter, volume, user_phone_num]

    line = ", ".join(map(str, customer_data))

    volumes_file.write(line + "\n")
    
    