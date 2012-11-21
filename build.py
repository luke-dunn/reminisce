#!/usr/bin/python
import cgi
from pprint import pprint as pp
import cgitb; cgitb.enable()  # for troubleshooting
import pickle

print "Content-type: text/html"
print
 
form = cgi.FieldStorage()
from ident import rememberer
username = rememberer.replace(' ','_')

emotions = form.getvalue('emotions')
places = form.getvalue('places')
birthyear = form.getvalue('birthyear')
years = range(int(birthyear),2013)
memories = form.getvalue('memories')
phases = form.getvalue('phases')

places_filename = username+'_places'
emotions_filename = username+'_emotions'
years_filename = username+'_years'
phases_filename = username+'_phases'

pl=open(places_filename,'w')
em=open(emotions_filename,'w')
yr=open(years_filename,'w')
ph=open(phases_filename,'w')

emotions = emotions.split('\r\n')
places = places.split('\r\n')
phases = phases.split('\r\n')
memories = memories.split('\r\n')

pickle.dump(places,pl)
pickle.dump(emotions,em)
pickle.dump(years,yr)
pickle.dump(phases,ph)

pl.close()
em.close()
yr.close()
ph.close()





def make_slots(x):
    slotlist=""
    for val in x:
        slotlist+='<option value="'+str(val)+'">'+str(val)+'</option>\n'
    slotlist+='</select>'
    return slotlist
    
emotion_slots = make_slots(emotions)
place_slots = make_slots(places)
year_slots = make_slots(years)
phase_slots = make_slots(phases)



# ________________________________________________________

print '<html><head>'
print '<link rel="stylesheet" href="../b.css" type="text/css" />'
print '</head><body><div id="content"><form action="a.py" method="post"><table>'

dots = (str(x)+'.'+str(y)+'.'+str(z) for x in range(10) for y in range(10) for z in range(10))

for x in memories:
    num=dots.next()
    print'<tr><td> <input name="'+num+'" value="'+x+'" /></td><td><select name="'+num+'pl">'+place_slots+'</td><td><select name="'+num+'e">'+ emotion_slots+'</td><td><select name="'+num+'yea">'+year_slots+'</td><td><select name="'+num+'phas">'+phase_slots+'</td></tr>'
print '</table><input type="submit" value="Submit" /></form></div></body></html>'

