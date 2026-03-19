nums = []
while True:
    try:
        num = int(input("Enter a number: "))
        nums.append(num)
        if nums.count(num) == 1:
            print("Unique")
        elif nums.count(num) > 1:
            print("Duplicate")
    except ValueError:
        print("Invalid input")
        break