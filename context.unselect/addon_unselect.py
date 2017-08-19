# -*- coding: utf-8 -*-		
		
import xbmc		
import sys

if __name__ == '__main__':
	if xbmc.getCondVisibility("Container.Content(files)"):
		fn=xbmc.getInfoLabel("ListItem.FileName")
		print ("Filename %s" % fn)
		dname = xbmc.getInfoLabel("ListItem.FolderPath")
		print ("Dir name %s" % dname)
		xbmc.executebuiltin("RunScript(script.on.file,%s,%s,%s)" % ('unselect', fn, dname))
	else:
		print ("Unknown content, not calling script")
