#!/usr/bin/python

import sys
import httplib2

def Scan(url):
	modules = file("drupal-modules.lst")
	h = httplib2.Http(disable_ssl_certificate_validation=True)
	h.follow_all_redirects = False
	
	for mod in modules:
		mod = mod.rstrip()
		# Check for license.txt
		licensurl = url+"/sites/all/modules/{}/LICENSE.txt".format(mod)
		resp, content = h.request(licensurl)
		#print resp["content-location"]
		#print licensurl
		if(resp.status == 200 and resp["content-location"] == licensurl):
			print mod
			#print resp
			continue
			
		# Check for 403 or other response than redirect or 404 for module folder
		folderurl = url+"/sites/all/modules/{}/".format(mod)
		resp, content = h.request(folderurl)
		if(resp.status == 200 and resp["content-location"] == folderurl):
			print mod
			continue
		
	


if __name__ == '__main__':
	if(len(sys.argv) < 2):
		print """
		USAGE: scanner.py <url>
		"""
		exit(0)
		
	Scan(sys.argv[1])
		
	
