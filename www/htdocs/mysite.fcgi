#!/usr/local/bin/python
import sys,os
#import logging

#logging.basicConfig(filename='../logs/e.log', level=logging.DEBUG)
#logger=logging.getLogger('mysite.fcig')

#sys.path.insert(0, "/usr/local/bin/python")
#cwd=os.getcwd()
#logger.debug("cwd=" + cwd)
#sys.path.insert(0, "/www/1764598789.host/ip469_com/htdocs")
#msg=""
#for p in sys.path:
#    msg = msg + p + ":"
#logger.debug("sys.path=" + msg)
#os.chdir("/www/1764598789.host/ip469_com/htdocs")

os.environ["DJANGO_SETTINGS_MODULE"]="ip469.settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
