nums = [float(input(f"Enter {i} number: ")) for i in range(10, 0, -1)]
print(*[num for num in nums if nums.count(num) > 1], sep=',')

