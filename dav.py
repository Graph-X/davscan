# -*- coding: utf-8 -*- 
############################################################################
#
#  dav.py is part of davscan
#  I straight up jackmoved a metric fuck ton of this code from 
#  the easywebdav project on github. If I thought I could get away
#  with it I wouldn't have said shit. Since it's actually a popular
#  library, you should probably go check it out and give dude props.
#  https://github.com/amnong/easywebdav
#
###########################################################################
import requests
import platform
from numbers import Number
import xml.etree.cElementTree as xml
from collections import namedtuple

File = namedtuple('File', ['name', 'size', 'status', 'contenttype'])

def prop(elem, name, default=None):
    child = elem.find('.//{DAV:}' + name)
    return default if child is None else child.text

	
def elem2file(elem):
    return File(
        prop(elem, 'href'),
        int(prop(elem, 'getcontentlength', 0)),
        prop(elem, 'status', ''),
        prop(elem, 'getcontenttype', ''),
    )
	
class Client:

    def __init__(self, session):
        self.session = session

    ############################################################
    # get function:
    #	Uses the url that's passed to it and makes a get request
    #	to the server, and then returns the r as the request
    #	response.
    #
    #	Requires "u" as the url to make the get request against
    #
    #	Optional: "headers" as dict for request headers
	#
	#	Returns "r" as the request response
	#############################################################
	def get(self, u,):
                self.headers = self.session.headers
		#set the translate and connection headers per kingcope's disclosure
		#HTTP request should look like this:
		#> GET / %c0%af/foo/bar/file.zip HTTP/1.1
		#> Translate: f
		#> Connection: Close
		#> Host: <hostname>
		self.headers.update = {'Translate': 'f', 'Connection': 'close'}
		r = self.session.request('GET', u, headers=self.headers)
		return r
		
	##############################################################
	# propfind function:
	#   Uses the url that's passed to it and makes a propfind 
	#   request to the server, and then returst the r as the 
	#   request response.
	#
	#   Requires "u" as the url to make the propfind request
	#
	#   Optional "headers" as dict list of headers
	#
	#   Returns "r" as the request response
	################################################################
	def propfind(self,u):
		self.headers = self.session.headers
		if 'Depth' not in self.headers.keys():
				self.headers.update({'Depth': 'infinity'})
		r = self.session.request('PROPFIND', u, headers=self.headers)

		if r.status_code == 301:
			url = urlparse(r.headers['location'])
			return self.propfind(url.path)

		tree = xml.fromstring(r.content)
		return [elem2file(elem) for elem in tree.findall('{DAV:}response')]
