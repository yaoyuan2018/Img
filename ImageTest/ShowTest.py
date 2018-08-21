from PIL import Image,ImageFilter

im = Image.open('go.jpg')

# #图像转灰度
# im_gray = im.convert("L")
# im_gray.show()
#
# #使用模糊滤镜
# im_1 = im.filter(ImageFilter.BLUR)
# im_1.show()

#旋转45度
im.rotate(45).show()
