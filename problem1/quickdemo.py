#!/usr/bin/python2

import sys

with open("encrypted_msgs", 'r') as re:
    re.readline()
    re.readline()
    re.readline()
    re.readline()
    re.readline()
    m1 = re.readline().strip()
    m2 = re.readline().strip()

    key = ""
    for x in range(0, 12):
        key_g = 0
        while chr(ord(m1[x]) ^ key_g) != chr(ord(m2[x]) ^ key_g):
            if key_g > 0xff:
                print "No"
                exit()
            key_g += 1

        key += chr(key_g)
        print key.encode("hex")
re.close()
