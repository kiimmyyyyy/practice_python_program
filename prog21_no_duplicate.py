numbers = []
without_duplicates = []

for i in range (10, 0, -1):
    number = float(input(f"Enter a number: "))
    numbers.append(number)

for num in numbers:
    if numbers.count(num) == 1:
        without_duplicates.append(num)
print(without_duplicates)