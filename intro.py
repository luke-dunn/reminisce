#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
from ident import rememberer
usrs = open('users')
import pickle
users=pickle.load(usrs)
usrs.close()
if rememberer in users:
    from templates import known
    known=known.replace('**rememberer**',rememberer)
    print known
else:
    users.append(rememberer)
    usrs=open('users','w')
    pickle.dump(users,usrs)
    usrs.close()
    from templates import welcome
    welcome=welcome.replace('**rememberer**',rememberer)
    print welcome
