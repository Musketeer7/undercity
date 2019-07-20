import os
from splitter.settings import MEDIA_ROOT
from splitter.settings import BASE_DIR
from claptcha import Claptcha
from PIL import Image, ImageFont, ImageDraw, ImageChops
import arabic_reshaper
from bidi.algorithm import get_display
from django.core.files.storage import DefaultStorage

def trim(im):
	bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
	diff = ImageChops.difference(im, bg)
	diff = ImageChops.add(diff, diff, 2.0, -100)
	bbox = diff.getbbox()
	if bbox:
		return im.crop(bbox)

def wordsplitter(txtfile):

	from splitter.pagereceiver.models import Known

	file_path = os.path.abspath(os.path.join(MEDIA_ROOT, txtfile.file.name))

	with open(file_path,'r') as f:
		for line in f:
			for word in line.split():
			   # print(word)   

				if (word != 'و'):
					reshaped_text = arabic_reshaper.reshape(word)
					bidi_text = get_display(reshaped_text)
					print(bidi_text)

					image = Image.new("RGBA", (200,50), (255,255,255))
					font_file_path = os.path.join(MEDIA_ROOT, "nazanin.ttf")
					font = ImageFont.truetype(font_file_path, 45, encoding='unic')
					draw = ImageDraw.Draw(image)
					draw.text((0,0), bidi_text, (0,0,0), font=font)
					image = trim(image)
					temp_file_path = os.path.join(MEDIA_ROOT, "known.png")
					image.save(temp_file_path)
					storage = DefaultStorage()
					s = storage.open(temp_file_path, mode='rb')

					new_k = Known.objects.create(img=s, text=word)
