#!/usr/bin/python
import cgi
from pprint import pprint as pp
import cgitb; cgitb.enable()  # for troubleshooting
import Cookie
import os
import pickle
import random,datetime
form = cgi.FieldStorage()

name = form.getvalue('name')

c = Cookie.SimpleCookie()
c['username']=name
c['session'] = random.randint(1,1000000000)
expiration = datetime.datetime.now() + datetime.timedelta(days=30)
c['session']['expires']=expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST")
print c

from templates import new_rememberer
print new_rememberer
