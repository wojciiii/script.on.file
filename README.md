# script.on.file

This simple projects implements two Kodi addins which allows one to run a script with selected media/directory as argument. 
<pre>

[context.on.file] --> [script.on.file] --> [onkodiselection.sh]
                                        |
                kodi                    |         linux shell
</pre>

This can be used to do anything you want. I use this to create a regex used to ignore certain media files on my NAS by calling another script trough SSH.

<pre>
                                                                  ssh
[context.on.file] --> [script.on.file] --> [onkodiselection.sh] ------> some_script.sh
                                        |                          |
                kodi                    |         linux shell      | linux shell on another host
</pre>

## Kodi Addin: script.on.file

This Kodi script resolves the directory "~/kodi" on the computer which runs Kodi and executes "onkodiselection.sh" with the provided arguments:
- filename as the first argument to this script
- directory as the second argument to this script

## Kodi Addin: context.on.file

This Kodi addin adds an additional context menu "Run Shell Command".

When the user selects something and presses context menu key on remote (or right mouse button) it show this menu and calls executes the script.on.file with filename/directory as parameters.

I used this to get the filename and directory in this addin.
<pre>
	if xbmc.getCondVisibility("Container.Content(files)"):
		fn=xbmc.getInfoLabel("ListItem.FileName")
		print ("Filename %s" % fn)
		dname = xbmc.getInfoLabel("ListItem.FolderPath")
		print ("Dir name %s" % dname)
		xbmc.executebuiltin("RunScript(script.on.file,%s,%s)" % (fn, dname))
	else:
		print ("Unknown content, not calling script")
</pre>

It looks like this works on Kodi 15.2 (ubuntu) but not on a later version of Kodi. To make it work remove the if statement and just assume that one can always get the file.

By the way this Kodi interface is terrible. Why would I give a function call encoded as a string as argument to another Python function? This is just beyond fucked up.

## A Word on Copyright

I used other plugins to get inspired. For example the Kodi Hello World plugin/script and also Trakt - Contextmenu.
I bluntly copy/pasted parts of the plugins to create this one.
