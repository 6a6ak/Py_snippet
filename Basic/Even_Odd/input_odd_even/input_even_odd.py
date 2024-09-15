#inputs
numbers = input("Enter numbers sprated by commas:")
numbers = numbers.split(',') 

#for loop
for result in numbers:
    result = int(result) #convert to intiger
  #  check if it is even or odd
    if result %2 == 0:
        print (f"{result} is Even")

    else:
        print (f"{result} is Odd")
