print("hadiuhqod")
#print格式
first="ckjdsvua"
#变量
last="abssknckjc"
#字符串
full=first+" "+last
print(full.title())
#字符串.title():首字母大写；还有upper大写和lower小写
favourite_language=' python  '
print(favourite_language)
print(favourite_language.strip())
#消除两端空格；rstrip消除后空格lstrip消除前空格
#+-*/乘方为**
#str()#非字符串表示字符串
bicycles=['trek','cannondale','redline']
#列表
print(bicycles)
print(bicycles[0])
#访问列表，0为第一个，-1是最后一个
message="My first bicycles was a"+bicycles[0].title()+"."
#使用
bicycles[0]='ducati'
#列表元素可以改变
bicycles.append('ducati')
#在列表末尾加入
bicycles.insert(0,'ducati')
#在列表任意位置插入，0为开头
del bicycles[0]
#按照其位置顺序，删除列表元素;0为第一个
popped_bicycles=bicycles.pop()
print(bicycles)
print(popped_bicycles)
#按照顺序删除，并需要被删除量；pop()使列表最后一个元素弹出列表
# popped_bicycles则定义为最后一个元素，源列表最后一个被删除
first_bicycles=bicycles.pop(0)
#0为第一个，但当你使用pop使用时，源列表就删除了该元素
bicycles=['trek','cannondale','redline']
bicycles.remove('trek')
#根据值删除元素
too_expensive='cannondale'
bicycles.remove(too_expensive)
#可以先定义再删除
bicycles.sort()
# 永久排序：按首字母顺序对列表元素排序
bicycles.sort(reverse=True)
#首字母反顺序
print(sorted(bicycles))
#临时排序表示 反也是reverse=True
bicycles.reverse()
#反转顺序，永久
len(bicycles)
#列表长度，计数时从一开始
bicycles=['trek','cannondale','redline']
for bicycle in bicycles:
   print(bicycle)
   print(bicycle+",ihfjewhf")
   print(bicycle+",ihfjewhf"+"\n")
#for循环+"\n"换行
#注意缩进，循环外循环内
