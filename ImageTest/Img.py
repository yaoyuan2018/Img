from PIL import Image
import numpy as np
import math
import cv2
import matplotlib.pyplot as plt

src = np.array(Image.open('test.jpg'))
img = np.array(Image.open('XJTU.png'))
img2 = np.array(Image.open('filter2.jpg'))

# for i in range(len(img)):
#     for j in range(len(img[i])):
#         if img[i][j][0] == src[10][10][0] and img[i][j][1] == src[10][10][1] and img[i][j][2] == src[10][10][2]:
#             print(i)
#             print(j)
#             break


z = src[100][100][0]
y = src[100][100][1]
x = src[100][100][2]

pos_x = math.floor(y / 4) + math.floor(x/32) * 64
pos_y = math.floor(z / 4) + math.floor((x % 32) / 16)*64

print(img[int(pos_x)][int(pos_y)+1])
print(img[int(pos_x)+1][int(pos_y)])
#
# print(pos_x)
# print(pos_y)
#
print(img[int(pos_x)][int(pos_y)])
print(src[100][100])

print(img2[int(pos_x)][int(pos_y)])

print(img)



for i in range(len(src)):
    for j in range(len(src[i])):
        z = src[i][j][0]
        y = src[i][j][1]
        x = src[i][j][2]
        pos_x = int(y / 4) + int(x / 32) * 64
        pos_y = int(z / 4) + int((x % 32) / 16) * 64
        src[i][j] = img2[pos_x][pos_y]


cv2.imwrite('lvjing.jpg',src)


# line = []
# for i in range(len(img)):
#     for j in range(len(img[i])):
#         line.append(img[i][j])

# print(line[0])


# print(img.shape)
# print(img.dtype)
# print(img.size)
# print(img)
# print(img2)

