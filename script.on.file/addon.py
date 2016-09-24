import xbmcaddon
import xbmcgui
import os

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
#line1 = "Hello World!"
#line2 = "We can write anything we want here"
#line3 = "Using Python"
 
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

# xbmcgui.Dialog().ok(addonname, line1, line2, line3)

script_dir = os.path.expanduser('~/kodi')
script = script_dir + "/" + "ignorefileOrDir"

filename = sys.argv[1]
directory = sys.argv[2]

print("Running script from: %s" % script_dir)

from subprocess import call
call([script, filename, directory])
