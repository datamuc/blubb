#!./py/bin/python

from blubb import app as blubb

blubb.run(server='cherrypy', port=8280, host='0.0.0.0')
