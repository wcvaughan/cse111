"""
Open the provinces.txt file for reading.
Read the contents of the file into a list where each line of text in the file is stored in a separate element in the list.
Print the entire list.
Remove the first element from the list.
Remove the last element from the list.
Replace all occurrences of "AB" in the list with "Alberta".
Count the number of elements that are "Alberta" and print that number.
"""

import csv

def main():

    with open("week05\provinces.txt", "rt") as csv_file:

        reader = csv.reader(csv_file)

        row_list = list(reader)

        element_of_interest = "AB"

        replacement_element = "Alberta"

        occurrence_count = 0

        print(row_list)
        
        for row_list in reader:
            row_list.pop(0)
            row_list.pop()
        
        for row in row_list:
            for i in range (len(row)):
                if row[i] == element_of_interest:
                    row[i] = replacement_element

        occurrence_count_one = sum(row.count(replacement_element) for row in row_list)
        
        for row in row_list:
            for element in row:
                if element == replacement_element:
                    occurrence_count += 1
        print(occurrence_count)
        print(occurrence_count_one)

if __name__ == "__main__":
    main()