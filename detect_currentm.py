import cv2
import numpy as np
import os

MIN_WIDTH = 10
MAX_WIDTH = 120
MIN_HEIGHT = 10
MAX_HEIGHT = 120
BLOCK_SIZE = 15
C = 30
def current_method(input_path, out_path):
    list_files = os.listdir(input_path)

    for img_name in list_files:
        img_path = input_path + img_name

        image = cv2.imread(img_path)
        image = cv2.resize(image, (1024, 720))
        result = image.copy()

        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,BLOCK_SIZE,C)

        # Fill rectangular contours
        cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        for c in cnts:
            approx = cv2.approxPolyDP(c, 0.01* cv2.arcLength(c, True), True)
            if len(approx) == 4:
                x, y , w, h = cv2.boundingRect(approx)
                if   MIN_WIDTH <= w <= MAX_WIDTH and MIN_HEIGHT <= h <= MAX_HEIGHT:
                    cv2.drawContours(image, [approx], -1, (0,0,0), -1)

        #cv2.imshow('shapes', image)
        cv2.imwrite(os.path.join(out_path, "currentm_" + img_name), image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()