import base36

# Specify the file path
file_path = "output_image_with_hidden_text.jpg"

# Read the binary form of the file
with open(file_path, "rb") as file:
    binary_data = file.read()


# Convert and print the convertible strings
for string in binary_data.split():
    try:
        byte_data = base36.loads(string)
        print(byte_data)
        original_string = byte_data.to_bytes((byte_data.bit_length() + 7) // 8, "big").decode()

        print(original_string)
    except:
        pass
