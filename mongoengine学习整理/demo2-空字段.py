#!/usr/bin/env python
# coding=utf-8

#测试空字段插入到数据里的是什么样子
from mongoengine import *

class TestNull(Document):
    _id = StringField()
    a = StringField()
    b = StringField()
    id = ObjectIdField

#测试直插入1个字段，另一个字段不插，数据库里只有一个字段，且打印未插入的字段为None
def test_no_inesrt():
    t0 = TestNull(a="a")
    t = t0.save()
    print t.b   #None

#同直插入1个字段的效果
def test_insert_none():
    t0 = TestNull(a="a",b=None)
    t = t0.save()
    print t.to_json() #{"_id": {"$oid": "587f26a0540b6227a0acef09"}, "a": "a"}
    print t.b  # None
    #print t._auto_id_field  #True  估计意思是自动填充id
    print t.id  # 返回自动生成的id，属性名为id  不是 _id 但转换为字典之后，会变成 _id  ,在model里存在_id属性的时候，
                # 插入式 _id属性给None  数据库中实际存在_id，但无法通过id属性或者_id属性获取到id
    print t._id

def test_insert_with_id():
    t0 = TestNull(a="a", b=None)
    # t0.id = "a" #TestNull中其实没有id属性，但可能会继承Document的id属性  -----这样使用会报错

    #尝试在TestNull中加入id属性
    # t0.id = "a" 加入id属性仍然会报错

    # 尝试在TestNull中加入_id属性
    t0._id = "a" #此时可以在将数据里的_id设置成a  但无法获取到 id属性了

    t = t0.save()
    print t.to_json()
    print t.id  # id为None
    print t._id #_id为实际id

if __name__ == '__main__':
    connect("test")
    test_insert_with_id()

