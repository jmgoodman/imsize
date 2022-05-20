from PIL import Image
import sys

image = Image.open(sys.argv[1])
w,h = image.size
print(w,h)