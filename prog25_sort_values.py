nums = []
while True:
    try:
        num = float(input("Enter a number: "))
        nums.append(num)
    except ValueError:
        print("Invalid input")
        print(*sorted(nums), sep=',')
        break