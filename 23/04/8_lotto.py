import random

# Create an array with numbers from 1 to 45
numbers = list(range(1, 46))
result = []

# Remove duplicates and sort the selected numbers
num = [0] * 46
for i in range(4):
    selected_numbers = random.sample(numbers, 6)
    selected_numbersV = sorted(set(selected_numbers))
    print(selected_numbersV)