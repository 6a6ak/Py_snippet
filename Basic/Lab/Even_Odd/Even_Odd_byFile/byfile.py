import csv
# Function to find if a number is even or odd
def even_check(numbers):
    if numbers % 2 == 0:
        print(f"{numbers} is Even")
    else:
        print(f"{numbers} is Odd")

# Function to read numbers from the CSV file and pass them to even_check
def read_and_process_csv(file_path):
    with open(file_path, 'r') as csvfile:  
        content = csvfile.read()  
        numbers_list = content.split(',')  

        for number in numbers_list:
            even_check(int(number.strip()))  

# CSV file path
csv_file_path = 'numbers.csv'

# Read and process the CSV file
read_and_process_csv(csv_file_path)