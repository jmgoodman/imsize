from PIL import Image
import sys

with Image.open(sys.argv[1]) as image:
	w,h = image.size
	print(w,h)