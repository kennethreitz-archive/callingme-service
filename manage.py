#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flaskext.script import Manager

from rush import app

manager = Manager(app)

# @manager.command
# def inbox(addr, port):
#     from fedex.emaild import inbox

#     inbox.serve(int(port), addr)

if __name__ == "__main__":
    manager.run()