# TODO поиск объекта по пути вида rect1/rect2/rectinner/target

class MyRectangle(object):
    def __init__(self, width, height):
        # print(width, height)
        self.width = width
        self.height = height

    def __eq__(self, other):
        if other is None:
            return False
        return self.width == other.width \
            and self.height == other.height

    def getArea(self):
        return self.width * self.height

    def getAspectRatio(self):
        return self.width / self.height


class UiRectArea(MyRectangle):
    def __init__(self, parent, name, left, top, width, height):
        super().__init__(width, height)
        self.name = name
        self.parent = parent
        self.left = left
        self.top = top
        self.children = []

    @classmethod
    def fromDict(cls, parent, name, aDict):
        # print(aDict['width'], aDict['height'])
        return cls(parent, name, aDict['left'], aDict['top'], aDict['width'], aDict['height'])

    def getLT(self):
        return (self.left, self.top)

    def getRB(self):
        return (self.left + self.width, self.top + self.height)

    def getWH(self):
        return (self.width, self.height)

    # TODO consider move this method to dissection
    def getLTRelativeTo(self, rectArea):
        result = (self.left, self.top)
        # print(self.name)
        # print(self)
        parent = self.parent
        # print(parent.name)
        # print(rectArea)
        while rectArea != parent \
                and parent is not None:
            result = (result[0] + parent.left, result[1] + parent.top)
            if parent.parent is None:
                print('parent is none!')
                break
            parent = parent.parent
            # print(parent.name)

        return result

    # TODO consider move this method to dissection
    def getRBRelativeTo(self, rectArea):
        result = self.getRB()
        # print(self.name)
        # print(self)
        parent = self.parent
        # print(parent.name)
        # print(rectArea)
        while rectArea != parent \
                and parent is not None:
            result = (result[0] + parent.left, result[1] + parent.top)
            if parent.parent is None:
                print('parent is none!')
                break
            parent = parent.parent
            # print(parent.name)

        return result

    def contains(self, other):
        selfRB = self.getRB()
        otherRB = other.getRB()

        return self.left <= other.left \
            and self.top <= other.top \
            and selfRB[0] >= otherRB[0] \
            and selfRB[1] >= otherRB[1]

    def isInside(self, other):
        selfRB = self.getRB()
        otherRB = other.getRB()

        return self.left >= other.left \
            and self.top >= other.top \
            and selfRB[0] <= otherRB[0] \
            and selfRB[1] <= otherRB[1]

    def sameSize(self, other):
        return self.width == other.width \
            and self.height == other.height


class UiRectangleDissection(object):
    def __init__(self):
        self.root = None
        self.rectangles = {}
        self.left = 0
        self.top = 0

    @classmethod
    def fromDict(cls, aDict):
        result = cls()
        root = result.fromDictInner(aDict, result.rectangles)

        result.root = root

        return result

    def setTopLeft(self, left, top):
        self.top = top
        self.left = left

    def fromDictInner(self, aDict, namesDict):

        if 'location' not in aDict:
            return None

        locationDict = aDict['location']

        # object itself
        result = None
        if 'name' in aDict \
            and 'top' in locationDict \
            and 'left' in locationDict \
            and 'width' in locationDict \
                and 'height' in locationDict:
            try:
                obj = UiRectArea.fromDict(None, aDict['name'], locationDict)
            except Exception as e:
                print('UiRectArea from dict caused exception!')
                # return (result, dict())
                raise e
            else:
                # print('New object from dict', obj.name)
                result = obj
                namesDict[obj.name] = obj
        else:
            print('[EX] Not suitable object config')
            raise Exception('Not suitable object config ')

        # children
        if 'children' not in aDict \
                or (not (type(aDict['children']) is list)):
            # print('Children is absent or not list')
            return result

        for i, item in enumerate(aDict['children']):
            if not (type(item) is dict):
                print('child', i, 'is not a dict')
                continue

            obj = None
            try:
                # print('Parse child', i)
                obj = self.fromDictInner(item, namesDict)
            except Exception as e:
                print('[EX] in fromDictInner!')
                print(e)
                continue

            if obj is None:
                continue

            # print('names from outer dict:', namesDict.keys())
            obj.parent = result

            result.children.append(obj)

        return result

    def walkTreeInner(self, obj, func):

        func(obj)

        if not hasattr(obj, 'children'):
            print('no children')
            return

        for child in obj.children:
            self.walkTreeInner(child, func)

    def walkTree(self, func):
        return self.walkTreeInner(self.root, func)

    def getRelativeRect(self, target, relative):
        targetUiRect = self.rectangles.get(target)
        relativeToUiRect = self.rectangles.get(relative)

        left, top = targetUiRect.getLTRelativeTo(relativeToUiRect)
        w, h = targetUiRect.getWH()
        right = left + w
        bottom = top + h

        return ((left, top), (right, bottom))

    def getRB(self):
        return self.root.getRB()

    def getWH(self):
        return self.root.getWH()


# TODO
def findMinimumIncluding():
    pass


def main():
    print('module is not supposed to use as main module!!!')


if __name__ == '__main__':
    main()
