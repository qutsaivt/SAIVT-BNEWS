#!/usr/bin/env python
import os.path
import os
import fnmatch
import urllib
import time
import random

def find_meta(path):
    for f in os.listdir(path):
        p = os.path.join(path,f)
        if os.path.isdir(p):
            for sp in find_meta(p):
                yield sp
        elif fnmatch.fnmatch(f,'*.mp4.txt'):
            yield p

# find all metadata files (*.txt in directories under grandparent directory of this file)
for metafile in find_meta(os.path.join(os.path.dirname(__file__),'..')):
    meta = dict([[s.strip() for s in l.split(':',1)] for l in open(metafile) if l.strip()])
    media = meta['media_content']
    videoout = metafile.replace('.txt','')

    if os.path.exists(videoout):
        print "Video {} already downloaded.".format(videoout)
    else:
        wait = 5.0 + random.random()*5 # sleep between 5 and 10 seconds
        print "  (waiting for {} seconds before contacting server)".format(wait)
        time.sleep(wait)

        print "Downloading {} to {} ...".format(media,videoout)
        
        urllib.urlretrieve(media,videoout + '.part')

        os.rename(videoout + '.part',videoout)

        print " ... done!"

