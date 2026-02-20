# result=0
#
# def adder(num):   # def 함수 만들때 씀
#     global result # 전역변수로 선언하여 이전 계산값이 유지됨
#     result += num # num 변수의 값을 result에 더한다
#     return result # result 변수에 담긴 값을 돌려준다.
#
# print(adder(3))

class Service:
    secret = "영구는 배꼽이 두 개다."  # 클래스 변수
    def sum(self, a, b):  # 클래스 함수
        result = a + b
        print("%s + %s = %s입니다." % (a, b, result))


pey = Service()
# print(pey.secret)
pey.sum(1, 1)