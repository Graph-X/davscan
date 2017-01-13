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

class Client():	

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
    def get(self,s,u):
            headers = s.headers
            #set the translate and connection headers per kingcope's disclosure
       	    #HTTP request should look like this:
  	    #> GET / %c0%af/foo/bar/file.zip HTTP/1.1
	    #> Translate: f
	    #> Connection: Close
	    #> Host: <hostname>
	    headers.update({'Translate': 'f', 'Connection': 'close'})
	    r = s.request('GET', u, headers=headers)
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
    def propfind(self,s,u, headers=None):
	    headers = s.headers
            headers.update({"Content-Type": "application/xml"})
	    if 'Depth' not in headers.keys():
	        headers.update({'Depth': 'infinity'})
	    r = s.request('PROPFIND', u, headers=headers)

	    if r.status_code == 301:
		url = urlparse(r.headers['location'])
		return self.propfind(s,url.path)
            if r.status_code == 200 or r.status_code == 207:
    	        tree = xml.fromstring(r.content)
	        return [elem2file(elem) for elem in tree.findall('{DAV:}response')]
            if r.status_code == 403:
                #trying again with depth 1
                headers.update({'Depth': '1'})
                print("[!] 403 Forbidden status code returned. Adjusting Depth header...")
                return self.propfind(s,u,headers)
                
