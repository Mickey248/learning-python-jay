# string = 'mic:jay:zeer:oat:feer'.split(':')
# print(string)
# print(type(string))
# print(len(string))

# for i in range(1,len(string)):
#     print(string[i])
# for i in string:
#     print(i)


# listBotnoi = []
# if 'oat' in string:
#    listBotnoi.append('oat')
# print(listBotnoi)
# for i in range(0,len(string)):
#     if 'jay' in string[i]:
#         listBotnoi.append(string[i])
#     elif 'oat' in string[i]:
#         listBotnoi.append(string[i])
# print(listBotnoi)
# for i in range(0,len(string)):
#     if 'jay' in string[i]:
#         listBotnoi.append(string[i])
#     elif 'oat' in string[i]:
#         listBotnoi.append(string[i])
    
# print(listBotnoi[0])

# listTest = []
# listFruit = ['apple','straw','banana','mongo','a','v','c','d','e']
# for i in range(0,len(listFruit)):
#     if i % 2 == 0:
#         listTest.append(listFruit[i])
#     print(listTest)

# [listTest.append(listFruit[i]) for i in range(0,len(listFruit)) if i % 2 == 0]
# print(listTest)

# name = input('you name is :')
# surname = input('you surname is :')
# print(name + ' ' +  surname)
# print('%s %s'%(name,surname))
# print('{} {}'.format(name,surname))
# print(f'{name} {surname}')

# listSpeed = []
# speed = int(input('Speed : '))
# # print(type(speed))
# if (speed < 90):
#     listSpeed.append(f'{speed}' + 'A')
# elif (speed > 90 and speed <= 120):
#     listSpeed.append(f'{speed}' + 'F')
# elif (speed > 120):
#     listSpeed.append(f'{speed}' + 'X')
# print(listSpeed)

# a = 4.2
# b = 4.8
# print(int(a)+int(b))
# print(int(a + b))
# a = int(float(input('saffs:')))
# print(a)

# for i in range(0,5):
#     print(i)




listMail = []
a = 0
b = 0
c = 0
emailPeople = ['a@gmail.com','b@yahoo.com','c@hotmail.com','d@gmail.com']
# พี่อยากให้มันเเสดง ประเภทเมล
# มีเมลไรบ้างโดยห้ามเเสดงซ้ำ
# เเต่ละประเภทของเมลเเต่ละอันมีกี่อัน
# for i in range(0,len(emailPeople)):
#     catagoryEmail = emailPeople[i].split('@')[1]
#     if catagoryEmail not in listMail:
#         listMail.append(catagoryEmail)
# print(listMail)
# for i in range(0,len(emailPeople)):
#     if 'gmail.com' in emailPeople[i]:
#         a += 1
# print(f'category gmail = {a}')
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for keys, values in thisdict.items():
#   print(keys, values)
# print(thisdict['brand'])
# print(len(thisdict['brand']))
# print(len(thisdict))


# computer = ['mac','pc']
# del computer[1]
# print(computer)

# typeFruit = 'apple'
# def fruit(category):
#     # fruit = 'apple'
#     return category
# print(fruit(typeFruit))

# typeFruit = 'apple'
# name = 'mickey'
# def fruit(category):
#     # fruit = 'apple'
#     return category
# print(fruit(typeFruit))
# print(fruit(name))
# name = 'mickey'
# surname = 'supasun'
# def function(ox,ok):
#     profile = f'{ox} {ok} like apple'
#     return profile
# # print(function(name,surname))


# def test():
#     profile = 'like apple'
#     return profile
# def helpFunction():
#     testFunction = test()
#     print(testFunction)
# print(helpFunction())


class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14

print(Circle(8).area())
print(Circle(8).perimeter())










