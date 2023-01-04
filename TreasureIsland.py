list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]

ro = [list1,list2,list3]

treasure = input("Where to put the treasure")


column = int(treasure[0]) - 1
row = int(treasure[1]) - 1

print(ro[column][row])
