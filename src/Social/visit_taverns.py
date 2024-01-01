import sys
import pyautogui as ag
import resources as rc
from time import sleep

from Utils.utils import findImageFromList


class TavernVisitor(object):

    def __init__(self):
        self.socPanelActive = False
        self.socFriendsActiveImagePath = rc.imgPatterns['social']['buttons']['friends_active']
        self.socFriendsInactiveImagePath = rc.imgPatterns['social']['buttons']['friends_inactive']
        self.socMaximizeImagePath = rc.imgPatterns['social']['buttons']['maximize']
        self.socEndImagePath = rc.imgPatterns['social']['buttons']['end']
        self.tavernImagePath = rc.imgPatterns['social']['player']['tavern_ready']
        self.socFarLeftImagePath = rc.imgPatterns['social']['buttons']['far_left']
        self.socNumberOneList = rc.imgPatterns['social']['player']['number_one_list']

    # open friends social panel
    def socialOpenFriends(self):
        try:
            x, y = ag.locateCenterOnScreen(self.socMaximizeImagePath, confidence=0.9)
        except ag.ImageNotFoundException:
            print('soc maximize button not found')
        else:
            ag.moveTo(x, y, 1)
            ag.click()

        sleep(1)

        try:
            x, y = ag.locateCenterOnScreen(self.socFriendsInactiveImagePath, confidence=0.9)
            # print('soc firends Inactive FOUND')
        except ag.ImageNotFoundException:
            # print('soc firends Inactive NOT found')
            pass
        else:
            ag.moveTo(x, y, 1)
            ag.click()
            ag.moveTo(x - 50, y - 60)

        try:
            x, y = ag.locateCenterOnScreen(self.socFriendsActiveImagePath, confidence=0.8)
            self.socPanelActive = True
            print('soc firends Active FOUND')
        except ag.ImageNotFoundException:
            print('soc friends Active NOT found!')
            exit(0)

        if not self.socPanelActive:
            ag.moveTo(x, y, 1)
            ag.click()

    # visit taverns
    def visitTaverns(self):

        self.socialOpenFriends()

        try:
            x, y = ag.locateCenterOnScreen(self.socEndImagePath, confidence=0.8)
        except ag.ImageNotFoundException:
            print('social panel not found!')
            return

        ag.moveTo(x, y, 1)
        ag.click()

        allProcessed = False

        try:
            socFarLeftButtonLocation = ag.locateCenterOnScreen(self.socFarLeftImagePath,
                                                               confidence=0.8)
        except ag.ImageNotFoundException:
            print('Far left social button not found! something is wrong!')
            return
        # print(socFarLeftButtonLocation)

        while not allProcessed:

            sleep(0.5)  # чтобы дать время прогрузиться картинкам с друзьями

            try:
                for i in ag.locateAllOnScreen(self.tavernImagePath):
                    # print(i)
                    x, y = ag.center(i)
                    ag.moveTo(x, y, 1)
                    ag.click()
            except ag.pyscreeze.ImageNotFoundException:
                # print('tavern not found')
                pass

            numberOneFound = findImageFromList(self.socNumberOneList)

            if not numberOneFound[0]:
                print('number one NOT found')
                ag.moveTo(socFarLeftButtonLocation[0], socFarLeftButtonLocation[1], 1)
                ag.click()
            else:
                print('number one FOUND')
                ag.moveTo(numberOneFound[1][0], numberOneFound[1][1], 1)
                allProcessed = True


def main(argv):
    # socPanelActive = False
    # socFriendsActiveImagePath = imgPatterns['social']['buttons']['friends_active']
    # socFriendsInactiveImagePath = imgPatterns['social']['buttons']['friends_inactive']

    # socMaximizeImagePath = imgPatterns['social']['buttons']['maximize']
    # try:
    #     x, y = ag.locateCenterOnScreen(socMaximizeImagePath, confidence=0.9)
    # except:
    #     print('soc maximize button not found')
    # else:
    #     ag.moveTo(x, y, 1)
    #     ag.click()

    # sleep(1)

    # try:
    #     x, y = ag.locateCenterOnScreen(socFriendsInactiveImagePath, confidence=0.9)
    #     print('soc firends Inactive FOUND')
    # except ag.ImageNotFoundException as e:
    #     print('soc firends Inactive NOT found')
    # else:
    #     ag.moveTo(x, y, 1)
    #     ag.click()
    #     ag.moveTo(x - 50, y - 60)

    # try:
    #     location = ag.locateOnScreen(socFriendsActiveImagePath, confidence=0.8)
    #     socPanelActive = True
    #     print('soc firends Active FOUND')
    # except ag.ImageNotFoundException as e:
    #     print('soc friends Active NOT found!')
    #     exit(0)

    # if not socPanelActive:
    #     ag.moveTo(location[0] + location[2] / 2 , location[1] + location[3] / 2, 1)
    #     ag.click()

    # socEndImagePath = imgPatterns['social']['buttons']['end'];
    # try:
    #     location = ag.locateOnScreen(socEndImagePath, confidence=0.8)
    # except ag.ImageNotFoundException as e:
    #     print('social panel not found!')
    #     exit(0)

    # ag.moveTo(location[0] + location[2] / 2 , location[1] + location[3] / 2, 1)
    # ag.click()

    # tavernImagePath = imgPatterns['social']['player']['tavern_ready'];

    # allProcessed = False

    # socFarLeftImagePath = imgPatterns['social']['buttons']['far_left']
    # try:
    #     socFarLeftButtonLocation = ag.locateOnScreen(socFarLeftImagePath, confidence=0.8)
    # except ag.ImageNotFoundException as e:
    #     print('far left social button not found! something is wrong!')
    #     exit(0)
    # print(socFarLeftButtonLocation)

    # while not allProcessed:
    #     try:
    #         for i in ag.locateAllOnScreen(tavernImagePath):
    #             #print(i)
    #             ag.moveTo(i[0] + i[2] / 2, i[1] + i[3] / 2, 1)
    #             ag.click()
    #     except ag.pyscreeze.ImageNotFoundException as e:
    #         print('tavern not found')
    #         pass

    #     socNumberOneList = imgPatterns['social']['player']['number_one_list']
    #     numberOneFound = False
    #     for pic in socNumberOneList:
    #         try:
    #             location = ag.locateOnScreen(pic, confidence=0.9)
    #         except ag.ImageNotFoundException:
    #             print(pic + ' not found')
    #         else:
    #             print(location)
    #             ag.moveTo(location[0], location[1], 1)
    #             numberOneFound = True

    #     if not numberOneFound:
    #         print('number one NOT found')
    #         ag.moveTo(socFarLeftButtonLocation[0] + socFarLeftButtonLocation[2] / 2,
    #                     socFarLeftButtonLocation[1] + socFarLeftButtonLocation[3] / 2, 1)
    #         ag.click()

    #     else:
    #         print('number one FOUND')
    #         allProcessed = True
    pass


if __name__ == '__main__':
    main(sys.argv)
