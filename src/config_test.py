import pyautogui as ag
import numpy as np
import cv2 as cv
import colorsys
import sys
from time import sleep
import yaml

import resources as rc
import Utils.ui_rect_area as ra


def TEST_UiRectangleDissection_displayAll():
    # 0) найти окно Управление армией
    try:
        loc = ag.locateOnScreen(rc.imgPatterns['battle']['title'], confidence=0.9)
    except ag.ImageNotFoundException:
        print('battle manage window not found')
        return

    with open('Resources/data/manage_army.yaml', 'r') as fr:
        obj = yaml.load(fr.read(), yaml.Loader)

    dissection = ra.UiRectangleDissection.fromDict(obj)

    windowWidth, windowHeight = dissection.getWH()

    # для отладки
    imgManageArmy = ag.screenshot(region=(int(loc.left), int(loc.top), windowWidth, windowHeight))

    arr = np.array(imgManageArmy)
    arrImgManageArmy = cv.cvtColor(arr, cv.COLOR_RGB2BGR)

    hue = 0
    step = 1 / len(dissection.rectangles)
    for name, uiRect in dissection.rectangles.items():
        lt = uiRect.getLTRelativeTo(dissection.root)
        rb = uiRect.getRBRelativeTo(dissection.root)
        rgbNormalised = colorsys.hsv_to_rgb(hue, 0.8, 1.0)
        rgbColor = tuple(round(x * 255) for x in rgbNormalised)
        hue += step
        cv.rectangle(arrImgManageArmy, lt, rb, rgbColor, 2)

    sleep(2)

    cv.namedWindow('default', cv.WINDOW_AUTOSIZE)
    cv.imshow('default', arrImgManageArmy)
    cv.waitKey(0)

    cv.destroyAllWindows()


def main(argv):
    TEST_UiRectangleDissection_displayAll()


if __name__ == '__main__':

    main(sys.argv)
