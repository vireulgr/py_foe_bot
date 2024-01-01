import pyautogui as ag
import yaml
from time import sleep

import Utils.ui_rect_area as ra
import resources as rc


def battle():
    # 0) найти окно Управление армией
    try:
        loc = ag.locateOnScreen(rc.imgPatterns['battle']['title'], confidence=0.9)
    except ag.ImageNotFoundException:
        print('battle manage window not found')
        return

    with open('Resources/data/manage_army.yaml', 'r') as fr:
        obj = yaml.load(fr.read(), yaml.Loader)

    dissection = ra.UiRectangleDissection.fromDict(obj)

    # 1) очистить юнитов
    try:
        ((l, t), (r, b)) = dissection.getRelativeRect('unit_icon_0', 'manage_army')
        # print(l, t, r, b)
    except Exception as e:
        print('exception!')
        print(e)

    windowWidth, windowHeight = dissection.getWH()

    ag.moveTo(loc.left + l + 20, loc.top + t + 20, 1)
    for _ in range(10):
        ag.click()
        sleep(0.3)

    # 2) найти иконку вкладки тяжёлых юнитов и кликнуть
    ((l, t), (r, b)) = dissection.getRelativeRect('heavy', 'manage_army')
    ag.moveTo(loc.left + l + 10, loc.top + t + 7, 1)
    ag.click()
    sleep(0.3)

    # 3) найти нужный вид юнитов
    #   a) Если не найден - прокрутить скроллбар вправо
    #   b) GOTO 3
    # 4) кликнуть 3 раза
    # 5) найти иконку вкладки лёгких юнитов и кликнуть
    # 6) найти разбойников
    #   a) Если не найден - прокрутить скроллбар вправо
    #   b) GOTO 6
    # 7) найти кнопку автобой и нажать


def main():
    print('module is not supposed to use as main module!!!')


if __name__ == '__main__':
    main()
