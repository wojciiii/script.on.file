import xbmcaddon
import xbmcgui
import os
import requests

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

url="http://192.168.2.37:4444/post"
payload = {'file': sys.argv[1],
           'directory': sys.argv[2]
           }
response = requests.post(url, data=payload)

