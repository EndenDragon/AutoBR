import numpy as np
import cv2
import imutils

template = cv2.imread('screen_points/weapon_selection_random_btn.png') # template image
image_o = cv2.imread('screenshots/weapon_selection_deploy.jpeg') # image

template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
image = cv2.cvtColor(image_o, cv2.COLOR_BGR2GRAY)

loc = False
threshold = 0.9
w, h = template.shape[::-1]
for scale in np.linspace(0.2, 1.0, 20)[::-1]:
    resized = imutils.resize(template, width = int(template.shape[1] * scale))
    w, h = resized.shape[::-1]
    res = cv2.matchTemplate(image,resized,cv2.TM_CCOEFF_NORMED)

    loc = np.where( res >= threshold)
    if len(list(zip(*loc[::-1]))) > 0:
        break

if loc and len(list(zip(*loc[::-1]))) > 0:
    for pt in zip(*loc[::-1]):
        cv2.rectangle(image_o, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imshow('Matched Template', image_o)
cv2.waitKey(0)
cv2.destroyAllWindows()