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

places_filename = username+'_places'
emotions_filename = username+'_emotions'
years_filename = username+'_years'
mems_filename = username+'_mems'
phases_filename = username+'_phases'


pl=open(places_filename)
em=open(emotions_filename)
yr=open(years_filename)
me=open(mems_filename)
ph=open(phases_filename)

emotions = pickle.load(em)
places = pickle.load(pl)
years = pickle.load(yr)
memories = pickle.load(me)
phases = pickle.load(ph)


pl.close()
em.close()
yr.close()
me.close()
ph.close()

# ________________________________________________________

print '<html><head>'
print '<link rel="stylesheet" href="../b.css" type="text/css" />'
print '</head><body><div id="content"><form action="a.py" method="post"><table>'

dots = (str(x)+'.'+str(y)+'.'+str(z) for x in range(10) for y in range(10) for z in range(10))

for x in memories:
    num=dots.next()
    print'<tr><td> <input name="'+num+'" value="'+x+'" /></td><td><select name="'+num+'pl">'
    for plac in places:
        print '<option value="'+str(plac)+'"'
        if plac == memories[x]['place']:
            print ' selected="selected"'
        print '>'+str(plac)+'</option>\n'
    print '</select>'
    print '</td><td><select name="'+num+'e">'
    for emo in emotions:
        print '<option value="'+str(emo)+'"'
        if emo == memories[x]['emotion']:
            print ' selected="selected"'
        print '>'+str(emo)+'</option>\n'
    print '</select>'
    print '</td><td><select name="'+num+'yea">'
    for yea in years:
        print '<option value="'+str(yea)+'"'
        if str(yea) == memories[x]['year']:
            print ' selected="selected"'
        print '>'+str(yea)+'</option>\n'
    print '</select>'
    print '</td><td><select name="'+num+'phas">'
    for pha in phases:
        print '<option value="'+str(pha)+'"'
        if str(pha) == memories[x]['phase']:
            print ' selected="selected"'
        print '>'+str(pha)+'</option>\n'
    print '</select>'
    print '</td></tr>'
print '</table><input type="submit" value="Submit" /></form></div></body></html>'

