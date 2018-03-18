
from pyzbar.pyzbar import decode
from PIL import Image

tmp = decode(Image.open("image3.jpg"))
print(tmp)