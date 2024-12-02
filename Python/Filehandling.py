# f = open('a.txt', 'r')
# print(f.name)
# f.close()


with open('house.txt' , 'r') as f:
    # for line in f:
    #     print(line)
    f_content = f.read(100)
    print(f_content)