import pytesseract
from PIL import Image

image = Image.open('C:/Users/konglinggang/Downloads/123/verify.png')
vcode = pytesseract.image_to_string(image)

print(vcode)
