import os
import urllib2

def check_in():

    fqn = os.uname()[1]
    ext_ip = urllib2.urlopen('http://whatismyip.org').read()
    print ("\nAsset: %s " % fqn , "\n Checking in from IP#: %s " % ext_ip)
    
check_in()    
