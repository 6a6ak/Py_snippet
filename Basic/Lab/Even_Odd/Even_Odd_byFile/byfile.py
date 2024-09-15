# Function to find if a number is even or odd
def even_check(numbers):
    if numbers % 2 == 0:
        print(f"{numbers} is Even")
    else:
        print(f"{numbers} is Odd")

# Function to read numbers from the CSV file and pass them to even_check
def read_and_process_csv(file_path):
    try:
        with open(file_path, 'r') as csvfile:  # Open the file in read mode
            content = csvfile.read().strip()  # Read the whole content of the file and strip any extra spaces/newlines
            rows = content.splitlines()  # Split the content into lines

            for row in rows:
                if row.lower() == 'numbers':  # Skip the header if it's the first row
                    continue
                # Split the row into individual numbers
                numbers_list = row.split(',')  # Split by comma to get all numbers
                for number in numbers_list:
                    even_check(int(number.strip()))  # Convert each number to int and check even/odd
    except FileNotFoundError:
        print(f"File not found: {file_path}. Please check the path and try again.")
    except ValueError as e:
        print(f"Value error: {e}. Please check the content of the file.")

# Use the full path to the CSV file
csv_file_path = '../numbers.csv'

# Read and process the CSV file
read_and_process_csv(csv_file_path)
