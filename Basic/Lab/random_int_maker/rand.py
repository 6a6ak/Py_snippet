import random
import os

# تعداد اعداد تصادفی که می‌خواهیم تولید کنیم
number_count = 100

# تولید لیستی از 100 عدد تصادفی بین 1 تا 1000
random_numbers = [str(random.randint(1, 1000)) for _ in range(number_count)]

# ساخت رشته‌ای که اعداد با کاما جدا شده‌اند
numbers_string = ','.join(random_numbers)

# به دست آوردن مسیر دایرکتوری فعلی اسکریپت
current_dir = os.path.dirname(os.path.abspath(__file__))

# مسیر فایل CSV که قرار است در همان دایرکتوری ذخیره شود
csv_file_path = os.path.join(current_dir, 'random_numbers.csv')

# ذخیره به عنوان فایل CSV
with open(csv_file_path, 'w') as file:
    file.write('numbers\n')  # اضافه کردن هدر به فایل
    file.write(numbers_string)  # نوشتن اعداد در فایل

print(f"CSV file created at: {csv_file_path}")
