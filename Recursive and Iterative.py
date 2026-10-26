#Part a):
def Unkown(x,y):
    if x < y:
        print(x+y)
        return (Unkown(x + 1,y) *2)
    elif x == y:
        return 1
    else:
        print(x+y)
        return int((Unkown(x-1,y) / 2))
    
#Part b(i)
print("10 and 15")
print(Unkown(10,15))
print("10 and 10")
print(Unkown(10,10))
print("15 and 10")
print(Unkown(15,10))

#Part c)
def IterativeUnkown(x,y):
    while x != y:
        flag = False
        if x < y:
            print(x+y)
            x = x+1
            flag = True
        else:
            print (x+y)
            x = x-1
    if x == y:
        return 1
    if flag == True:
        return (x* 2)
    else:
        return (x / 2)
print(IterativeUnkown(10,15))