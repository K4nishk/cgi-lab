#!/usr/bin/env python3
import cgi, cgitb
from templates import secret_page
import secret
import time

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
username = form.getvalue('username')
password = form.getvalue('password')

print("Content-Type: text/html\r\n\r\n")
# print("<p><b>Username</b> %s <b>password</b> %s</p>" % (username, password))
if secret.username == username and secret.password == password:
    print("<p>Set-Cookie: lastvisit=" + str(time.time()) + "</p>")
    print(secret_page(username, password))
