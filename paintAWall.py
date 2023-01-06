import math as m

def paintAWall(height,width,coverage):
    cans = m.ceil((height*width)/coverage)
    print(cans)


paintAWall(2,4,5)