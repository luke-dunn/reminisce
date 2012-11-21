#!/usr/bin/python

import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import Cookie,os
c = Cookie.SimpleCookie()
if 'HTTP_COOKIE' in os.environ:
    c.load(os.environ['HTTP_COOKIE'])
    rememberer=str(c['username']).split('=')[1]
    from templates import known
    known = known.replace('**rememberer**',rememberer)
    print known
else:
    from templates import get_rememberer
    print get_rememberer
