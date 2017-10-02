#!/usr/bin/python2

with open("possibilities", 'r') as possf:
    outf = open("possibilities_clean", 'w')

    # loop through every encrypted message
    for e in range(0, 11):
        outf.write(possf.readline())

        # for every encrypted message there are 10 pairs
        poList1 = list()
        poList1.append(" ") # filler for logic
        poList2 = list()
        for pair in range(0, 10):
            # for every pair there are 12 possibilities created
            for po in range(0, 12):
                poList2.append(possf.readline())

            # keep longest pairs
            if len(poList1[0]) < len(poList2[0]):
                poList1 = list(poList2)
            del poList2[:]

        for msg in poList1:
            outf.write(msg)

    outf.close()
possf.close()
