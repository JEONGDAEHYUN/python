# #adder1.py
# result = 0
#
# def adder(num):
#     global result
#     result += num
#     return result
#
# print(adder(3))
# print(adder(4))
#
# #adder2.py
# result1 = 0
# result2 = 0
# def adder1(num):
#     global result1
#     result1 += num
#     return result1
# def adder2(num):
#     global result2
#     result2 += num
#     return result2
# print(adder1(3))
# print(adder1(4))
# print(adder2(3))
# print(adder2(7))
#
# #adder3.py
# class Calculator:
#      def __init__(self):
#           self.result = 0
#
#      def adder(self, num):
#          self.result += num
#          return self.result
#
# cal1 = Calculator()
# cal2 = Calculator()
#
# print(cal1.adder(3))
# print(cal1.adder(4))
# print(cal2.adder(3))
# print(cal2.adder(7))
#
# #인스턴스 설명 7.py
# class Simple:
#     pass
#
# a=Simple()

# class Service:
#     secret = "영구는 배꼽이 두 개다."
#     def sum(self, a,b):
#         result = a + b
#         print("%s + %s = %s입니다."%(a, b, result))
#
# pey = Service()
#
# pey.sum(1, 1)
#
# class Service:
#     secret = “영구는 배꼽이 두 개다.”
# def setname(self, name):
#     self.name = name
# def sum(self, a, b):
#     result = a + b
#     print (“%s님 %s + %s = %s입니다.” % (self.name, a, b, result))
#
#
# 31p
# class FourCal:
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
#
#     def sum(self):
#         result = self.first + self.second
#         return result
#
#     def mul(self):
#         result = self.first * self.second
#         return result
#
#     def sub(self):
#         result = self.first - self.second
#         return result
#     def div(self):
#         result = self.first / self.second
#         return result
#
# a = FourCal()
# b = FourCal()
# a.setdata(4, 2)
# b.setdata(3, 7)
# a.sum()
#
#
# class HousePark:
#     lastname="박"
#
# pey=HousePark()
# pes=HousePark()
#
#
# class HousePark:
#     lastname="박"
#     def detname(self, name):
#         self.fullname=self.lastname+name
#
# class HouseKim(HousePark):
#     lastname="김"
#     def travel(self, where, day):
#         print("%s,%s여행 %d일 가네."%(self.fullname, where, day))
#
#
# class HousePark:
#     lastname="박"
#     def __init__(self,name):
#         self.fullname=self.lastname+name
#     def travel(self,where):
#         print("%s, %s여행을 가다." % (self.fullname, where))
#     def love(self, other):
#         print("%s, %s 사랑에 빠졌네" % (self.fullname, other.fullname))
#     def __add__(self, other):
#         print("%s, %s 결혼했네" % (self.fullname, other.fullname))
#
#
# class HouseKim(HousePark):
#     lastname = "김"
#     def travel(self, where, day):
#         print("%s, %s여행 %d일 가네." % (self.fullname, where, day))
#
#
# pey = HousePark("응용")
# juliet = HouseKim("줄리엣")
# pey.love(juliet)
# pey + juliet




class HousePark:
    lastname="박"
    def __init__(self, name):
        self.fullname=self.lastname+name
    def travel(self, where):
        print("%s, %s여행을 가다." %(self.fullname, where))
    def love(self, other):
        print("%s, %s사랑에 빠졌네" %(self.fullname, other.fullname))
    def fight(self, other):
        print("%s, %s싸우네"%(self.fullname, other.fullname))
    def __add__(self, other):
        print("%s, %s 결혼했네"%(self.fullname, other.fullname))
    def __sub__(self, other):
        print("%s, %s 이혼했네"%(self.fullname, other.fullname))

class HouseKim(HousePark):
    lastname="김"
    def travel(self, where, day):
        print("%s, %s 여행 %d일 가네." %(self.fullname, where, day))

pey = HousePark("응용")
juliet = HouseKim("줄리엣")
pey.travel("부산")
juliet.travel("부산",3)
pey.love(juliet)
pey + juliet
pey.fight(juliet)
pey - juliet