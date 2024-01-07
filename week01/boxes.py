"""A manufacturing company needs a program that 
will help its employees pack manufactured items 
into boxes for shipping. Write a Python program 
named boxes.py that asks the user for two integers:

the number of manufactured items
the number of items that the user will pack per box

Your program must compute and print the number of 
boxes necessary to hold the items. This must be 
a whole number. Note that the last box may be 
packed with fewer items than the other boxes."""

import math

num_items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))

num_boxes_needed = math.ceil(num_items / items_per_box)

print()

print(f"For {num_items} items, packing {items_per_box} items in each box, you will need {num_boxes_needed} boxes.")