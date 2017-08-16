#!/usr/bin/env python
# coding=utf-8
#
# soaplib - Copyright (C) 2009 Aaron Bickell, Jamie Kirkpatrick
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
#

from soaplib.service import rpc
from soaplib.service import DefinitionBase
from soaplib.serializers.primitive import String, Integer
from wsgiref.simple_server import make_server

from soaplib.wsgi import Application
import json
import multiprocessing
import time

'''
This is a simple HelloWorld example to show the basics of writing
a webservice using soaplib, starting a server, and creating a service
client.
'''


class HelloWorldService(DefinitionBase):
    @rpc(String, _returns=String)
    def sayHello(self, name):
        '''
        Docstrings for service methods appear as documentation in the wsdl
        <b>what fun</b>
        @param name the name to say hello to
        @param the number of times to say hello
        @return the completed array
        '''
        results = 'Hello,%s' % name
        return results

    @rpc(String, _returns=String)
    def hello_name(self, name):
        result = 'Hello,%s' % name
        return result

    @rpc(String, _returns=String)
    def hello_json(self, name):
        result = {'name': name}
        return json.dumps(result)

    # 暂未完成
    @rpc(String, _returns=String)
    def checkSoftStatus(self, task_obj_str):
        return "this method is not complete"


class ServerHelp:
    server = make_server('localhost', 7789, Application([HelloWorldService], 'tns'))

    def run_server(self):
        print 'listen 127.0.0.1:7789'
        self.server.serve_forever()
        pass

    def stop_server(self):
        self.server.shutdown()
        print 'stop server'


if __name__ == '__main__':
    try:
        print 'start server'
        server = make_server('localhost', 7799, Application([HelloWorldService], 'tns'))
        server.serve_forever()

    except ImportError:
        print "Error: example server code requires Python >= 2.5"
