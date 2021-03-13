#3.Create a class Rectangle with private attributes length and width. Overload ‘<’  operator  to compare the area of 2 rectangles.
class Rectangle():
    def __init__(self, l, w):
        self.__length = l
        self.__width = w

    def area(self):
        return self.__length*self.__width

    def __lt__(self):
        if (area1 < area2):
            print("area of rectangle 1 is less than Rectangle 2 !")
        else:
            print("area of rectangle 2 is less than Rectangle 1 !")

print("\n***RECTANGLE 1***\n")
a=int(input("enter the length : "))
b= int(input("enter the width : "))
rect1=Rectangle(a,b)

print("area of rectangle 1 : ",rect1.area())

print("\n***RECTANGLE 2***\n")
p=int(input("enter the length : "))
q= int(input("enter the width : "))
rect2=Rectangle(p,q)

print("area of rectangle 2 : ",rect2.area())


area1 = rect1.area()
area2 = rect2.area()
obj=Rectangle(area1,area2)
obj.__lt__()