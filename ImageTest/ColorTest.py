import cv2
import numpy as np

def findPos()

def myFilter(orimap, newmap, picname):
    ori = cv2.imread(orimap)
    new = cv2.imread(newmap)
    src = cv2.imread(picname)

    pic_name = picname.split('/')[-1].split('.')[0]
    style_name = newmap.split('/')[-1].split('.')[0]

    tmp = "tmp/"+pic_name+"-"+style_name+".jpg"

    #printPri(ori)

    #filter
    for i in range(len(src)):
        for j in range(len(src[0])):
            pos = findPos(src[i][j], ori)
            src[i][j] = new[pos[0], pos[1]]

    cv2.imwrite(tmp,src)
    return tmp