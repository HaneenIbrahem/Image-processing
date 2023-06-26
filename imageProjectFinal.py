import numpy as np
import cv2
#Name :Isra Awwad &&Haneen Ibrahem
img = cv2.imread('input.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,240, 255,1)

contours,h = cv2.findContours(thresh,1,2)
cv2.imshow('im',img)
for isy in contours:
    approx = cv2.approxPolyDP(isy,0.01*cv2.arcLength(isy,True),True)
    print
    len(approx)
    if len(approx)==3:
        print
        "triangle"
        cv2.drawContours(img,[isy],0,(51,153,0),-1)

    elif len(approx)==4:
        area = cv2.contourArea(isy)
        (x, y, w, h) = cv2.boundingRect(approx)

        if( (area /(w*float (h)))>=0.95 and(area /(w*float (h)))<=1.05):
           cv2.drawContours(img, [isy], 0, (153, 51, 0), -1)
        else:
         cv2.drawContours(img,[isy],0,(0,0,0),-1)

    elif len(approx)>11:
        (x, y, w, h) = cv2.boundingRect(approx)
        ar = w / float(h)
        cv2.drawContours(img, [isy], 0, (0, 0, 255), -1) if ar >= 0.95 and ar <= 1.05 else cv2.drawContours(img, [isy], 0, (0, 0, 0), -1)

    else:
          print
          "other"
          cv2.drawContours(img, [isy], 0, (0, 0, 0), -1)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Name :Isra Awwad &&Haneen Ibrahem