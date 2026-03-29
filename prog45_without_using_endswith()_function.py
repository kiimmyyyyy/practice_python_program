def manual_endswith(text, suffix):
    if suffix == "": return True
    return text[-len(suffix):] == suffix

print(manual_endswith("abcd", ""))