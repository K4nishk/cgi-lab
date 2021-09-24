#!/usr/bin/env python3
import os, cgi, cgitb
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
# if secret.username == username and secret.password == password:
#     print("<p>Set-Cookie: lastvisit=" + str(time.time()) + "</p>")
#     print(secret_page(username, password))

# print(os.environ["HTTP_COOKIE"])
cookies = os.environ["HTTP_COOKIE"].split(";")
uname = cookies[0].strip().split("=")[1]
pwd = cookies[1].strip().split("=")[1]

if secret.username == uname and secret.password == pwd:
    print(secret_page(uname, pwd))