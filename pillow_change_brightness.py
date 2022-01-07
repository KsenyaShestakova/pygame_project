import os
from PIL import Image


def box(filename, endname):
    fullname = os.path.join('Игра', 'data', filename)
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
            pixels2[i, j] = int(pixels[i, j][0]) - 20,\
                            int(pixels[i, j][1]) - 20,\
                            int(pixels[i, j][2]) - 20
    endname = os.path.join('Игра', 'data', endname)
    res.save(endname)


box('BUTTON_old_game.png', 'BUTTON_old_game_change.png')