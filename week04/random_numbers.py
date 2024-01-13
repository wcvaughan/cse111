import random

def main():

    numbers = [ 16.2, 75.1, 52.3 ]

    words = []

    append_random_numbers(numbers)

    print(numbers)

    append_random_numbers(numbers, 3)

    print(numbers)

    pass

def append_random_numbers(numbers_list, quantity = 1):

    num = 0

    while num < quantity:

        random_number = random.uniform(0, 100)

        rounded = round(random_number, 1)

        numbers_list.append(rounded)

        num += 1

    return

def append_random_words(words_list, quantity = 1):

    num = 0

    list_of_words = [""]

    while num < quantity:

        random_word = random.choice(list_of_words)

        words_list.append(random_word)

    return

if __name__ == "__main__":
    main()