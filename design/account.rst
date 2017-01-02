===================================
Redis Game database design document
===================================

-------
account
-------

- account:count id
- account:userlist set(id)
- account:email:[email] id
- account:[id]:version number
- account:[id]:email string
- account:[id]:password string // md5(password..salt)
- account:[id]:nickname string
- account:[id]:lastlogin hashes
  - account:[id]:lastlogin:ip string
  - account:[id]:lastlogin:time string
- account:[id]:history list(string)
- account:[id]:avaliable enum(open/locked/delete)
