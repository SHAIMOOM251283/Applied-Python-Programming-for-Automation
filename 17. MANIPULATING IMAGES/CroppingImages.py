from PIL import Image
catIm = Image.open('zophie.png')
croppedIm = catIm.crop((335, 345, 565, 560))
croppedIm.save('cropped.png')

#from PIL import Image
# Open a JPG image
#catIm = Image.open('your_image.jpg')
# Crop the image
#croppedIm = catIm.crop((335, 345, 565, 560))
# Save the cropped image
#croppedIm.save('cropped.jpg')

#from PIL import Image
# Open a PNG image
#png_image = Image.open('input.png')
# Crop the image
#cropped_image = png_image.crop((335, 345, 565, 560))
# Save the cropped image as JPG
#cropped_image.save('output.jpg', 'JPEG')

#from PIL import Image
# Open a JPG image
#jpg_image = Image.open('input.jpg')
# Crop the image
#cropped_image = jpg_image.crop((335, 345, 565, 560))
# Save the cropped image as PNG
#cropped_image.save('output.png', 'PNG')
