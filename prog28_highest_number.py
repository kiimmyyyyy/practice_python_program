nums = []
while True:
    try:
        num = float(input("Enter a number: "))
        nums.append(num)
    except ValueError:
        print("Invalid input")
        print(f"The highest number you entered is {max(nums)}")
        break