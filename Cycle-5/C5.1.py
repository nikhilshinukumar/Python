#1.Create  Rectangle  class  with  attributes  length  and  breadth  and  methods  to  find  area  and perimeter. Compare two Rectangle objects by their area
class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b

    def area(self):
            return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)

print("\n*** RECTANGLE 1 ***\n")
p =int(input("enter the length of rectangle 1 : "))
q =int(input("enter the breadth of the rectangle 1 : "))
rect1=Rectangle(p,q)
area1=rect1.area()

print("\n*** RECTANGLE 2 ***\n")
a =int(input("enter the length of rectangle 2 : "))
b =int(input("enter the breadth of the rectangle 2 : "))
rect2=Rectangle(a,b)
area2=rect2.area()

print("area of rectangle 1 : ", area1)
print("perimeter of rectangle 1 : ", rect1.perimeter())
print("area of rectangle 2 : ", area2)
print("perimeter of rectangle 2 : ",rect2.perimeter())

print("\n***COMPARISION**\n")
if rect1.area() > rect2.area():
 print("rectangle 1 is greater !!")
elif rect1.area() < rect2.area():
 print("rectangle 2 is greater !!")
else:
 print("both are the same !!")