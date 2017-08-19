import xbmcaddon
import xbmcgui
import os
import requests

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

ignore_url = addon.getSetting('IgnoreURL')
select_url = addon.getSetting('SelectURL')

print 'Using URLs: %s, %s' % (ignore_url, select_url)

payload = {'action': sys.argv[1],
           'file': sys.argv[2],
           'directory': sys.argv[3]
}

if sys.argv[1] == 'ignore':
    response = requests.post(ignore_url, data=payload)
elif sys.argv[1] == 'select':
    response = requests.post(select_url, data=payload)
elif sys.argv[1] == 'unselect':
    response = requests.post(select_url, data=payload)
else:
    print('Unknown action')
