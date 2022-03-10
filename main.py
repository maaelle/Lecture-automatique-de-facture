
import imgutils
import pandas as pd
import cv2
import matplotlib.pyplot as plt
import extraction_silhouette

import part3
part3.main_3()

###### début 2.2

path_sample = "data/sample.jpg"

extraction_silhouette.silhouette(path_sample)

#######début 2.3

def list_area(list):
    area = []
    for i in range(len(list)):
        area_contours = cv2.contourArea(list[i])
        area.append(area_contours)
    return area

contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img_contours = cv2.drawContours(Resize.copy(), contours, -1, (0,255,0), 3)
imgutils.plot_rgb(img_contours)
plt.show()

area_list = list_area(contours)

index = []
for i in range (len(contours)):
    index.append(i)


df = pd.DataFrame({'index':index ,'area': area_list})

df_sorted = df.sort_values(by=['area'], ascending=False)


list_index = df_sorted['index'].head(10)

list_contours = []
for i in list_index:
    list_contours.append(contours[i])


img_large_contours = cv2.drawContours(Resize.copy(), list_contours, -1, (0, 255, 0), 3)
imgutils.plot_rgb(img_large_contours)
plt.show()

rect = imgutils.get_receipt_contour(list_contours)
img_rect = cv2.drawContours(Resize.copy(), rect, -1, (0, 255, 0), 3)
imgutils.plot_rgb(img_rect)
plt.show()

#######2.4