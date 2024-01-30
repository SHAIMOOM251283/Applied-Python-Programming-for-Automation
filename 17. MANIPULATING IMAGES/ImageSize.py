import os
from PIL import Image

def calculate_pixel_size(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
        return width, height

def print_image_sizes():
    # Get the current working directory
    folder_path = os.getcwd()

    # Get a list of all files in the current working directory
    files = os.listdir(folder_path)

    for file in files:
        # Check if the file is an image (you may want to add more image file extensions)
        if file.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp")):
            # Get the full path to the image
            image_path = os.path.join(folder_path, file)
            
            # Calculate the width and height using the previously defined function
            width, height = calculate_pixel_size(image_path)

            # Print the result
            print(f"{file}: Width={width} pixels, Height={height} pixels")

# Example usage
print_image_sizes()
