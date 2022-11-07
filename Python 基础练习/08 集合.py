

# 集合添加新的元素  s.add( x )

thisset = set(("Google", "Runoob", "Taobao"))
thisset.add("Facebook")
print(thisset)

# {'Taobao', 'Facebook', 'Google', 'Runoob'}


# s.update( x )

thisset.update({1,3})
print(thisset)

# {1, 3, 'Taobao', 'Google', 'Facebook', 'Runoob'}

thisset.update([1,4],[5,6])
print(thisset)

# 移除元素  s.remove( x )
thisset.remove(6)
print(thisset)


# 移除集合中的元素，且如果元素不存在，不会发生错误  s.discard( x )

thisset.discard(4)
print(thisset)

# 随机删除集合中的一个元素，语法格式如下：  s.pop()

thisset.pop()
print(thisset)


# 计算集合长度   len(thisset)
# 清空集合       s.clear()
