
import imgutils
import pandas as pd
import cv2
import matplotlib.pyplot as plt
import extraction_silhouette
import contours_image

import part3
part3.main_3()

###### début 2.2

path_sample = "data/sample.jpg"

base, image = extraction_silhouette.silhouette(path_sample)

imgutils.plot_gray(image)
plt.show()

#######début 2.3

img_contours, contours = contours_image.extraction_contour(image, base)

imgutils.plot_rgb(img_contours)
plt.show()

list = contours_image.ten_contours(contours)


img_large_contours = cv2.drawContours(base.copy(), list, -1, (0, 255, 0), 3)
imgutils.plot_rgb(img_large_contours)
plt.show()

rect = imgutils.get_receipt_contour(list)
img_rect = cv2.drawContours(base.copy(), rect, -1, (0, 255, 0), 3)
imgutils.plot_rgb(img_rect)
plt.show()

#######2.4