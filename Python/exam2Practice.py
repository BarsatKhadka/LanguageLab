import math

# print("The value of pi  is ", math.pi)

# x = 4.1

# print("Ceil value is" ,math.ceil(x))
# print("Floor value is", math.floor(x))
# print("Round value is", round(x))

import random

# rand1 = random.randint(1,9)

# #this doesnot print random values everytime
# for i in range(5):
#     print(rand1)


# #this will print ranadom values everytime
# for i in range(5):
#     print(random.randint(1,9))



# choices = ["hello" , "tommorrow i need a 100" , "adding-more", "some more senpai",
#            "random", "truly random"]

# print(random.choices(choices))

# print("Barsat\nKhadka")

# print("Barsat \"Hates Python\" ")
# print("But \'Why does he\'")
# print("I need a backslash ASAP \\")
# print("I need two backslashes \\\\")
# print("Idk what does this do \r")
# print("\t best formatting tool in console")


# print("Main Menu. Choose an option:\n\t1> Add a user\n\t2> Edit User\n\t3> Remove User\n\t4> Exit Application")

# plugin = 5.555555
# new = 5555555555
# serie = 12345
# print(f"barsat is practicing alignment {plugin:0<9.2f} in between")
# print(f"practice 2 {plugin:0>10.2f} in between")
# print(f"what {plugin:10,} is this")
# print(f"{new:,}")
# print(f"{serie:10,}")
# print(f"is it {serie:^10} in between")



#Challenge Problem 1 

# carA_speed = float(input("Enter the speed of car A"))
# carB_speed = float(input("Enter the speed of car B"))

# Time_hours = float(input("Enter the hours passed"))
# Time_minutes = float(input("Enter the minutes passed"))

# Total_time = float(Time_hours + Time_minutes/60)

# carA_avg = carA_speed/Total_time
# carB_avg = carB_speed/Total_time

# shortest_distance = math.sqrt((carA_avg **2) + (carB_avg **2))
# print(f"{shortest_distance:10.2f}")


#Challenge Problem 2

# Principal_balance = float(input("enter principal balance: "))
# r = float(input("Enter interest rate: "))
# n = float(input("number: "))
# t = float(input("time period"))

# area = Principal_balance * ((1 + r/n)** n/t)

# while True:
#     num = int(input("Enter a number between 1 to 9: "))
#     match num:
#         case 1:
#             print("lumber one")
#         case 2:
#             print("why am i doing htis")
#         case 3 | 4 | 5:
#             print("Everybody's doing it")
#         case _ :
#             print("Nothing")

# num  = int(input(("Enter a number: ")))
# match num:
#     case num if num > 0:
#         print("Negative numebr")
#     case num if num <0:
#         print("positive number in parallel world")
#     case _:
#         print("0 most probably")


# num = int(input("Give me a positive number dawg: "))
# match num:
#     case num if num > 9:
#         print(f"The number has {num} more than one significant digits")
#     case num if num < 0 :
#         print("Error: Negative Numbers are not accepted")
#     case _:
#         print(f"The number {num} has only one significant digit")


# year = int(input("Enter the year number you are living in"))
# if(year%4 ==0):
#     print("You are living in a leap year")
# else:
#     print("Not a leap year, bad hai bad")


# for i in range(99,-99,-1):
#     print(i)

# lists = list("hello" , "very nice") this does not work
# print(lists)

lists = ["tie me down",1 ,2, 3, 4, 5]
# for i in lists:
#     print(i)

# for i in range(len(lists)):
#     print(i)


# for i in range(len(lists)):
#     print(lists[i])
#     if  i ==1:
#         break
   
# count = 0
# for i in range(6):
#     ask_user = int(input(f"Write number of Bugs you collected on day {i+1} "))
#     count += ask_user
    

# print("The average is " , count/6)


# list_done = ['one', 'two', 'three']
# list_done.insert(5,'new')
# print(min(list_done))



lis = ["Sadhak","Python","Lang"]
rev = [word[::-1] for word in lis[::-1]]
print(rev)













