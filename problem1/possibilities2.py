#!/usr/bin/python2

import enchant
from itertools import combinations
eng_dict = enchant.Dict("en_US")

with open("possibilities_clean", 'r') as possf:
    outf = open("possibilities2", 'w')

    # loop through every encrypted message
    for e in range(0, 11):
        outf.write(possf.readline())

        # for every pair there are 12 possibilities created
        poList = list()
        for po in range(0, 12):
            poList.append(possf.readline().strip())

        prevBreak = 0
        nextBreak = -1
        for msg in poList:
            #outf.write(str(poList))
            while msg.find('~') != -1:
                prevBreak = nextBreak+1
                nextBreak = msg.find('~')
                msg = msg[:nextBreak] + "_" + msg[nextBreak+1:]
                string = "" #msg[prevBreak:nextBreak]
                for msgp in poList:
                    string += msgp[prevBreak:nextBreak]
                length = nextBreak - prevBreak
                #print string
                #print length
                if length > 9:
                    continue 
                combs = list(combinations(string, nextBreak-prevBreak))
                for cs in combs:
                    s = ''.join(cs)
                    if len(s) and eng_dict.check(s):
                        outf.write(s+"/")

                outf.write("\n\n")
            outf.write("------------------------------------------------------------\n")#break
            prevBreak = 0
            nextBreak = -1
        break 
                    
    outf.close()
possf.close()
