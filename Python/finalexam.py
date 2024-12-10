import turtle

import tkinter as tk

# # test = random.randint(0,1)  #this includes 1
# # print(test)

# # for i in range(5):  #random 5 times.
# #     print(i)


# # new_list = ['barsat' , 'taimori', 'vana' , 'dalkhyo']

# # very = random.choice(new_list)
# # print(very)


# # print("who am i \n i am him")

# # dec = 2.789898898
# # print(f"dec is {dec:.2f}")
# # print(f"dec is{dec:0<6.2f}")
# # print(f"dec is {dec:0>6.2f}")
# # print(f"dec is{dec:10.20}")

# # normal = 2093874374374973247329
# # p0int(f"normal seperated by comma {normal:,}")
# # p0int(f"scientific notation {normal:e}")
# # 
# # new_normal = 8928392.23290382
# # print(f"integer number {new_normal:d}") gives error

# # name = "barsat"
# # print(f"***** {name:^20} *****")


# turtle.setup(450,450)
# turtle.bgcolor("green")
# turtle.forward(120)
# turtle.right(120)
# turtle.done()

# turtle.setup(450,450)
# turtle.penup()
# turtle.goto(100,100)
# turtle.setheading(180)
# turtle.pendown()
# turtle.forward(200)
# turtle.setheading(270)
# turtle.forward(200)
# turtle.setheading(0)
# turtle.forward(200)
# turtle.setheading(90)
# turtle.forward(200)
# turtle.done()

# name1 = "barsat"
# name2 = "barsath"

# if name1 >name2:
#     print("name 1 great")
# else:
#     print("name 2 great")

# name = "barsat"
# match name:
#     case "basrat":
#         print("reread")
#     case "barsat":
#         print("right one dog")
#     case "test":
#         print("I got a B")
#     case _ :
#         print("default")

# number = int(input("Enter number between 1 and 6: "))
# match number:
#     case 1 |2 :
#         print("either number 1 or 2")
#     case number if number > 2:
#         print("number greater than 2")
#     case number if number > 6:
#         print(" i need between 1 and 6")
#     case _:
#         print("bruh")


# def submitEventHandler(event):
#     age = int(textEntry.get())
#     return lbMessage.config(text = f"your age is {age}")

# window = tk.Tk()
# window.geometry("500x500")
# lbMessage = tk.Label(text="Hello world")
# textEntry = tk.Entry()
# textButton = tk.Button(text="submit")
# textEntry.pack()
# textButton.pack()
# textButton.bind("<Button-1>",submitEventHandler)
# lbMessage.pack()
# window.mainloop()


# def MakeForm():
#     ask_1 = tk.Label(text = "2 tests average")
#     ask_1_box = tk.Entry()
#     ask_1.pack()
#     ask_1_box.pack()
#     ask_2 = tk.Label(text = "quizzes and activities")
#     ask_2_box = tk.Entry()
#     ask_2_box.pack()
#     ask_3 = tk.Label(text = "Programming assignments")
#     ask_3.pack()
#     ask_3_box = tk.Entry()
#     ask_3_box.pack()

# window = tk.Tk()
# window.geometry("500x500")
# MakeForm()
# window.mainloop()

# def submitButton(event):
#     age = int(text_box.get())
#     if age > 18:
#         text.config(text = "Your age is {age} , Legal guy")
#     else:
#         text.config(text = "Your age is not 18")


# window = tk.Tk()
# window.geometry("500x500")
# text = tk.Label(text = "Enter your age: ")
# text.pack()
# text_box = tk.Entry()
# text_box.pack()
# button = tk.Button(text = "submit")
# button.bind("<Button-1>", submitButton)
# button.pack()
# window.mainloop()


# new_Value = [2,3,4,5,6,7]
# tough = [2,3,4]
# print(tough[1:])
# print(tough[:2])

# for i,j in enumerate(new_Value):
#     print(i,j)


# my_students = ["Chad", "Corey", "Dustin", "Hope", "Jessica",
# "Bridget", "Matthew", "Angela", "Amanda", "Brandon",
# "Jeremy"]

# print(my_students)

# my_students.sort(reverse=True)
# print(my_students)

# my_list = [
# [ 2, 4, 6, 8], # Row 1
# [10, 12, 14, 16], # Row 2
# [18, 20, 22, 24] # Row 3
# ]
# 
# sum = 0
# 
# for i in range(len(my_list)):
    # for j in range(len(my_list[i])):
        # if my_list[i][j] % 2 == 0:
            # sum += my_list[i][j]
# 




# 
# my_list[0].insert(2,2)
# print(my_list)


# Barsatstr = "barsat  barsatbarsat"
# new_list = (Barsatstr.split("s"))
# print("".join(new_list))

# new = Barsatstr.replace("bar", "new")
# print(new)


