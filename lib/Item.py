#!/usr/bin/env python
# coding=utf-8

import redis

class DB(object):
    def __init__(self, host='localhost', port=6379, db=0):
        self.pool = redis.ConnectionPool(host=host, port=port, db=db)
        self.r = redis.Redis(connection_pool=self.pool)

    def set(self, key, value, outtime=0):
        result = self.r.set(key, value)
        if outtime != 0:
            self.r.expire(key, outtime)
        return result

    def get(self, key):
        return self.r.get(key)

    def flushdb(self):
        return self.r.flushdb()

db = DB(host = 'localhost', port = 6379)


# item Base class
class Item(object):

    def __init__(self, id):
        self.db = db
        self.id = id

class Weapon(Item):
    def __init__(self, id):
        super(Weapon, self).__init__(id)
        # Prefix Item:{id}:{key}
        self.prefix = 'Item:{id}:'.format(id=id)

    # set redis
    def _set(self, key, value):
        return self.db.set(key, value)

    # get redis
    def _get(self, key):
        # compose key, prefix and key .like as Item:{id}:{key}
        key = '{prefix}{key}'.format(prefix=self.prefix, key=key)
        return key

    def name(self, value=None):
        key = '{prefix}name'.format(prefix=self.prefix)

        if value is None:
            return self.db.get(key)
        else:
            return self._set(key, value)
            #return self.db.set(key, value)

    def desc(self, value=None):
        if value is None:
            return self._get('desc')
            #return self.db.get('desc')
        else:
            return self._set('desc')
            #return self.db.set('{prefix}desc'.frmat(prefix=self.prefix))

    def attack(self, value=None):
        if value is None:
            return self.id


i1 = Weapon(1)

print(i1.desc())
