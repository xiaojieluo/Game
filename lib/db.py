#!/usr/bin/env python
# coding=utf-8

import redis

class DB(object):

    def __init__(self, host='127.0.0.1', port=6379, db='game'):
        self.r = redis.Redis(host=host, port=port)

    def set(self, key, value):
        return self.r.set(key, value)


db = DB()
db.set('hello', 'world')
print(db.r.keys())
