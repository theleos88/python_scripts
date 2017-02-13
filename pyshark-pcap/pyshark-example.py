import pyshark
import signal
import os
import string

counter=0
ipcounter=0
tcpcounter=0
udpcounter=0

filename='/home/leos/Dropbox/work/vpp_fdio/VPP_SVN/datasets/smia2012central.cap'

cap = pyshark.FileCapture(filename)

i=0

for packet in cap:

    if 'ip' not in packet:
        print "OTHER"
        print packet.eth.src, packet.eth.dst.int_value
    else:
        print "Ip packet here"

    #for a in packet:
    #    print a

    if packet.transport_layer == 'TCP':


        ip = None
        #ip_version = get_ip_version(packet)
        #if ip_version == 4:
        ip = packet.ip
        #elif ip_version == 6:
        #    ip = packet.ipv6
        print 'Packet %d' % i
        print 'Source IP        -', ip.src.int_value
        print 'Source port      -', packet.tcp.srcport
        print 'Destination IP   -', ip.dst
        print 'Destination port -', packet.tcp.dstport
        print
    i += 1

    print packet.length # Packet length

    if i> 10:
        break
