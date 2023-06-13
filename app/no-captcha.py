import pytesseract
import PIL
import matplotlib.pyplot as plt

# 读取验证码图片
image = PIL.Image.open('captcha.png')

# 将图片转为灰度图像
image = image.convert('L')
# plt.imshow(image)
# plt.show()

# 对图像进行二值化处理
threshold = 127
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')
# plt.imshow(image)
# plt.show()

# 使用pytesseract进行识别
code = pytesseract.image_to_string(
    image, config='-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz')

print(code)
