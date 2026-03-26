def manual_removeprefix(text, prefix):
    if text[:len(prefix)] == prefix:
        return text[len(prefix):]
    return text

print(manual_removeprefix("PANGET", "P"))