newd = ["fjfdsklfjkdslf", "jhfjdhfjkdsfds"]
# newd.reverse()
# print(newd)
vnewd = []

# print(newd)

# lastone = len(newd)
# for i in range (lastone , 0 , -1):
#     vnewd.append(newd[i - 1])

# print(vnewd)


# for i in range (5,0,-1):
    # print(i)
# 


# barsat = "barsatKhadkaIS"
# print(barsat.replace("b", "new" ))
# print(barsat.find("d", 7, 10))
# print(barsat.find('a'))
# print(barsat.rfind('a'))
# 
# 
# newd = "barsat kjkdjfklds dkkfjalkjfla"
# print(newd.capitalize())
# print(newd.title())

# file = open('newfile.txt', 'w')
# file.write('hello')
# # print(file.readlines())
# file.close()


# file = open('house.txt' , 'r')
# file_contents = file.readlines()
# for i in file_contents:
#     print(i)
#     print()
#     data = i.split("\t")
#     print(data)


# file = open('house.txt', 'wb')
# arr = [4,5,6,7,8,9]
# barr = bytearray(arr)
# file.write(barr)
# file.close()

# file = open('house.txt','rb')
# number = file.read(3)
# print(number)
# file.close()


dicti = {'barsat': 80, 'new': 'hero'}

# print(dicti['barsat'])
# print(dicti['nobo'])

# for i in dicti:
#     print(i,dicti[i])

# dicti.clear()

# return_copy = dicti.copy()
# print(return_copy)
# print(dicti)


# listed = [98,34,53,53,53,53,53]
# doesItReturn = listed.pop()
# print(listed)
# print(doesItReturn)

# x = {'barsat'}
# y = 0
# print(dicti.fromkeys(x,y))

# print(dicti.get("barsat"))
# print(dicti.items())

# for i in dicti.items():
#     print(i[0])

# 
# for i in dicti.keys():
    # print(i)

# for i in dicti.values():
    # print(i)

# print(dicti.pop(len(dicti)))  not work

# print(len(dicti))

# print(dicti.pop(len(dicti) - 1))

# print(dicti.pop('barsat'))
# print(dicti)

# del dicti['barsat']
# print(dicti)

# print(dicti.popitem())
# print(dicti)

# print(dicti.setdefault('newbarsat', 0))
# print(dicti)

# print(dicti.update({'barsat' : 0}))
# print(dicti)

# print(dicti.values())

# values = dicti.values()
# for i in values:
    # print(i)
# 
# dicti.clear()
# print(dicti)

# print(dicti.copy())

# x = ('key1', 'key2', 'key3')
# y = 0

# newdict = dicti.fromkeys(x,y)
# print(newdict)

# store = (newdict.get('key1'))
# print(store)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
# 
# print(car.items())
# 
# for i in car.items():
    # print(i[0], i[1])


# for i in car.keys():
    # print(i)

# print(car.pop("brand"))
# print(car)

# print(car.popitem())
# print(car)
# new  = (car.setdefault("model", "bronco"))
# print(new)
# print(car)

# update = car.update({"model":"bronco"})
# print(car)

myfamily = {
"child1" : {
"name" : "Emil",
"year" : 2004
},
"child2" : {
"name" : "Tobias",
"year" : 2007
},
"child3" : {
"name" : "Linus",
"year" : 2011
}
}

# for i in myfamily.keys():
    # for j in (myfamily[i]):
        # print(j[0], j[1])
# 

# for i,j in myfamily.items():
    # print(i)
    # for y in j:
        # print(y , j[y])
# 
# print(myfamily['child1']['name'])

# for x in myfamily:
    # for y in myfamily[x]:
        # print(myfamily[x][y])

# file = open('vnew.txt' , 'wb')
# arr = [89,34,44,34,34,43]
# barr = bytearray(arr)
# file.write(barr)
# file.close()

# file = open('vnew.txt', 'rb')
# contents = file.read(3)
# print(contents)
# file.close()
# 

# turtle.setup(450,450)
# turtle.penup()
# turtle.goto(100,100)
# turtle.setheading(180)
# turtle.pendown()
# turtle.forward(100)
# turtle.setheading(270)
# turtle.forward(100)
# turtle.setheading(0)
# turtle.forward(100)
# turtle.setheading(90)
# turtle.forward(100)
# turtle.done()

# strd = "Hello World"
# newd = strd.split(" ")
# print(newd)
# vnewd = newd[::-1]
# print(vnewd)
# print(" ".join(vnewd) )

# new = ['barsat' , 'sadas' , 'asdasd']
# new.sort(reverse=True)
# barsat = sorted(new, reverse=True)
# print(barsat)
# 
# window = tk.Tk()
# window.geometry("500x500")
# lblText = tk.Label(text="Hello world")
# lblText.pack()
# window.mainloop()

listed = [4,5,2,32,232,32,3,53,3]
print(min(listed))