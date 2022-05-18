from mojo.subscriber import Subscriber, registerRoboFontSubscriber
import glob
from mojo.UI import getDefault
from mojo.extensions import getExtensionDefault
import re
from lib.scripting.scriptTools import ScriptRunner

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

def beautifyMenuTitle(menuTitle):
    readableTitle = menuTitle.translate(transMap).strip()
    words = re.split('(?<=[a-z])(?=[A-Z])|[ _-]', readableTitle)
    result = []
    for w in words:
        if len(w) > 0:
            newWord = w[0].upper() + w[1:]
            result.append(newWord)
    return " ".join(result)

def addToMenuMap(menuMap, menus):
    if menus:
        menuTitle = menus.pop(0)
        dic = menuMap.get(menuTitle, {})
        addToMenuMap(dic, menus)
        menuMap[menuTitle] = dic

def convertFolderStructureToMenuItems(path):
    titleToPaths = {}
    menuMap = {}
    for f in glob.glob(path+"/**/*.py", recursive=True):
        menuTitle = f.split(path)[-1][1:-2]
        # readable titles uses transDic to beautify the title
        readableTitle = beautifyMenuTitle(menuTitle)
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
        self.titleToPaths, menuMap = convertFolderStructureToMenuItems(defaultFolder)
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
        scriptPath = self.titleToPaths[pathTitle]
        ScriptRunner(path=scriptPath)

if __name__ == '__main__':
    registerRoboFontSubscriber(ModularFontOverviewContextualMenu)
