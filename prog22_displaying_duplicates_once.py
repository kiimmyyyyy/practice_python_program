nums = [float(input(f"Enter {i} numbers: ")) for i in range(10, 0, -1)]
print(*dict.fromkeys(nums), sep=',')