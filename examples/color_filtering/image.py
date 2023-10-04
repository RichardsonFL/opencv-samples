import cv2
import numpy as np

IMAGE_SOURCE = '../data/frames/frame_1.png'
  
# cap = cv2.VideoCapture(0)

def filter_color(path: str):
    # image = cv2.imread(path, cv2.COLOR_BGR2RGB)  # it also work
    image = cv2.imread(path)  # but convert aprt

    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # preparing get_mask_by_color_interval
    threshold = (
        np.array([10,10,50]),
        np.array([200,200,200])
    )
    
    mask = cv2.inRange(rgb, threshold[0], threshold[1])

    result = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow("Preview Original image", image)
    cv2.imshow("Preview Mak", mask)
    cv2.imshow("Preview Result", result)
    cv2.waitKey()


if __name__ == '__main__':
    filter_color(IMAGE_SOURCE)

