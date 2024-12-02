# 1. Basic Operations

#     Write a program that accepts a number from the user and determines if it is even or odd.
#     Create a function that accepts a string and prints its length.

# 2. Loops and Conditions

#     Write a program to print all even numbers between 1 and 50 using a for loop.
#     Using a while loop, reverse a given number (e.g., input 1234, output 4321).
#     Write a program that counts how many times a specific character appears in a string.

# 3. File I/O

#     Write a program to create a file, write five lines of text into it, and then read all lines back.
#     Modify the program to append a new line to the existing file and print the updated contents.
#     Write a program to count the number of lines in a given text file.

# 4. String Functions

#     Write a program to check if a substring is present in a string using the in operator.
#     Create a program to reverse a string and check if it is a palindrome.
#     Write a function that accepts a string, splits it into words, and prints the list of words.

# 5. List Operations

#     Write a program that takes a list of numbers as input and prints the list in reverse order.
#     Write a program to slice a list into two halves and print both halves.

# 6. Functions and Arguments

#     Write a function that accepts a number as an argument and returns its factorial.
#     Create a program where a function accepts two numbers and returns the greater one.
#     Write a program that demonstrates the use of keyword and positional arguments.

# 7. Processing 2D Lists

#     Write a program to find the sum of all elements in a 2D list.
#     Create a 2D list and write a program to print the transpose of the list.

# 8. Miscellaneous

#     Write a program to check if two variables refer to the same object using the is operator.
#     Create a function that appends an element to a list passed as an argument and returns the updated list


#1)
# number = int(input("Enter a number: "))
# if(number %2 ==0):
#     print("number is even")
# else:
#     print("number is odd")


# def accept(stringAccept):
#     if(type(stringAccept) == str):
#         return len(stringAccept)
#     else:
#         return "Not a valuid type"
    


# print(accept(4))


# even_list = list(i for i in range(50) if i%2 ==0)
# print(even_list)

# number = 12345

# count = len(list(str(number))) -1
# store = ""

# while(count >-1):
#     list_number = list(str(number))
#     store += str(list_number[count])
#     count -=1

# print(f"The reversed number is  {int(store)}")




# def appear(word , letter):
#     word = 'barsat'
#     count = 0
#     for i in word:
#         if(i == letter):
#             count +=1 
#     return count

# print(appear("barsat","b"))



# f = open('a.txt', 'r')
# print(f.name)
# f.close()


#Problem 1 chapter 7

# def class_type(A,B,C):
#     A_price = 20
#     B_price = 15
#     C_price = 10

#     total = A_price*A + B_price*B + C_price*C
#     return total



# list_here = ['barsat','new','thavayena']
# normal_str = "String"
# print(list_here.index('barsat'))
# print(list_here.find('barsat'))
# new = list_here[::-1]
# new = normal_str[::-1]
# print(new)

# names_str = "chad,corey,dustin,jessica"
# names_arr = names_str.split(",")
# print(names_arr)
# print("".join(names_arr))


# user_input = input("Enter the numbers you want to sum , seperated by commas ")

# input_arr = user_input.split(",")

# count = 0
# for i in input_arr:
#     count += float(i)

# print(count)

# barsat = "RaceCar"
# print(barsat[:4:2])

# variable = "BarsatBar"
# vnew = variable.replace("Bar","ass",2)
# print(vnew)


# find_index = "BarsatB"
# print(find_index.count("B"))
# print(find_index.find("B",2))
# print(find_index.rfind("B"))

# with open('a.txt','r') as f:
#     for line in f:
#         print(line)

# with open('b.txt', 'w') as f:
#     f.write("New file , b let's go")

# a = [1,2,3,4,5]
# b = [5,4,23,34,24]

# with open('b.txt','a') as f:
#     for i in a:
#         f.write(str(i))


# with open('house.txt','r') as f:
#     line = f.read

# with open('newfile.txt','w') as f:
#     f.write("Hello World")


# with open("house.txt" , 'r') as f:
#     lines = f.readlines()
#     print(len(lines))

# my_2d_list = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# count = 0
# for i in range(len(my_2d_list)):
#     for y in range(len(my_2d_list[i])):
#         count += my_2d_list[i][y]

# print(count)


# counting = "barsatbarsat"
# count = 0
# for i in counting:
#     if i== 'b':
#         count +=1 

# print(count)

with open('house.txt' , 'r' ) as f:
    new = list(f.read().split("\t"))
    print(new)


