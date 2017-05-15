#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gnupg 
import ConfigParser, os, sys
import pprint, re

pp = pprint.PrettyPrinter(indent=4)
verbose = True

# psuedo code
# * parse config
# * setup gpg

me = sys.argv[0]
basename= re.search('./(.*).py', me, re.IGNORECASE).group(1)

config = ConfigParser.ConfigParser()
personalconfig  = os.path.expanduser('~/' + basename + '.ini' )
thisdir = basename + '.ini' 

readconfig = config.read([personalconfig,thisdir])

print 'this is Read config file '
pp.pprint ( readconfig )

# print 'Read config file ' + readconfig + '\n'

homedir = "/home/dthornton/.gnupg"
gpgverboseflag = True


print "Home is "
print os.environ['HOME']

if ( os.path.isdir(homedir) ) :
	print homedir + " exists"
else:
	sys.exit(0)

gpg = gnupg.GPG(gnupghome=homedir,use_agent=True,verbose=gpgverboseflag)

public_keys = gpg.list_keys() # same as gpg.list_keys(False)
private_keys = gpg.list_keys(True) # True => private keys


pp.pprint(public_keys)
pp.pprint(private_keys)
