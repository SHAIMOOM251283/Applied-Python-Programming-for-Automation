from docx import Document
from docx.shared import Inches, Cm

doc = Document()

# Add a picture with specified width and height
doc.add_picture('valentine.png', width=Inches(1), height=Cm(4))

# Save the document
doc.save('output.docx')

