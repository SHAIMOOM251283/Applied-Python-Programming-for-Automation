from PIL import Image, ImageDraw

# Create a blank image with a white background
width, height = 300, 200
image = Image.new("RGB", (width, height), "white")

# Define a box tuple (left, top, right, bottom)
box = (50, 50, 200, 150)

# Draw a rectangle on the image using the box tuple
draw = ImageDraw.Draw(image)
draw.rectangle(box, outline="black", width=2)

# Save the image to a file
image.save("output_image.png")

# Display the image (optional, requires external viewer)
image.show()


# (50, 50)
# +-------------------+
# |                   |
# |                   |
# |                   |
# |                   |
# +-------------------+
#                   (200, 150)

#The left edge is at x-coordinate 50.
#The top edge is at y-coordinate 50.
#The right edge is at x-coordinate 200.
#The bottom edge is at y-coordinate 150.