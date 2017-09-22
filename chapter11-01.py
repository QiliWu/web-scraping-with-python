from PIL import Image, ImageFilter


logo = Image.open(r'D:\03-CS\web scraping with python\logo.jpg')
for i in range(5):
    blurrylogo = logo.filter(ImageFilter.GaussianBlur)
    blurrylogo.save('logo_blurred.jpg')
    blurrylogo.show()
    logo = Image.open(r'D:\03-CS\web scraping with python\logo_blurred.jpg')