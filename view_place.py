#!/usr/bin/python
import cgi
from pprint import pprint as pp
import cgitb; cgitb.enable()  # for troubleshooting
import Cookie
import os
import pickle
def make_slots(x):
    slotlist=""
    for val in x:
        slotlist+='<option value="'+str(val)+'">'+str(val)+'</option>\n'
    slotlist+='</select>'
    return slotlist

c = Cookie.SimpleCookie()
c.load(os.environ['HTTP_COOKIE'])
rememberer=str(c['username']).split('=')[1]
filename = rememberer.replace(' ','_')+'_places'
pl=open(filename)
places=pickle.load(pl)
place_slots = make_slots(places)
print "Content-type: text/html"
print
print '<html><head>'
print '<link rel="stylesheet" href="../b.css" type="text/css" />'

print '</head><body><div id="content">'
print """<form action="view_place_display.py" method="post">

<h3>select a place to view your memories by</h3>
<select name="place">"""+place_slots
print """<input type="submit" value="Submit" /></form>"""


print '<p><a href="index.py">my memories</a></p>'
print '</div></body></html>'
pl.close()

