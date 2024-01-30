import os
from PIL import Image

# Load the catlogo.png
logo_path = "catlogo.png"
logo = Image.open(logo_path)

# Create a new folder named "withLogo" in the current working directory
output_folder_path = "withLogo"
os.makedirs(output_folder_path, exist_ok=True)

# Iterate through all images in the folder
folder_path = os.getcwd()  # Use the current working directory
for image_name in os.listdir(folder_path):
    if image_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        # Load the image
        image_path = os.path.join(folder_path, image_name)
        original_image = Image.open(image_path)

        # Resize the logo to fit the bottom right corner
        resized_logo = logo.resize((100, 100))  # Adjust the size as needed

        # Calculate the position to paste the logo
        paste_position = (
            original_image.width - resized_logo.width,
            original_image.height - resized_logo.height,
        )

        # Paste the logo onto the original image
        original_image.paste(resized_logo, paste_position, resized_logo)

        # Save the modified image to the "withLogo" folder
        output_path = os.path.join(output_folder_path, image_name)
        original_image.save(output_path)

# Close the logo image
logo.close()
