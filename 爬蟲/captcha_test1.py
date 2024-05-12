from PIL import Image
import pytesseract

img = Image.open(r"D:\More Document\Python\宏碁班\課程講義\練習題\Start_Over\爬蟲\image-1.png")
img = img.convert("L")
ans = pytesseract.image_to_string(img)

print(ans)