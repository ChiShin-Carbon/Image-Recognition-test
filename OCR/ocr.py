from PIL import Image
import pytesseract


# 載入圖片
img_name = './image.png'
img = Image.open(img_name)

# 使用 pytesseract 進行 OCR
text = pytesseract.image_to_string(img, lang='chi_tra+eng')

# 輸出識別的文字
print("識別的文字為:", text)
