import csv


def main():

    student_file = "week05\students.csv"

    student_dictionary = read_dictionary(student_file)

    user_request = int(input("Enter a student I-Number: "))
    if user_request in student_dictionary:
        name = student_dictionary[user_request]
        print(name)
    else:
        print("No such student")

    return

def read_dictionary(filename):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary."""

    student_dictionary = {}

    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:
            if len(row_list) != 0:
                key = int(row_list[0])
                name = row_list[1]

                student_dictionary[key] = name

    """
    Parameters
    filename: the name of the CSV file to read.
    Return: a dictionary that contains
    the contents of the CSV file.
    """

    return student_dictionary

if __name__ == "__main__":
    main()