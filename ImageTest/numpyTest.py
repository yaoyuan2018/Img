import numpy as np
import cv2
from PIL import Image
a = np.array(cv2.imread('xjtu.jpg'))
img = np.array(cv2.imread('XJTU.png'))
img2 = np.array(cv2.imread('pinkday.jpg'))


x = []
y = []
z = []
pos_x = np.array([])
pos_y = np.array([])
for i in range(len(a)):
        x.extend(a[i][:,0])
        y.extend(a[i][:,1])
        z.extend(a[i][:,2])


y = np.array(y)
x = np.array(x)
z = np.array(z)
pos_x = np.floor(y/4).astype(np.int32) + np.floor(x / 32).astype(np.int32) * 64
pos_y = np.floor(z / 4).astype(np.int32) + np.floor((x % 32) / 16).astype(np.int32) * 64

print(pos_x)
print(pos_y)
print(len(pos_x))
print(len(pos_y))
count = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = img2[pos_x[count]][pos_y[count]]
        count+=1

cv2.imwrite('xjtu1.jpg',a)



# print(np.floor(y1/4).astype(np.int32))

#
# print(pos_x)
# print(pos_y)
# print(a[0][1])
# print(a[0][:,1])
# print(a[0])
# print(a[:,0][:,0])


