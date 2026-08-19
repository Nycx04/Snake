import qrcode
from PIL import Image
text_data = input("Enter img path: ")
img = Image.open(text_data)

output = qrcode.make(text_data)
output.save("Kevin.jpg")
print("Qr code successfully")