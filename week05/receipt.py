import csv
from datetime import datetime

"""
Print the store name at the top of the receipt.
Print the list of ordered items.
Sum and print the number of ordered items.
Sum and print the subtotal due.
Compute and print the sales tax amount. Use 6% as the sales tax rate.
Compute and print the total amount due.
Print a thank you message.
Get the current date and time from your computer’s operating system and print the current date and time.
Include a try block and except blocks to handle FileNotFoundError, PermissionError, and KeyError.
"""

"""
Included a discount for if the current day is either Tuesday or Wednesday and printed the discount amount
"""

def main():

    current_date_and_time = datetime.now()

    day_of_the_week = current_date_and_time.weekday()

    product_file = "week05\\products.csv"

    request_file = "week05\\request.csv"

    product_id_index = 0

    product_quantity_index = 1

    product_name_index = 1
    
    product_price_index = 2

    subtotal = 0

    quantity_total = 0

    sales_tax = 0.06

    total_price = 0

    products_dict = read_dictionary(product_file, product_id_index)

    company_name = "Dave's Pin Exchange"

    # print(products_dict)
    print(company_name)
    print('')
    try:
        with open(request_file, "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)

            for row_list in reader:
                product_id = row_list[product_id_index]
                quantity = int(row_list[product_quantity_index])

                if product_id in products_dict:
                    try:
                        value = products_dict[product_id]
                        product_name = value[product_name_index]
                        product_price = float(value[product_price_index])
                        product_total_price = product_price * quantity
                        subtotal += product_total_price
                        quantity_total += quantity
                        print(f'{product_name}: {quantity} @ ${product_price}')
                    except KeyError as key_error:
                        print(f'KeyError: {key_error}')
                else:
                    print(f'Product with product ID {product_id} was not found.')
        if day_of_the_week == 1 or day_of_the_week == 2:
            discount = subtotal * .1
            sales_tax_amount = (subtotal - discount) * sales_tax
            total_price = sales_tax_amount + subtotal - discount
        else:
            sales_tax_amount = subtotal * sales_tax
            total_price = subtotal + sales_tax_amount
        print('')
        print(f'Number of items: {quantity_total}')
        print(f'Subtotal: ${subtotal:.2f}')
        if day_of_the_week == 1 or day_of_the_week == 2:
            print(f'Thank you for shopping with us today! You received a discount of: ${discount:.2f}')
        print(f'Sales tax: ${sales_tax_amount:.2f}')
        print(f'Total: ${total_price:.2f}')
    except FileNotFoundError as not_found_error:
        print(not_found_error)
    print('')
    print(f'Thank you for shopping at {company_name}.')
    print(f'{current_date_and_time:%A %I:%M %p}')

    pass

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary."""

    comp_dictionary = {}

    """Parameters
    filename: the name of the CSV file to read.
    key_column_index: the index of the column
        to use as the keys in the dictionary.
    Return: a compound dictionary that contains
    the contents of the CSV file.
    """
    try:
        with open(filename, "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)

            for row_list in reader:
                if len(row_list) != 0:
                    key = row_list[key_column_index]

                    comp_dictionary[key] = row_list
        return comp_dictionary
    except PermissionError as perm_error:
        print(perm_error)

if __name__ == "__main__":
    main()