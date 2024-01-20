import csv


def main():

    product_file = "week05\\products.csv"

    request_file = "week05\\request.csv"

    product_id_index = 0

    product_quantity_index = 1

    product_name_index = 1
    
    product_price_index = 2

    products_dict = read_dictionary(product_file, product_id_index)

    print(products_dict)

    with open(request_file, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:
            product_id = row_list[product_id_index]
            quantity = int(row_list[product_quantity_index])
            if product_id in products_dict:
                value = products_dict[product_id]
                product_name = value[product_name_index]
                product_price = value[product_price_index]
            print(f'{product_name}: {quantity} @ ${product_price}')

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
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]

                comp_dictionary[key] = row_list
    return comp_dictionary

if __name__ == "__main__":
    main()