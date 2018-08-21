import cv2
import numpy as np

img = cv2.imread('test1.jpg')
sky = cv2.imread('sky2.jpg')
mask = cv2.imread('test1-mask.jpg',0)
# ret, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
_,contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
print(len(contours[0]))
print(len(contours[1]))
print(len(contours[2]))
line = []
list = []
for i in range(len(contours)):
    for j in range(len(contours[i])):
        line.append(contours[i][j][0][0])
        list.append(contours[i][j][0][1])

maxline = np.max(line)
minline = np.min(line)
maxlist =  np.max(list)
minlist = np.min(list)

for i in range(len(contours)):
    if len(contours[i])>= 4:
        a = contours[i][0:4]
        break

print(a)
a[0][0][0] = minline
a[0][0][1] = maxlist
a[1][0][0] = maxline
a[1][0][1] = maxlist
a[2][0][0] = maxline
a[2][0][1] = minlist
a[3][0][0] = minline
a[3][0][1] = minlist
print(a)

cnt = a
x, y, w, h = cv2.boundingRect(cnt)
print(x,y)
dst_size = img.shape

print(dst_size)
sky_x = dst_size[1]
sky_y = dst_size[0]

src = cv2.resize(sky, (w, h), interpolation=cv2.INTER_CUBIC)
cv2.imwrite("src_sky.jpg", src)

center = (int((maxline+minline)/2), int((maxlist+minlist)/2))
print(center)

clone = cv2.seamlessClone(src, img, mask, center, cv2.NORMAL_CLONE )
cv2.imwrite('output.jpg',clone)