odd = 0
for i in range (10):
    numbers = int(input("Enter a number: "))
    if float(numbers) % 2 != 0:
        odd += 1
print(odd)