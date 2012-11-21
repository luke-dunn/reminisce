#!/usr/bin/python
import cgi
from pprint import pprint as pp
import cgitb; cgitb.enable()  # for troubleshooting
import Cookie
import os
import pickle
form = cgi.FieldStorage()
phases = form.getvalue('phases')
phases = phases.split('\r\n')
c = Cookie.SimpleCookie()
c.load(os.environ['HTTP_COOKIE'])
rememberer=str(c['username']).split('=')[1]

phases_filename = rememberer.replace(' ','_')+'_phases'
ph=open(phases_filename)
phases_old = pickle.load(ph)
ph.close()
ph=open(phases_filename,'w')
phases_old.extend(phases)
pickle.dump(phases_old,ph)
ph.close()

print "Content-type: text/html"
print
print '<html><head>'
print '<link rel="stylesheet" href="../b.css" type="text/css" />'

print '</head><body><div id="content">'
print '<p>new phases added</p>'
print '<p><a href="index.py">my memories</a></p>'
print '</div></body></html>'
