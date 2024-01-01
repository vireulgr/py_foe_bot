import pyautogui as ag


def findImageFromList(imgList):

    location = ()
    for pic in imgList:
        try:
            location = ag.locateCenterOnScreen(pic, confidence=0.9)
        except ag.ImageNotFoundException:
            # print(pic + ' not found')
            pass
        else:
            return (True, location)

    return (False, location)

