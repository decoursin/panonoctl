# Copyright 2016 Florian Lehner. All rights reserved.
#
# The contents of this file are licensed under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with the
# License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

import socket

class ssdpNotify:
    @staticmethod
    def discover(self):
        print "discover"
        ip = None
        port = None
        path = None
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(7)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('',1900))
        sock.sendto("M-SEARCH * HTTP/1.1\r\nMX: 10\r\nHOST: 239.255.255.250:1900\r\nMAN: \"ssdp:discover\"\r\nNT: panono:ball-camera\r\n\r\n", ('239.255.255.250', 1900))
        while True:
            print "."
            try:
                data, addr = sock.recvfrom(1024)#.decode('utf-8')
                print data
            except socket.error as e:
                print e
                break
        sock.close()
        return (ip, port, path)
