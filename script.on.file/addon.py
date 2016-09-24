import xbmcaddon
import xbmcgui
import os

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

script_dir = os.path.expanduser('~/kodi')
script = script_dir + "/" + "onkodiselection.sh"

filename = sys.argv[1]
directory = sys.argv[2]

print("Running script from: %s" % script_dir)

from subprocess import call
call([script, filename, directory])
