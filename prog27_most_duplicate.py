nums = []
most_dup= 0
num_highest = None
while True:
    try:
        num = float(input("Enter a number: "))
        nums.append(num)
        if nums.count(num) > most_dup:
            most_dup = nums.count(num)
            num_highest = num
    except ValueError:
        print("Invalid input")
        print(f"The number with most duplicates is {num_highest} with {most_dup} duplicates")
        break