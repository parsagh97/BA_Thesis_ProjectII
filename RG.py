from PIL import Image
import numpy as np
from scipy.spatial import distance

def fingerprint(PATH):
    normalized_size =512
    img = Image.open(PATH).convert("L")
    img = img.resize((normalized_size, normalized_size))
    img = img.crop((128,128,384,384))
    x, y = img.size
    smoothed_image = np.zeros((16, 16), dtype=int)
    i = 0
    while i<256:
        j = 0
        while j<256:
            m = i/16
            n = j/16
            tmp = int(np.asarray(img.crop((m*8, n*8, (m+1)*8, (n+1)*8))).ravel().mean())
            if tmp < 52:
                smoothed_image[int(i / 16), int(j / 16)] = -2
            elif tmp < 103:
                smoothed_image[int(i / 16), int(j / 16)] = -1
            elif tmp < 154:
                smoothed_image[int(i / 16), int(j / 16)] = 0
            elif tmp < 205:
                smoothed_image[int(i / 16), int(j / 16)] = 1
            else:
                smoothed_image[int(i / 16), int(j / 16)] = 2
            j += 16
        i += 16

    selected_blocks = np.zeros((8, 8), dtype=int)

    i,m = 0,0
    while i < 16:
        j,n =  0,0
        while j < 16:
            selected_blocks[m,n] = smoothed_image[i,j]
            j += 2
            n +=1
        i += 2
        m += 1

    # print(selected_blocks)
    diff = []

    for i in range(8):
        for j in range(8):
            if (j - 1) >= 0 and (i - 1) >= 0:
                diff.append(int(selected_blocks[j][i] - selected_blocks[j - 1][i - 1]))
            else:
                diff.append(0)
            if (j - 1) >= 0:
                diff.append(int(selected_blocks[j][i] - selected_blocks[j - 1][i]))
            else:
                diff.append(0)
            if (j - 1) >= 0 and (i + 1) < 8:
                diff.append(int(selected_blocks[j][i] - selected_blocks[j - 1][i + 1]))
            else:
                diff.append(0)
            if (i - 1) >= 0:
                diff.append(int(selected_blocks[j][i] - selected_blocks[j][i - 1]))
            else:
                diff.append(0)
            if (i + 1) < 8:
                diff.append(int(selected_blocks[j][i] - selected_blocks[j][i + 1]))
            else:
                diff.append(0)
            if (j + 1) < 8 and (i - 1) >= 0:
                diff.append(int(selected_blocks[j][i] - selected_blocks[j + 1][i - 1]))
            else:
                diff.append(0)
            if (j + 1) < 8:
                diff.append(int(selected_blocks[j][i] - selected_blocks[j + 1][i]))
            else:
                diff.append(0)
            if (j + 1) < 8 and (i + 1) < 8:
                diff.append(int(selected_blocks[j][i] - selected_blocks[j + 1][i + 1]))
            else:
                diff.append(0)
            # diff.append(tmp)
    return diff

# a = fingerprint("/home/parsa/ProjectII/dataset_scrips/natural-images/selected/35.jpg")
# b = fingerprint("/home/parsa/ProjectII/dataset_scrips/natural-images/selected/brightness/15_brightness.jpg")
#
# print(distance.hamming(a, b))
