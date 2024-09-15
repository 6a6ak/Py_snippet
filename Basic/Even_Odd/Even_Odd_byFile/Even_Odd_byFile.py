
def even_check(number):
    if number % 2 == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")

# 
def read_and_process_csv(file_path):
    with open(file_path, 'r') as csvfile:  # 
        content = csvfile.read()  # 
        numbers_list = content.split(',')  #
        for number in numbers_list:
            even_check(int(number.strip()))  
# 
csv_file_path = 'random_numbers.csv'

# 
read_and_process_csv(csv_file_path)
