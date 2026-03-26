def manual_lstrip(text):
    # Initialize index tracker
    start_index = 0

    # Loop through the string
    for char in text:
        if char == " ":
            start_index += 1
        else:
            # We found a non-space character, so break the loop
            break

    # Return the slice from the first non-space character to the end
    return text[start_index:]

test_str = "    Hello World!    "
result = manual_lstrip(test_str)

print(f"Original: '{test_str}'")
print(f"Stripped: '{result}'")