def manual_isupper(text):
    has_alpha = False
    for char in text:
        if 'a' <= char <= 'z':
            return False
        if 'A' <= char <= 'Z':
            has_alpha = True
    return has_alpha

print(manual_isupper("PANGET"))