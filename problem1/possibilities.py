#!/usr/bin/python2

# e t a o i n s r h l d c
# found in around 80% of the words in the English language.
letters = ['e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'l', 'd', 'c']

possibilities = dict()
with open("encrypted_msgs", 'r') as ef:
    outf = open("possibilities", 'w')
    msgs = []
    # build list of all encrypted messages
    for msg in ef:
       msgs.append(msg.strip())

    # process all encrypted messages
    for x in range(0, len(msgs)):
        #print x
        outf.write("POSSIBILITES FOR MSG {}\n".format(x))
        msg1 = msgs[x].decode("hex")
        msg1p = ""
        l1 = len(msg1)
        
        # messages that will be paired with current message being process
        for y in range(0, len(msgs)):
            # skip same index
            if x == y:
                continue
            # 
            msg2 = msgs[y].decode("hex")
            msg2p = ""
            l2 = len(msg2)
            # go through common letters
            for letter in letters:
                # will assume all letters in msg2 is letter
                # xor will zero out letter and leave just key
                # will then xor with msg1 to zero out key and leave just msg1
                for i in range(0, l2):
                    # for first letters assume capital
                    if i == 0:
                        msg2p += chr(ord(msg2[i]) ^ (ord(letter)-0x20))
                    else:
                        msg2p += chr(ord(msg2[i]) ^ ord(letter))
                l = 0
                if l1 <= l2:
                    l = l1
                else:
                    l = l2
                #print l, l1, l2
                #print len(msg1)
                for j in range(0, l):
                    msg1p += chr(ord(msg1[j]) ^ ord(msg2p[j]))
                
                # loop through message 1 and if anything is within range
                # of ascii alphaber mark is as a possibility, else mark as _
                for z in range(0, l):
                    
                    if ord(msg1p[z]) >= 0x41 and ord(msg1p[z]) <= 0x5a:
                        #possibilities[z] = msg1p[z]
                        outf.write(msg1p[z])
                    elif ord(msg1p[z]) >= 0x61 and ord(msg1p[z]) <= 0x7a:
                        #possibilities[z] = msg1p[z]
                        outf.write(msg1p[z])
                    elif ord(msg1p[z]) == 0x20:
                        outf.write(msg1p[z])
                    
                    #if ord(msg1p[z]) >= 0x20 and ord(msg1p[z]) < 0x7E:
                        #outf.write(msg1p[z])
                    else:
                        #possibilities[z] = "~"
                        outf.write("~")

                outf.write("\n")
                msg1p = ""
                msg2p = ""

    outf.close()
ef.close()

