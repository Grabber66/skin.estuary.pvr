import xbmc
import xbmcgui

home = xbmcgui.Window(10000)
skin = home.getProperty("CurrentSkin")
if skin == "skin.estuary.pvr":
    xbmc.executebuiltin("SetFocus(8000)")
else:
    pass 
