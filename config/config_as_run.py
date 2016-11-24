#!/usr/bin/env python
import sys,os, shutil

def get_root():
	if(len(sys.argv) > 1):
		root = sys.argv[1]
	else:
		root = os.getcwd()
	print "------------->";
	print "get root %s \n" % root;
	return root

def get_port():
	port = os.getenv("PORT")
	if port == None:
		port = '8082';
	print "------------->";
	print 'get_port: %s \n' % port;
	return port

def get_jexus_conf(root_path):
	return os.path.join(root_path, ".jexus_build_pack/jexus/siteconf/default");



def get_app_web_path(root_path):
	return root_path;
	# return os.path.join(root_path, 'jexus_b_sites');


def change_conf_file(root_path, port, app_path):
	jexus_conf_file = get_jexus_conf(root_path);
	print "------------->";
	print 'open file %s \n' % jexus_conf_file
	conf_file = open(jexus_conf_file,"r");
	jexus_conf_over = os.path.join(root_path, 'default');
	conf_file_over = open(jexus_conf_over, "w");
	content = conf_file.readlines()
	for line in content:
		# print  'read line: %s' % line;
		if line.startswith('port='):
			line = 'port='+ port + '\n';
			print "------------->";
			print "replace port compete: %s \n" % line;
		elif line.startswith('root='):
			line = 'root=' + app_path +'\n';
			print "------------->";
			print "replace web root compete: %s \n" % line;
		conf_file_over.write(line)
	conf_file.close()
	conf_file_over.close()
	shutil.move(jexus_conf_over, jexus_conf_file)

def main():
	port=get_port()
	print "------------->";
	print "get port complete \n"
	root = get_root()
	print "------------->";
	print "get root compelet\n"
	app_path = get_app_web_path(root);
	print "------------->";
	print "get app_path compelet \n"
	change_conf_file(root,port, app_path)

main()


