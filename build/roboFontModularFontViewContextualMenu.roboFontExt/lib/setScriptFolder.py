from mojo.UI import GetFolder
from contextualMenu import EXTENSION_KEY, ModularFontOverviewContextualMenu
from mojo.subscriber import registerRoboFontSubscriber
from mojo.extensions import setExtensionDefault

theNewFolder = GetFolder()
if theNewFolder:
	setExtensionDefault(EXTENSION_KEY + ".folder", theNewFolder)
	registerRoboFontSubscriber(ModularFontOverviewContextualMenu)
