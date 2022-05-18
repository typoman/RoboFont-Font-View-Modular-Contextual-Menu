from contextualMenu import EXTENSION_KEY
from mojo.extensions import getExtensionDefault
import AppKit

p = getExtensionDefault(EXTENSION_KEY + ".folder")
AppKit.NSWorkspace.sharedWorkspace().selectFile_inFileViewerRootedAtPath_(p, '')
