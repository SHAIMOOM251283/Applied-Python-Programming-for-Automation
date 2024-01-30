#An RGBA value represents a color in digital graphics and is commonly used in web design, image editing, and computer graphics. 
#The term "RGBA" stands for Red, Green, Blue, and Alpha.

#To get the RGBA value of the color 'CornflowerBlue' using the Pillow module in Python, you can use the ImageColor module provided by Pillow. 
#Here's an example:
from PIL import ImageColor
# Get the RGBA value of 'CornflowerBlue'
cornflower_blue_rgba = ImageColor.getrgb('CornflowerBlue')
print(f'RGBA value of CornflowerBlue: {cornflower_blue_rgba}')
#The output will be a tuple in the format (R, G, B, A), where each component is an integer value between 0 and 255. 
#If the color does not have an alpha channel (like 'CornflowerBlue'), the alpha value will be 255 (fully opaque).

#A box tuple, in the context of image processing and the Python Imaging Library (PIL) or its successor Pillow, refers to a tuple that defines a rectangular region or bounding box. 
#The format of the box tuple is (left, upper, right, lower). Here's a breakdown of what each value represents:
#left: The x-coordinate of the left edge of the box.
#upper: The y-coordinate of the upper edge of the box.
#right: The x-coordinate of the right edge of the box.
#lower: The y-coordinate of the lower edge of the box.
from PIL import Image
# Open an image
original_image = Image.open("zophie.jpg")
# Define a box tuple (left, upper, right, lower)
box = (100, 50, 300, 200)
# Crop the image using the box tuple
cropped_image = original_image.crop(box)
# Save the cropped image
cropped_image.save("zophie_cropped.jpg")
#In this example, the box tuple is used to define the region to be cropped from the original image.

#In Pillow you can use the Image.open() function to open an image file and obtain an Image object. 
#Here's an example using the file named "zophie.png":
from PIL import Image
# Open an image file and obtain an Image object
image_path = "zophie.png"
image = Image.open(image_path)
# Now 'image' is an Image object representing the content of the image file
# You can perform various operations on this Image object
# For example, you can display the image using the show() method
image.show()

#To find out the width and height of an Image object's image in Pillow, you can use the size attribute. 
#The size attribute returns a tuple representing the width and height of the image. Here's an example:
from PIL import Image
# Open an image file and obtain an Image object
image_path = "zophie.png"
image = Image.open(image_path)
# Get the width and height of the image using the size attribute
width, height = image.size
# Print the results
print(f"Width: {width}px")
print(f"Height: {height}px")

#To get an Image object for a 100×100 image, excluding the lower-left quarter of it in Pillow, you can use the crop() method. 
#The crop() method allows you to extract a rectangular region (specified by a box tuple) from the original image. 
#You can then create a new Image object with the cropped region. Here's an example:
from PIL import Image
# Open an image file and obtain an Image object
image_path = "zophie.png"
original_image = Image.open(image_path)
# Define the box tuple for the upper-right three-quarters of the image
# The box tuple format is (left, upper, right, lower)
box = (0, 0, original_image.width // 2, original_image.height // 2)
# Crop the image using the box tuple
cropped_image = original_image.crop(box)
# Display the original and cropped images (optional)
original_image.show()
cropped_image.show()
# Save the cropped image to a file (optional)
cropped_image.save("zophie_cropped.png")

#To save changes made to an Image object in Pillow, you can use the save() method. 
from PIL import Image
# Open an image file and obtain an Image object
image_path = "your_image.png"
image = Image.open(image_path)
# Perform operations on the Image object (e.g., cropping, resizing, etc.)
# ...
# Save the modified Image object to a new file
output_path = "output_image.png"
image.save(output_path)
# You can also specify the file format explicitly
# image.save(output_path, format="PNG")
# or
# image.save(output_path, format="JPEG")
# ...
# Note: The file format is inferred from the file extension by default.
#In this example, the save() method is called on the Image object, and the modified image is saved to a new file specified by the output_path. 
#You can specify the file format explicitly by providing the format parameter, or Pillow will infer it from the file extension in the output path.

#In Pillow, the shape-drawing code is contained in the ImageDraw module. 
#The ImageDraw module provides a set of methods for drawing shapes, text, and other elements on an Image object. 
#You can use it to draw lines, rectangles, ellipses, polygons, text, and more.
from PIL import Image, ImageDraw
# Open an image file and obtain an Image object
image_path = "zophie.png"
image = Image.open(image_path)
# Create an ImageDraw object
draw = ImageDraw.Draw(image)
# Define the coordinates of the rectangle (left, upper, right, lower)
rectangle_coordinates = (50, 50, 150, 150)
# Set the color for drawing (red in this case)
fill_color = (255, 0, 0)  # RGB values for red
# Draw a red rectangle on the image
draw.rectangle(rectangle_coordinates, fill=fill_color)
# Save or display the modified image
image.save("zophie_new_image.png")
image.show()

#In the Pillow module (PIL Fork), the primary object for image manipulation is the Image class. 
#While Image objects themselves do not have direct drawing methods, you can use the ImageDraw module within Pillow to draw on Image objects.
#Here's a basic example:
from PIL import Image, ImageDraw
# Create a new image with a white background
width, height = 300, 200
image = Image.new("RGB", (width, height), "white")
# Get a drawing context
draw = ImageDraw.Draw(image)
# Draw a red rectangle
draw.rectangle([(50, 50), (150, 150)], fill="red")
# Draw a green circle
draw.ellipse([(180, 50), (280, 150)], fill="green")
# Save or display the image
image.save("new_output_image.png")
image.show()
#In this example, we create an Image object with a white background. 
#Then, we use the ImageDraw module to get a drawing context (draw). 
#With the drawing context, you can use methods like rectangle and ellipse to draw shapes onto the image. 
#Finally, you can save or display the resulting image.

