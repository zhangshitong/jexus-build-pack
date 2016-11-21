#!/usr/bin/env python
import sys,os, shutil
import re
portPattern = re.compile("port=")
rootPattern = re.compile("root=")

def get_root():
	root = os.getcwd()
	return root

def get_port():
	port = os.getenv("PORT")
	return port

def get_jexus_conf(root_path):
	os.path.join(root_path, 'jexus_build_pack/jexus/siteconf/default');


def get_app_web_path(root_path):
	os.path.join(root_path, 'jexus_b_sites');


def change_conf_file(root_path, port, app_path):
	jexus_conf_file = get_jexus_conf(root_path);
	conf_file = os.open(jexus_conf_file);
	jexus_conf_over = os.path.join(root_path, 'default');
	conf_file_over = os.open(jexus_conf_over, "w");
	content = conf_file.readlines()
	for line in content:
		if portPattern.search(line):
			line = 'port='+ port;
			print "replace port compete~~~~"
		elif rootPattern.search(line):
			line = 'root=' + app_path;
		conf_file_over.write(line+"\n")
	conf_file.close()
	conf_file_over.close()
	shutil.move(jexus_conf_over, jexus_conf_file)

def main():
	port=get_port()
	print "get port complete~~"
	root = get_root()
	print "get root compelet~~~"
	app_path = get_app_web_path(root);
	print "get app_path compelet~~~"
	change_conf_file(root,port, app_path)

main()


