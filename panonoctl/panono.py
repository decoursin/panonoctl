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

import websocket
import json

class panono:

    def __init__(self, ip="192.168.80.80", port="12345", path="8086"):
        self.ip     = ip
        self.port   = port
        self.path   = path
        self.ws     = None
        self.count  = 1

    def connect(self):
        self.ws = websocket.create_connection("ws://" + self.ip + ":" + self.port + "/" + self.path)
        return

    def askForUpfs(self):
        upf = []
        self.ws.send("{\"id\":"+str(self.count)+",\"method\":\"get_upf_infos\",\"jsonrpc\":\"2.0\"}")
        self.count = self.count + 1
        response = self.ws.recv()
        rep = json.loads(response)
        for key in rep:
            if key == "result":
                for captures in rep["result"]["upf_infos"]:
                    for capture in captures:
                        upf.append(captures['upf_url'])
        return upf

    def deleteUpf(self, upf=None):
        self.ws.send("{\"id\":"+str(self.count)+",\"method\":\"delete_upf\",\"params\":{\"image_id\":\""+str(upf)+"\"},\"jsonrpc\":\"2.0\"}")
        self.count = self.count + 1
        response = self.ws.recv()
        rep = json.loads(response)
        return rep

    def getStatus(self):
        self.ws.send("{\"id\":"+str(self.count)+",\"method\":\"get_status\",\"jsonrpc\":\"2.0\"}")
        self.count = self.count + 1
        response = self.ws.recv()
        rep = json.loads(response)
        return rep

    def getOptions(self):
        self.ws.send("{\"id\":"+str(self.count)+",\"method\":\"get_options\",\"jsonrpc\":\"2.0\"}")
        self.count = self.count + 1
        response = self.ws.recv()
        rep = json.loads(response)
        return rep

    def capture(self):
        self.ws.send("{\"id\":"+str(self.count)+",\"method\":\"capture\",\"jsonrpc\":\"2.0\"}")
        self.count = self.count + 1
        response = self.ws.recv()
        rep = json.loads(response)
        return rep

    def __auth(self):
        self.ws.send("{\"id\":"+str(self.count)+",\"method\":\"auth\",\"params\":{\"device\":\"test\",\"force\":true},\"jsonrpc\":\"2.0\"}")
        self.count = self.count + 1
        response = self.ws.recv()
        rep = json.loads(response)
        return rep

    def __getAuthToken(self):
        self.ws.send("{\"id\":"+str(self.count)+",\"method\":\"get_auth_token\",\"params\":{\"device\":\"test\",\"force\":true},\"jsonrpc\":\"2.0\"}")
        self.count = self.count + 1
        response = self.ws.recv()
        rep = json.loads(response)
        return rep
