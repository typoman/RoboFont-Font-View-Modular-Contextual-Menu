from mojo.subscriber import Subscriber, registerRoboFontSubscriber
import glob
from mojo.UI import getDefault
from mojo.extensions import getExtensionDefault
import os
from pathlib import PurePath

EXTENSION_KEY = "com.glyphsets.ModularFontOverviewContextualMenu"
DEFAULT_FOLDER = getDefault("pythonDir")

transDic = {
    "-": " ",
    "_": " ",
    "-": " ",
    ".": " ",
    "/": " > ",
}

transMap = str.maketrans(transDic)

def addToMenuMap(menuMap, menus):
    if menus:
        menuTitle = menus.pop(0)
        dic = menuMap.get(menuTitle, {})
        addToMenuMap(dic, menus)
        menuMap[menuTitle] = dic

def convertFolderStrcutureToMenuItems(path):
    titleToPaths = {}
    menuMap = {}
    for f in glob.glob(path+"/**/*.py", recursive=True):
        p = f.split(path)[-1][1:-2]
        # readable titles uses transDic to beautify the title
        readableTitle = p.translate(transMap).strip()
        titleToPaths[readableTitle] = f
        menus = readableTitle.split(" > ")
        addToMenuMap(menuMap, menus)
    return titleToPaths, menuMap

class ModularFontOverviewContextualMenu(Subscriber):

    debug = True

    def build(self):
        self._reset(None)

    def _reset(self, sender):
        defaultFolder = getExtensionDefault(EXTENSION_KEY + ".folder", DEFAULT_FOLDER)
        self.titleToPaths, menuMap = convertFolderStrcutureToMenuItems(defaultFolder)
        self.menuItems = self._convertToMenuItem(menuMap)

    def _convertToMenuItem(self, menuMap):
        result = []
        for menuTitle, nestedMenuMap in menuMap.items():
            if nestedMenuMap == {}:
                result.append((menuTitle, self.runScriptForMenuItem))
            else:
                result.append((menuTitle, self._convertToMenuItem(nestedMenuMap)))
        return result

    def fontOverviewWantsContextualMenuItems(self, info):
        info["itemDescriptions"].extend(self.menuItems)

    def runScriptForMenuItem(self, menuItem):
        menus = [menuItem.title()]
        while menuItem.parentItem() is not None:
            menus.append(menuItem.parentItem().title())
            menuItem = menuItem.parentItem()
        pathTitle = " > ".join(reversed(menus))
        path = self.titleToPaths[pathTitle]
        os.chdir(PurePath(path).parent)
        with open(path, "r", encoding="utf-8") as f:
            exec(f.read())

if __name__ == '__main__':
    registerRoboFontSubscriber(ModularFontOverviewContextualMenu)
