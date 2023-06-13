import pytesseract
import PIL
import matplotlib.pyplot

# 读取验证码图片
image = PIL.Image.open('app/captcha.png')

# 将图片转为灰度图像
image = image.convert('L')
# matplotlib.pyplot.imshow(image)
# matplotlib.pyplot.show()

# 对图像进行二值化处理
threshold = 127
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')
# matplotlib.pyplot.imshow(image)
# matplotlib.pyplot.show()

# 使用pytesseract进行识别
code = pytesseract.image_to_string(
    image, config='-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz')

print(code)
