import random

list = [12,1,31,12312]
print(random.choice(list))

string = "test"
print(random.choice(string))

print(random.randrange(1,25,3))

random.seed(5)
print(random.random())

random.seed(7)
print(random.random())

