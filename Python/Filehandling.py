# f = open('a.txt', 'r')
# print(f.name)
# f.close()


# with open('house.txt' , 'r') as f:
#     # for line in f:
#     #     print(line)
#     f_content = f.read(100)
#     print(f_content)


filename = input("Enter the file name:")
file = open(filename,'a')
add_more = True
while add_more:
    val = input("Enter the content here:")
    file.write(val)
    file.write("\n")
    if val=="exit":
        add_more = False

    