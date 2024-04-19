import pytesseract
from PIL import Image

# Set the path to the Tesseract executable (change this according to your system)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open the image file
image_path = r'C:\Users\jplop\Pictures\fotosprueba\20230621_112908.jpg'  # Replace with the actual path to your image
image = Image.open(image_path)

# Convert the image to grayscale
image = image.convert('L')

# Use Tesseract to extract the text from the image
extracted_text = pytesseract.image_to_string(image)

# Print the extracted text
print(extracted_text)
