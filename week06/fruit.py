
def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    # Add code to reverse and print fruit_list.
    fruit_list.reverse()
    print(f'Reversed: {fruit_list}')
    # Add code to append "orange" to the end of fruit_list and print the list.
    fruit_list.append("orange")
    print(f'Append Orange: {fruit_list}')
    # Add code to find where "apple" is located in fruit_list and insert "cherry" before "apple" in the list and print the list.
    fruit_list.insert(fruit_list.index("apple"), "cherry")
    print(f'Insert cherry: {fruit_list}')
    # Add code to remove "banana" from fruit_list and print the list.
    fruit_list.remove("banana")
    print(f'Remove banana: {fruit_list}')
    # Add code to pop the last element from fruit_list and print the popped element and the list.
    print(f'Popped element: {fruit_list.pop()}')
    print(f'Popped orange: {fruit_list}')
    # Add code to sort and print fruit_list.
    fruit_list.sort()
    print(f'Sorted: {fruit_list}')
    # Add code to clear and print fruit_list.
    fruit_list.clear()
    print(f'Cleared: {fruit_list}')
    # At the bottom of your program write a call to the main function.
if __name__ == "__main__":
    main()