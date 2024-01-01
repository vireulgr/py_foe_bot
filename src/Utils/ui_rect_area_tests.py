import ui_rect_area as ra
import sys
import yaml


def TEST_UiRectArea():
    obj1 = ra.UiRectArea(None, 'top', 0, 0, 400, 500)
    obj2 = ra.UiRectArea(obj1, 'rect1', 10, 20, 200, 200)
    obj3 = ra.UiRectArea(obj2, 'rect2', 30, 40, 50, 50)

    x, y = obj2.getLTRelativeTo(obj1)
    print(x, y)
    x, y = obj3.getLTRelativeTo(obj1)

    print(x, y)

    x, y = obj3.getLTRelativeTo(obj2)
    print(x, y)


def TEST_UiRectangleDissection():

    with open('Resources/data/manage_army.yaml', 'r') as fr:
        # print(fr.read().encode('utf-8'))
        obj = yaml.load(fr.read(), yaml.Loader)

    dissection = ra.UiRectangleDissection.fromDict(obj)

    def aFunc(el):
        print('{}, p: {}'.format(el.name, el.parent.name if el.parent else 'None'))

    dissection.walkTree(aFunc)


def TEST_UiRectangleDissection_relative():

    with open('Resources/data/manage_army.yaml', 'r') as fr:
        # print(fr.read().encode('utf-8'))
        obj = yaml.load(fr.read(), yaml.Loader)

    dissection = ra.UiRectangleDissection.fromDict(obj)

    try:
        ((t, l), (r, b)) = dissection.getRelativeRect('unit_icon_0', 'manage_army')
        print(t, l, r, b)
    except Exception as e:
        print('exception!')
        print(e)


def main(argv):

    # TEST_UiRectArea()

    # TEST_UiRectangleDissection()

    TEST_UiRectangleDissection_relative()

    # print(obj)
    # newObj, names = fromDict(obj)
    # for name, item in names.items():
    #     parName = 'None'
    #     if item.parent is not None:
    #         parName = item.parent.name

    #     print('{} p: {}({}) children len: {}'.format(name, item.parent, parName, len(item.children)))

    # print(names.keys())

    # try:
    #     walkTree(newObj, lambda el: print('{}, p: {}'.format(el.name, el.parent.name if el.parent else 'None')))
    # except Exception as e:
    #     print('[EX] in walkTree!')
    #     print(e)

    # toFind = 'unit_icon_0'
    # try:
    #     wasyaObj = names[toFind]
    # except KeyError as e:
    #     print('[EX] key error')
    #     print(e)
    #     return

    # rootObj = names['manage_army']

    # print(wasyaObj.getLTRelativeTo(rootObj))


if __name__ == '__main__':
    main(sys.argv)
