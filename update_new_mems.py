#!/usr/bin/python
import cgi
from pprint import pprint as pp
import cgitb; cgitb.enable()  # for troubleshooting
import Cookie
import os
import pickle

form = cgi.FieldStorage()
d={}

c = Cookie.SimpleCookie()
c.load(os.environ['HTTP_COOKIE'])
rememberer=str(c['username']).split('=')[1]

print "Content-type: text/html"
print

for x in sorted(form.keys()):
    if len(x) == 5:
        label = form.getvalue(x)
        d[label] = {}
    if len(x) == 6:
        d[label]['emotion'] = form.getvalue(x)
    if len(x) == 7:
        d[label]['place'] = form.getvalue(x)
    if len(x) == 8:
        d[label]['year'] = form.getvalue(x)
    if len(x) == 9:
        d[label]['phase'] = form.getvalue(x)

mem_filename = rememberer.replace(' ','_')+'_mems'
old_mems = open(mem_filename)
oldies=pickle.load(old_mems)
old_mems.close()
mem_file = open(mem_filename,'w')
d.update(oldies)
pickle.dump(d,mem_file) 
mem_file.close()

print '<html><head>'
print '<link rel="stylesheet" href="../b.css" type="text/css" />'

print '</head><body><div id="content">'

print "hi,",rememberer

print "<h4>here are all your memories </h4><p>including the ones you just classified</p><table>"

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
print '<p>We have updated our database for you... Later you can access them, add to them and share them with others on the site.</p>'
print '<p><a href="index.py">my memories</a></p>'
print '</div></body></html>'


