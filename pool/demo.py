from __future__ import print_function

import numpy as np
import cv2


def demo(infile):
    # Load an color image in grayscale
    buf = np.fromfile(infile, np.dtype('byte'))
    img = cv2.imdecode(buf, cv2.IMREAD_COLOR)
    output = img.copy()
    img_bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.namedWindow('Pool Table', cv2.WINDOW_NORMAL)
    cv2.imshow('Pool Table', img)
    cv2.namedWindow('Pool Table BW', cv2.WINDOW_NORMAL)
    cv2.imshow('Pool Table BW', img_bw)
    #for i, name in enumerate(["Blue", "Green", "Red"]):
    #    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    #    cv2.imshow(name, img.copy()[:, :, i])

    # use = img_bw
    # use = img.copy()[:, :, 0]
    # use = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)[:, :, 2]
    use = cv2.Canny(img, 70, 100)
    cv2.namedWindow('Pool Table Using', cv2.WINDOW_NORMAL)
    cv2.imshow('Pool Table Using', use)
    circles = cv2.HoughCircles(use, cv2.cv.CV_HOUGH_GRADIENT, dp=4, minDist=20,
                               param2=90.0, minRadius=57, maxRadius=65)
    #, circles[, param1[, param2[, minRadius[, maxRadius]]]]]))
    print(len(circles))
    print(circles[0])

    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")

        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

        # show the output image
        cv2.namedWindow('output', cv2.WINDOW_NORMAL)
        cv2.imshow("output", output)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
