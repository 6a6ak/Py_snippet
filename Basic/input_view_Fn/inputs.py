# Input: "1,2,3"
def get_num():
    numbers = input("Enter a series of numbers separated by commas: ")  # Input as a string
    numbers_list = numbers.split(',')  # Split the string into a list using ',' as a delimiter
    numbers_list = [int(num) for num in numbers_list]  # Convert each string to an integer
    return numbers_list #4 having it outside of the function

