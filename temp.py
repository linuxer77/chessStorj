
def InsertBinary(text):
    binary_list = [format(ord(char), '08b') for char in text]
    with open("binary.txt", "w") as f:
        f.write(''.join(binary_list))

InsertBinary("Hello World")
