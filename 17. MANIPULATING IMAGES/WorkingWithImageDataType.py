from PIL import Image
catIm = Image.open('zophie.png')
#catIm.show()

print(catIm.size)

width, height = catIm.size
print(width)

print(height)

print(catIm.filename)

print(catIm.format)

print(catIm.format_description)

catIm.save('zophie.jpg')