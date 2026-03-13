num_1 = float(input("Enter first num: "))
num_2 = float(input("Enter second num: "))

first_range = min(num_1, num_2)
second_range = max(num_1, num_2)

print(f"numbers betweekn {num_1} and {num_2}: ")

for num in range(int(first_range) + 1, int(second_range)):
    print(num)
