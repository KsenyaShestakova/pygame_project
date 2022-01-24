import os
from PIL import Image


def box(filename, endname):
    fullname = os.path.join('data', filename)
    image = Image.open(fullname)
    pixels = image.load()
    x, y = image.size
    res = Image.new('RGB', (x, y), (0, 0, 0))
    pixels2 = res.load()
    for i in range(x):
        for j in range(y):
            sr_zn = int((int(pixels[i, j][1]) + int(pixels[i, j][2])) / 2)
            if int(pixels[i, j][0]) + 50 > 255:
                pixels2[i, j] = 255, sr_zn, sr_zn
            else:
                pixels2[i, j] = int(pixels[i, j][0]) + 50, sr_zn, sr_zn
            pixels2[i, j] = int(int(pixels[i, j][0]) - 50),\
                            int(int(pixels[i, j][1]) - 50),\
                            int(int(pixels[i, j][2]) - 50)
    endname = os.path.join('data', endname)
    res.save(endname)


box('save_btn.jpg', 'save_btn_change.jpg')