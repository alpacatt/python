'''
bicycles = ["terk","cannondale","redline","specialized"]
print(bicycles[0])      #列表只返回该值，不包括方括号以及引号。索引从0开始
print(bicycles[-2])      #倒叙索引从-1开始
'''
'''
names = ["zxc","zjh","cy"]
for num in range(0,3):
    print("Hello, " + names[num].title() + ", how are you today?")
for name in names:
    print("Hello, " + name.title() + ", how are you today?")
'''
'''
vehicles = ["car","bus","bike"]
print(vehicles)
#for vehicle in vehicles:
#    print("I would like to go school by " + vehicle + ".")

vehicles[0] = "boat"

print(vehicles)

vehicles.insert(0,"van")      #insert可以在任意位置插入
vehicles.append("car")      #在列表的末尾添加新的元素
print(vehicles)

transports = []
print(transports)
for vehicle in vehicles:
    transports.append(vehicle)
print(transports)
'''
foods = ["rice","noodle","berg","bread"]
'''
print(foods)

del foods[2]      #del在删除元素后便无法再访问了
print(foods)

foods.insert(2,"berg")
print(foods)

favourite = foods.pop(2)
print(foods)
print(favourite)      #使用pop删除元素，还可以再次访问他

favourites = []
for i in range(0,2):
    favourite = foods.pop(i)
    favourites.append(favourite)
print(favourites)
'''
'''
too_expensive = "berg"       #remove可以删除指定值的元素
foods.remove(too_expensive)
print(foods)
print(too_expensive)
print("I dont like to eat " + too_expensive + " because its too expensive.")
'''

names = ["zjh","zxc","zjy","cy","tt"]
for name in names:
    print("Hello! " + name.title() + ", I would like to invite you to my party!")
no_come = "zjy"
order = names.index(no_come)      #找出不来的人在列表中的次序
names.remove(no_come)
print(no_come + " wont come.")
print(order)
names.insert(order,"zl")      #用新来的人代替旧的位置
print(names)
for name in names:
    print("Hello! " + name.title() + ", I would like to invite you to my party!")

print("I find a bigger table!")
names.insert(0,"laoma")
print(names)
guest_num = int(len(names)/2)      #利用列表长度计算中间位置的次序
names.insert(guest_num,"laoba")
names.append("laojiu")
print(names)
for name in names:
    print("Hello! " + name.title() + ", I would like to invite you to my party!")

print("Cuz the lack of table, I can only invite two guest.")
while len(names)>2:
    name = names.pop()
    print("Sorry " + name + ", there is no sit for you.")
for name in names:
    print("Im glad to inform you, " + name + ", you are still invited.")
del names[0]
del names[0]
print(names)


