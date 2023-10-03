import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def edges_detection(img: str, values: tuple = (100, 200)):
    assert img is not None, "file could not be read, check with os.path.exists()"

    # Image in gray scale maybe better to obtain a best result of edges.
    # But exists another pssibilites.
    image = cv.imread(img, cv.IMREAD_GRAYSCALE)
    # img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    edges = cv.Canny(
        image=image,
        threshold1=values[0],
        threshold2=values[1]
    )

    name, ext =  img.split('.')
    output = name + '_edges.' + ext
    print(output)
    cv.imwrite(output, edges)

if __name__ == '__main__':
    edges_detection('../data/images/sample.png', values=(10,200))
