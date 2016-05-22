from PIL import Image as myImage
import pytesseract

def ocr_text(image_path):

	text = ''

	try:
		img = myImage.open(image_path)
		print img
		# text = pytesseract.image_to_string(img)
	except Exception, e:
		print e

	return text


if __name__ == "__main__":
	ocr_text("./youlei.jpg")