#!/usr/bin/python

from panonoctl import panono
import urllib2
import os

cam = panono.panono()
cam.connect()

print(cam.auth())

print(cam.getStatus())

upfs = cam.getUpfs()
for i in upfs['result']['upf_infos']:
    print i['upf_url']
    attempts = 0
    while attempts < 3:
        try:
            response = urllib2.urlopen(i['upf_url'])
            content = response.read()
            f = open(os.path.basename(i['upf_url']), 'w')
            f.write(content)
            f.close()
            break
        except:
            attempts += 1

cam.disconnect()
