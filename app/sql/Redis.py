import redis

# pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
# r = redis.Redis(host='localhost', port=6379, decode_responses=True)  
# r.set('name', 'runoob')  # 设置 name 对应的值
# print(r['name'])
# print(r.get('name'))  # 取出键 name 对应的值
# print(type(r.get('name')))  # 查看类型
# # class myRedis(object):
# #     pass

class myRedis(object):
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
    r = redis.Redis(host='localhost', port=6379, decode_responses=True) 

    @classmethod
    def get_state(cls):
        return cls.pool is not None and cls.r is not None   

    @classmethod
    def insertOne(cls,name,data):
        if cls.get_state():
            cls.r.hmset(name,data)
        else:
            return ""
    
    @classmethod
    def findOne(cls,name):
        if cls.get_state():
            return cls.r.hgetall(name)
        else:
            return ""
    
    @classmethod
    def findMany(cls,start):
        data = []
        if cls.get_state():
            for i in range(start, start+12):
                data.append(cls.r.hgetall(i))
            return data
        else:
            return ""

    @classmethod
    def findAll(cls):
        data = []
        if cls.get_state():
            for i in range(0, 144):
                data.append(cls.r.hgetall(i))
            return data
        else:
            return ""

    @classmethod
    def expire_key(cls,key,time):
        if cls.get_state():
            return cls.r.expire(key,time)
        else:
            return ""
    
    @classmethod
    def timeLeft(cls,key):
        if cls.get_state():
            return cls.r.ttl(key)
        else:
            return ""

    