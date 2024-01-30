from PIL import Image
from tkinter import Tk, filedialog

def convert_to_png(input_path, output_path):
    try:
        # Open the JPG image
        with Image.open(input_path) as img:
            # Save the image in PNG format
            img.save(output_path, format='PNG')
        print(f"Conversion successful. Image saved at {output_path}")
    except Exception as e:
        print(f"Error during conversion: {e}")

def select_file():
    root = Tk()
    root.withdraw()

    # Ask the user to select a JPG file
    file_path = filedialog.askopenfilename(title="Select a JPG file", filetypes=[("JPG files", "*.jpg")])

    return file_path

if __name__ == "__main__":
    # Get the input file path
    input_file = select_file()

    if input_file:
        # Determine the output file path by changing the extension to PNG
        output_file = input_file.rsplit('.', 1)[0] + ".png"

        # Convert the selected JPG image to PNG
        convert_to_png(input_file, output_file)
