#Rabinovic and O'Gorman with hypercomplex method
from PIL import Image
import numpy as np
from scipy.spatial import distance

NORMALIZED_SIZE = 512
path ="C:/Users/parsa/Desktop/repot project 2/2.jpg"

def fingerprint(path):
    img = Image.open(path)
    img = img.resize((NORMALIZED_SIZE, NORMALIZED_SIZE))
    img = img.crop((128, 128, 384, 384))

    i = 0
    grids = np.zeros((16, 16, 3), dtype=int)
    single_grids = np.zeros((16,16), dtype=int)
    # img.show()
    while i < 256:
        j = 0
        while j < 256:
            cropped = img.crop((j, i, j+8, i+8))
            rgb_matix = list(cropped.getdata()) # 8*8*3
            red = int(np.asarray([i[0] for i in rgb_matix]).mean())
            green = int(np.asarray([i[1] for i in rgb_matix]).mean())
            blue = int(np.asarray([i[2] for i in rgb_matix]).mean())
            grids[int(i/16)][int(j/16)] = [red, green, blue]
            # single_grids[int(i / 16)][int(j / 16)] =  int(np.asarray(grids[int(i/16)][int(j/16)]).mean())
            if int(np.asarray(grids[int(i/16)][int(j/16)]).mean()) < 52:
                single_grids[int(i / 16)][int(j / 16)] = -2
            elif int(np.asarray(grids[int(i/16)][int(j/16)]).mean()) < 103:
                single_grids[int(i / 16)][int(j / 16)] = -1
            elif int(np.asarray(grids[int(i / 16)][int(j / 16)]).mean()) < 155:
                single_grids[int(i / 16)][int(j / 16)] = 0
            elif int(np.asarray(grids[int(i / 16)][int(j / 16)]).mean()) < 205:
                single_grids[int(i / 16)][int(j / 16)] = 1
            elif int(np.asarray(grids[int(i / 16)][int(j / 16)]).mean()) < 255:
                single_grids[int(i / 16)][int(j / 16)] = 2
            j += 16
        i += 16
    img2 = Image.fromarray(grids, 'RGB').show()
    img2 = Image.fromarray(grids, 'RGB').show()
    tmp_sing = np.zeros((18,18), dtype=int)
    tmp_sing[0][0] = single_grids[0][0]
    tmp_sing[0][17] = single_grids[0][15]
    tmp_sing[17][0] = single_grids[15][0]
    tmp_sing[17][17] = single_grids[15][15]
    for j in range(1,17):
        tmp_sing[0][j] = single_grids[0][j-1]
    for j in range(1,17):
        tmp_sing[17][j] = single_grids[15][j-1]
    for i in range(1,17):
        tmp_sing[i][0] = single_grids[i-1][0]
    for i in range(1,17):
        tmp_sing[i][17] = single_grids[i-1][15]
    for i in range(1, 17):
        for j in range(1,17):
            tmp_sing[i][j] = single_grids[i-1][j-1]

    finger_print = []
    for i in range(1, 17):
        for j in range(1,17):
            finger_print.append(tmp_sing[i][j]-tmp_sing[i-1][j])
            finger_print.append(tmp_sing[i][j]-tmp_sing[i-1][j-1])
            finger_print.append(tmp_sing[i][j]-tmp_sing[i][j-1])
            finger_print.append(tmp_sing[i][j]-tmp_sing[i+1][j-1])
            finger_print.append(tmp_sing[i][j]-tmp_sing[i+1][j])
            finger_print.append(tmp_sing[i][j]-tmp_sing[i+1][j+1])
            finger_print.append(tmp_sing[i][j]-tmp_sing[i][j+1])
            finger_print.append(tmp_sing[i][j]-tmp_sing[i-1][j+1])

    return finger_print

# fingerprint(path)
a = fingerprint("E:/from ubuntu/natural-images/selected/0.jpg")
b = fingerprint('E:/from ubuntu/natural-images/selected/19.jpg')

from numpy import linalg as LA
import os
def sim(a, b):
    a_norm = LA.norm(a)
    b_norm = LA.norm(b)
    sub_norm = LA.norm(np.subtract(a, b))
    if (a_norm+b_norm) == 0:
        return 0
    return sub_norm/(a_norm+b_norm)

print(sim(a,b))
