from PIL import Image
import base36


def hide_base36_text_in_image(image_path, hidden_text, output_path):
    # Open the image and read its binary data
    with open(image_path, "rb") as image_file:
        image_data = bytearray(image_file.read())

    # Encode the hidden text in base36
    encoded_text = base36.dumps(int.from_bytes(hidden_text.encode(), byteorder="big"))

    # Add newline characters before and after the encoded text
    encoded_text_with_newlines = "\n" + encoded_text + "\n"

    # Calculate the position to insert the base36-encoded text in the middle of the image
    middle_position = len(image_data) // 2

    # Insert the base36-encoded text into the image data
    image_data = (
        image_data[:middle_position]
        + encoded_text_with_newlines.encode()
        + image_data[middle_position:]
    )

    # Save the new image with hidden base36-encoded text
    with open(output_path, "wb") as output_file:
        output_file.write(image_data)


if __name__ == "__main__":
    # Replace these paths and hidden text with your actual values
    image_path = "Everest.jpg"
    hidden_text = "ShaastraCTF{C0m3_W3st1n}"
    output_path = "output_image_with_hidden_text.jpg"

    hide_base36_text_in_image(image_path, hidden_text, output_path)
