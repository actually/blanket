#!/usr/bin/env python
"""
Search Icinga Service Status Details

"""
import re
import sys
import requests 
from BeautifulSoup import BeautifulSoup

alert_arg = 'urlopen' 

try:
    import config
    r = requests.get(config.icinga_url, verify=False, auth=(config.username, config.password))
except:
    import getpass
    username = raw_input("Username: ")
    password = getpass.getpass()
    icinga_url = raw_input("URL to Icinga Service Status Details: ")
    r = requests.get(icinga_url, verify=False, auth=(username, password))

html = r.content
soup = BeautifulSoup(html)
found_alerts = []
nodenames = []

alerts = soup.findAll(text=re.compile(alert_arg))

for alert in alerts:
    found_alerts.append(alert.findPrevious('a'))

for item in found_alerts:
    node_string = str(item)
    if 'com&amp' in node_string:  
        start_of_node_string = node_string.find('srv=')
        start_of_node = start_of_node_string + 4                                                                                                                                                         
        end_of_node = node_string.find('" target')                                                                                                                                                
        just_the_node = node_string[start_of_node:end_of_node]                                                                                                                   
        nodenames.append(just_the_node)
        print just_the_node
       
#print ','.join(nodenames)
