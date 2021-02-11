INVIS_CHAR = "‌"

def magic(text, mode="normal"):
    result = ""
    if mode == "normal":
        result = INVIS_CHAR.join(list(text))

    return result

text = "Hello! This is a test"
print(magic(text))

def test(old, new):
    return old == new

print(test(text, magic(text)))

print("Old length: " + str(len(text)) + "\nNew length: " + str(len(magic(text))))