from PIL import Image, ImageDraw, ImageFont
import os

# Create a folder for seating cards
seating_cards_folder = "seating cards"
os.makedirs(seating_cards_folder, exist_ok=True)

# Load the list of guests from the guests.txt file
guests_file_path = "guests.txt"
with open(guests_file_path, "r") as file:
    guests = file.read().splitlines()

# Load the flower image and resize it to 100x100 pixels
flower_image_path = "flower.png"
flower_image = Image.open(flower_image_path)
flower_image = flower_image.resize((100, 100))

# Create seating cards for each guest
for seat_number, guest in enumerate(guests, start=1):
    # Create a blank image with the specified dimensions
    image = Image.new("RGB", (288, 360), "white")
    draw = ImageDraw.Draw(image)

    # Load a font for the guest's name and seat number
    font_size = 38  # Adjust the font size as needed
    font_name = ImageFont.load_default()
    font_seat = ImageFont.load_default()

    # Calculate text size and position for the guest's name
    text_bbox_name = draw.textbbox((0, 0), guest, font=font_name)
    text_position_name = ((image.width - text_bbox_name[2]) // 2, (image.height - text_bbox_name[3]) // 2 - 20)

    # Add the guest's name to the image
    draw.text(text_position_name, guest, font=font_name, fill="black")

    # Calculate text size and position for the seat number
    text_bbox_seat = draw.textbbox((0, 0), f"Seat {seat_number}", font=font_seat)
    text_position_seat = ((image.width - text_bbox_seat[2]) // 2, (image.height - text_bbox_seat[3]) // 2 + 20)

    # Add the seat number to the image
    draw.text(text_position_seat, f"Seat {seat_number}", font=font_seat, fill="black")

    # Calculate the position for the logo (bottom right corner)
    logo_position = (image.width - flower_image.width, image.height - flower_image.height)

    # Paste the logo onto the image
    image.paste(flower_image, logo_position, flower_image)

    # Save the image to the seating cards folder
    seating_card_path = os.path.join(seating_cards_folder, f"{guest}_seating_card.png")
    image.save(seating_card_path)

print("Seating cards created and saved in the 'seating cards' folder.")
