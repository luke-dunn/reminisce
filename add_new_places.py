#!/usr/bin/python
import cgi
from pprint import pprint as pp
import cgitb; cgitb.enable()  # for troubleshooting
import Cookie
import os
import pickle
form = cgi.FieldStorage()
places = form.getvalue('places')
places = places.split('\r\n')
c = Cookie.SimpleCookie()
c.load(os.environ['HTTP_COOKIE'])
rememberer=str(c['username']).split('=')[1]

places_filename = rememberer.replace(' ','_')+'_places'
pl=open(places_filename)
places_old = pickle.load(pl)
pl.close()
pl=open(places_filename,'w')
places_old.extend(places)
pickle.dump(places_old,pl)
pl.close()

print "Content-type: text/html"
print
print '<html><head>'
print '<link rel="stylesheet" href="../b.css" type="text/css" />'

print '</head><body><div id="content">'
print '<p>new places added</p>'
print '<p><a href="index.py">my memories</a></p>'
print '</div></body></html>'
