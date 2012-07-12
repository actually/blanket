#!/usr/bin/env python
"""
Search Icinga Service Status Details

Usage:
    ./get_alert_hosts.py "Disk Usage"
        - Returns csv list of hostnames

    $ fab -H $(./get_alert_hosts.py "Puppet client status") fix_puppet
        - Uses fabric to execute fix_puppet across listed hosts in icinga
"""
import re
import sys
import requests 
from BeautifulSoup import BeautifulSoup

try:
    alert_arg = sys.argv[1]
except:
    print "Please enter a valid alert to search for"
    print "example: 'Puppet client status'"
    exit()

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
hostnames = []

alerts = soup.findAll(text=re.compile(alert_arg))

for alert in alerts:
    found_alerts.append(alert.findPrevious('a'))

for item in found_alerts:
    host_string = str(item)
    if 'com&amp' in host_string:                                                                                                                                                           
        end_of_host = host_string.index('com&amp')                                                                                                                                                
        just_the_host = host_string[37:end_of_host] + "com"                                                                                                                   
        hostnames.append(just_the_host)
       
print ','.join(hostnames)
