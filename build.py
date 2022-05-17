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
extensionFile = 'roboFontContextualMenu.roboFontExt'

# path of the compiled extension
buildPath = os.path.join(basePath, 'build')
extensionPath = os.path.join(buildPath, extensionFile)

# initiate the extension builder
B = ExtensionBundle()

# name of the extension
B.name = "roboFontContextualMenu"

# name of the developer
B.developer = 'Frank Grie?hammer, Bahman Eslami'

# URL of the developer
B.developerURL = 'http://bahman.design'

# version of the extension
B.version = '0.0.1'

# should the extension be launched at start-up?
B.launchAtStartUp = True

# script to be executed when RF starts
B.mainScript = 'contextualMenu.py'

# does the extension contain html help files?
B.html = True

# minimum RoboFont version required for this extension
B.requiresVersionMajor = '3'
B.requiresVersionMinor = '0'

# scripts which should appear in Extensions menu
# B.addToMenu = [
#     {
#         'path':          'doSomething.py',
#         'preferredName': 'do something',
#         'shortKey':      None,
#     },
# ]

# license for the extension
with open(licensePath) as license:
    B.license = license.read()

# required extensions
with open(requirementsPath) as requirements:
    B.requirements = requirements.read()

# expiration date for trial extensions
B.expireDate = '2022-12-31'

# compile and save the extension bundle
print('building extension...', end=' ')
B.save(extensionPath, libPath=libPath, htmlPath=htmlPath)
print('done!')

# check for problems in the compiled extension
print()
print(B.validationErrors())