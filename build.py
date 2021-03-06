import os
from mojo.extensions import ExtensionBundle

# get current folder
basePath = os.path.dirname(__file__)

# source folder for all extension files
sourcePath = os.path.join(basePath, 'source')

# folder with python files
libPath = os.path.join(sourcePath, 'code')

# folder with html files
htmlPath = os.path.join(sourcePath, 'documentation')

# load license text from file
# see choosealicense.com for more open-source licenses
licensePath = os.path.join(basePath, 'license.txt')

# required extensions
requirementsPath = os.path.join(basePath, 'requirements.txt')

# name of the compiled extension file
extensionFile = 'roboFontModularFontViewContextualMenu.roboFontExt'

# path of the compiled extension
buildPath = os.path.join(basePath, 'build')
extensionPath = os.path.join(buildPath, extensionFile)

# initiate the extension builder
B = ExtensionBundle()

# name of the extension
B.name = "Font View Menu"

# name of the developer
B.developer = 'Bahman Eslami'

# URL of the developer
B.developerURL = 'http://bahman.design'

# version of the extension
B.version = '0.0.2'

# should the extension be launched at start-up?
B.launchAtStartUp = True

# script to be executed when RF starts
B.mainScript = 'contextualMenu.py'

# does the extension contain html help files?
B.html = True

# minimum RoboFont version required for this extension
B.requiresVersionMajor = '4'
B.requiresVersionMinor = '2'

# scripts which should appear in Extensions menu
B.addToMenu = [
    {
        'path':          'revealScriptFolder.py',
        'preferredName': 'Reveal Script Folder',
        'shortKey':      '',
    },
    {
        'path':          'setScriptFolder.py',
        'preferredName': 'Set Script Folder',
        'shortKey':      '',
    },
    {
        'path':          'contextualMenu.py',
        'preferredName': 'Refresh Menu Items',
        'shortKey':      '',
    }
]

# license for the extension
with open(licensePath) as license:
    B.license = license.read()

# required extensions
with open(requirementsPath) as requirements:
    B.requirements = requirements.read()

# copy readme contents to the extension docs
readmeText = ''
with open("README.md", "r", encoding="utf-8") as f:
    readmeText = f.read()
with open("source/documentation/index.md", "w", encoding="utf-8") as f:
    f.write(readmeText)

# expiration date for trial extensions
# B.expireDate = '2022-12-31'

# compile and save the extension bundle
print('building extension...', end=' ')
B.save(extensionPath, libPath=libPath, htmlPath=htmlPath)
print('done!')

# check for problems in the compiled extension
print()
print(B.validationErrors())