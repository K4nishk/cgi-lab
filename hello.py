#!/usr/bin/env python3
import os, json, cgi
from templates import login_page, secret_page

#Q1
print("Content-Type: text/html\r\n\r\n")
print()
# print(os.environ)
# json_object = json.dumps(dict(os.environ), indent = 4)
# print(json_object)

# #Q2
# for param in os.environ.keys():
# 	if (param == "QUERY_STRING"):
# 		print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))

# #Q3
# for param in os.environ.keys():
# 	if (param == "HTTP_USER_AGENT"):
# 		print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))

#Q4
print(login_page())
