#!/usr/bin/env python
import sys,os
import re
pattern = re.compile("\"8080\"")
def get_root():
	root = os.getcwd()
	return root

def get_port():
	port = os.getenv("PORT")
	return port

def change_xml(root,port):
	file_config=open(root+"/.tongweb_buildpack/tongweb5/config/twns.xml","r")
	file_config_over=open(root+"/twns.xml","w")
	content = file_config.readlines()
	for line in content:
		if pattern.search(line):
			line = pattern.sub("\""+port+"\"",line)
			print "replace compete~~~~"
		file_config_over.write(line+"\n")
	file_config.close()
	file_config_over.close()

def main():
	port=get_port()
	print "get port complete~~"
	root = get_root()
	print "get root compelet~~~"
	change_xml(root,port)
	os.system("mv -f "+root+"/twns.xml "+root+"/.tongweb_buildpack/tongweb5/config/")


main()


