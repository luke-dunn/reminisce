#!/usr/bin/python
import cgi
from pprint import pprint as pp
import cgitb; cgitb.enable()  # for troubleshooting
import Cookie
import os
import pickle

c = Cookie.SimpleCookie()
c.load(os.environ['HTTP_COOKIE'])
rememberer=str(c['username']).split('=')[1]
filename = rememberer.replace(' ','_')+'_mems'
mems=open(filename)
d=pickle.load(mems)
print "Content-type: text/html"
print
print '<html><head>'
print '<link rel="stylesheet" href="../b.css" type="text/css" />'

print '</head><body><div id="content">'
print "<h4>here are your memories</h4><table>"

print '<tr><th><strong>memory</strong></th><th><strong>place</strong></th><th><strong>emotion</strong></th><th><strong>date</strong></th><th><strong>phase</strong></th></tr>'
counter =0
for x in d:
    if counter % 2 ==1:
        print '<tr>'
    else:
        print '<tr class="a">'
    counter+=1
    print '<td>'+x+'</td>'
    print '<td>'+d[x]['place']+'</td>'
    print '<td>'+d[x]['emotion']+'</td>'
    print '<td>'+d[x]['year']+'</td>'
    print '<td>'+d[x]['phase']+'</td>'
    print '</tr>'
print '</table><br /><br />'
print '<p><a href="index.py">my memories</a></p>'
print '</div></body></html>'
mems.close()

