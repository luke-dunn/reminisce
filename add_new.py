#!/usr/bin/python
import cgi
from pprint import pprint as pp
import cgitb; cgitb.enable()  # for troubleshooting
import Cookie
import os
import pickle
form = cgi.FieldStorage()
memories = form.getvalue('memories')
memories = memories.split('\r\n')
c = Cookie.SimpleCookie()
c.load(os.environ['HTTP_COOKIE'])
rememberer=str(c['username']).split('=')[1]

def make_slots(x):
    slotlist=""
    for val in x:
        slotlist+='<option value="'+str(val)+'">'+str(val)+'</option>\n'
    slotlist+='</select>'
    return slotlist

places_filename = rememberer.replace(' ','_')+'_places'
emotions_filename = rememberer.replace(' ','_')+'_emotions'
years_filename = rememberer.replace(' ','_')+'_years'
phases_filename = rememberer.replace(' ','_')+'_phases'

pl=open(places_filename)
em=open(emotions_filename)
yr=open(years_filename)
ph=open(phases_filename)

places = pickle.load(pl)
emotions = pickle.load(em)
years = pickle.load(yr)
phases = pickle.load(ph)
pl.close()
em.close()
yr.close()
ph.close()

emotion_slots = make_slots(emotions)
place_slots = make_slots(places)
year_slots = make_slots(years)
phase_slots = make_slots(phases)




# ________________________________________________________
print "Content-type: text/html"
print
print '<html><head>'
print '<link rel="stylesheet" href="../b.css" type="text/css" />'
print '</head><body><div id="content"><form action="update_new_mems.py" method="post"><input name ="name" value="'+rememberer+'" /><br /><table>'

dots = (str(x)+'.'+str(y)+'.'+str(z) for x in range(10) for y in range(10) for z in range(10))

for x in memories:
    num=dots.next()
    print'<tr><td> <input name="'+num+'" value="'+x+'" /></td><td><select name="'+num+'pl">'+place_slots+'</td><td><select name="'+num+'e">'+ emotion_slots+'</td><td><select name="'+num+'yea">'+year_slots+'</td><td><select name="'+num+'phas">'+phase_slots+'</td></tr>'
print '</table><input type="submit" value="Submit" /></form></div></body></html>'

