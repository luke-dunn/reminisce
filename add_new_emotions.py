#!/usr/bin/python
import cgi
from pprint import pprint as pp
import cgitb; cgitb.enable()  # for troubleshooting
import Cookie
import os
import pickle
form = cgi.FieldStorage()
emotions = form.getvalue('emotions')
emotions = emotions.split('\r\n')
c = Cookie.SimpleCookie()
c.load(os.environ['HTTP_COOKIE'])
rememberer=str(c['username']).split('=')[1]

emotions_filename = rememberer.replace(' ','_')+'_emotions'
em=open(emotions_filename)
emotions_old = pickle.load(em)
em.close()
em=open(emotions_filename,'w')
emotions_old.extend(emotions)
pickle.dump(emotions_old,em)
em.close()

print "Content-type: text/html"
print
print '<html><head>'
print '<link rel="stylesheet" href="../b.css" type="text/css" />'

print '</head><body><div id="content">'
print '<p>new emotions added</p>'
print '<p><a href="index.py">my memories</a></p>'
print '</div></body></html>'
