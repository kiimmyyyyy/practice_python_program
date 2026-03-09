even = 0
for i in range(10):
    numbers = float(input(f"Enter {i} a number: "))
    if numbers % 2 == 0:
        even += 1
print(even)