import cv2
import numpy
from tkinter import *
import tkinter as tk
from tkinter import filedialog

def show_image():
    # root = tk.Tk()
    # root.withdraw()
    # file_path = filedialog.askopenfilename()
    #
    # print(file_path)


    img = cv2.imread('basketball1.png', 1)
    cv2.imshow('Input image',img)
    cv2.waitKey()


def contrast():
    img = cv2.imread('basketball1.png', 1)
    new_image = numpy.zeros(img.shape, img.dtype)
    beta = 2

    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            for c in range(img.shape[2]):
                new_image[y, x, c] = numpy.clip(beta * img[y, x, c] + beta, 0, 255)
    cv2.imshow('Original Image', img)
    cv2.imshow('Contrast Image', new_image)
    cv2.waitKey()

def brightness():
    img = cv2.imread('basketball1.png', 1)
    new_image = numpy.zeros(img.shape, img.dtype)
    alpha = .3
    beta = 100

    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            for c in range(img.shape[2]):
                new_image[y, x, c] = numpy.clip(alpha * img[y, x, c] + beta, 0, 255)
    cv2.imshow('Original Image', img)
    cv2.imshow('Brightness Image', new_image)
    cv2.waitKey()

def thresholding():
    img = cv2.imread('basketball1.png', 0)
    new_image = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 127, 1)
    cv2.imshow('Thresholding Image', new_image)
    cv2.imshow('Original Image', img)
    cv2.waitKey()

def extract():
    img = cv2.imread("basketball1.png", 0)
    r, c = img.shape
    x = numpy.zeros((r, c, 8), dtype=numpy.uint8)
    x[:, :, 4] = 2 ** 4
    r = numpy.zeros((r, c, 8), dtype=numpy.uint8)

    r[:, :, 4] = cv2.bitwise_and(img, x[:, :, 4])
    mask = r[:, :, 4] > 0
    r[mask] = 255
    cv2.imshow("Original Image", img)
    cv2.imshow('Extracting the bit planes Image', r[:, :, 4])
    cv2.waitKey()

def save():
    img = cv2.imread('basketball1.png', 1)



def controller(img, brightness=255, contrast=127):
    brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255))

    contrast = int((contrast - 0) * (127 - (-127)) / (254 - 0) + (-127))

    if brightness != 0:

        if brightness > 0:

            shadow = brightness

            max = 255

        else:

            shadow = 0
            max = 255 + brightness

        alpha = (max - shadow) / 255
        beta = shadow


        cal = cv2.addWeighted(img, alpha,
                              img, 0, beta)

    else:
        cal = img

    if contrast != 0:
        Alpha1 = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        beta1 = 127 * (1 - Alpha1)

        cal = cv2.addWeighted(cal, Alpha1,
                              cal, 0, beta1)


    return cal




def BrightnessContrast(brightness=0):
    brightness = cv2.getTrackbarPos('Brightness',
                                    'Image')

    contrast = cv2.getTrackbarPos('Contrast',
                                  'Image')

    effect = controller(original,
                        brightness,
                        contrast)


    cv2.imshow('Effect', effect)



original = cv2.imread("basketball1.png")



cv2.imshow('Image', original)

cv2.createTrackbar('Brightness', 'Image',
                       255, 2 * 255,
                       BrightnessContrast)

cv2.createTrackbar('Contrast', 'Image',
                       127, 2 * 127,
                       BrightnessContrast)

BrightnessContrast(0)
cv2.waitKey()



r = Tk()
frame = Frame(r)
frame.pack()
bottomframe = Frame(r)
bottomframe.pack(side=LEFT)
redbutton = Button(frame, text='show input image', fg='red', command=show_image)
redbutton.pack(side=LEFT)
greenbutton = Button(frame, text='Modifying the brightness', fg='blue', command = brightness)
greenbutton.pack(side=LEFT)
bluebutton = Button(frame, text='Modifying the contrast', fg='green', command=contrast)
bluebutton.pack(side=RIGHT)
blackbutton = Button(bottomframe, text='Thresholding', fg='green',command=thresholding)
blackbutton.pack(side=LEFT)
blackbutton = Button(bottomframe, text='Extracting the bit planes', fg='blue', command=extract)
blackbutton.pack(side=LEFT)
blackbutton = Button(bottomframe, text='Saving the processed image', fg='red', command=save())
blackbutton.pack(side=RIGHT)
r.mainloop()


