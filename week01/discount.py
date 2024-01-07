"""Work as a team to write a Python program named 
discount.py that gets a customer’s subtotal as 
input and gets the current day of the week from 
your computer’s operating system. Your program 
must not ask the user to enter the day of the week. 
Instead, it must get the day of the week from 
your computer’s operating system.

If the subtotal is $50 or greater and today is 
Tuesday or Wednesday, your program must subtract 
10% from the subtotal. Your program must then 
compute the total amount due by adding sales 
tax of 6% to the subtotal. Your program must 
print the discount amount if applicable, 
the sales tax amount, and the total amount due."""

import math
from datetime import datetime

user_subtotal = float(input('What does the cost come to?'))

current_day = datetime.now()

day_of_the_week = current_day.weekday()

# day_of_the_week = 2

discount = 0

if user_subtotal >= 50 and (day_of_the_week == 1 or day_of_the_week == 2):
    discount = user_subtotal * .1
    sales_tax = (user_subtotal - discount) * 0.06
else:
    sales_tax = user_subtotal * .06

total = user_subtotal + sales_tax - discount

difference_to_discount = 50 - user_subtotal


if day_of_the_week == 1 or day_of_the_week == 2:
    print(f'Thank you for shopping with us! Your total without tax is {user_subtotal:.2f} and sales tax is {sales_tax:.2f} AND your discount is {discount:.2f} if you spend more than $50 with us today you will receive a 10% off coupon from you total order, spend just {difference_to_discount:.2f} more to receive your discount! Your total is {total:.2f} ')
else:
    print(f'Your total without tax is {user_subtotal:.2f} and sales tax is {sales_tax:.2f}. Your total comes to {total}.')


