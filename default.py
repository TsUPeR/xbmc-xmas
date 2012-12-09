"""
 Copyright (c) 2010, 2011, 2012 Popeye

 Permission is hereby granted, free of charge, to any person
 obtaining a copy of this software and associated documentation
 files (the "Software"), to deal in the Software without
 restriction, including without limitation the rights to use,
 copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the
 Software is furnished to do so, subject to the following
 conditions:

 The above copyright notice and this permission notice shall be
 included in all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
"""

import xbmcaddon
import xbmcgui

import datetime

__settings__ = xbmcaddon.Addon(id='plugin.audio.bjallerklang')
__language__ = __settings__.getLocalizedString

URL = "rtmp://rtmp-live.sr.se/webbradio/kanaler/srextra12-aac-192"

if (__name__ == "__main__" ):
    the_end = datetime.datetime(2012, 12, 28, 23, 59)
    
    if datetime.datetime.now() < the_end:
        listitem=xbmcgui.ListItem(__language__(32000), iconImage="icon.png")
        listitem.setInfo(type="Audio", infoLabels=[{'title':'%s' % __language__(32000)}])
        listitem.setProperty("Fanart_Image", "fanart.jpg")
        listitem.setProperty('IsPlayable', "True")
        listitem.setProperty('IsLive', "True")
        listitem.setPath(URL)
        xbmc.Player().play(URL, listitem)
    else:
        xbmcgui.Dialog().ok(__language__(32000), __language__(32001))
