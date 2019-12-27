import img2pdf
import os
from PIL import Image
image_location = "image.png"    
pdfstore_location = "pdf.pdf"  
myimage = Image.open(image_location)
pdf_data = img2pdf.convert(myimage.filename)
converted_file = open(pdfstore_location,"wb")
converted_file.write(pdf_data)
myimage.close()                

