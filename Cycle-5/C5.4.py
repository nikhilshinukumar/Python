#4.Create a class Time with private attributes hour, minute and second. Overload ‘+’ operator to find sum of 2 time
class Time:
    def __init__(self,hour,minute,second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        return self.__hour + other.__hour, self.__minute + other.__minute, self.__second + other.__second

print("\n***TIME 1***\n")
a=int(input("enter the hour : "))
b= int(input("enter the minute : "))
c= int(input("enter the second : "))

print("Time 1 : ", a, ":", b, ":", c)

print("\n***TIME 2***\n")
d=int(input("enter the hour : "))
e= int(input("enter the minute : "))
f= int(input("enter the second : "))

print("Time 2 : ", d, ":", e, ":", f)

t1 = Time(a,b,c)
t2 = Time(d,e,f)
t3 = t1 + t2
print("Sum of time : ",t3)