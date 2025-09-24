# # 2p
# def sum(a, b):
#     return a + b
#
# # 3p
# a = 3
# b = 4
# c = sum(a,b)
# print(c)
#
# # 5p
# def sum(a,b):
#     result = a + b
#     return result
# a = sum(3,4)
# print(a)
#
# # 6p
# def say():
#     return 'Hi'
#
# a = say()
# print(a)
# # 7p
# def sum(a,b):
#     print("%d, %d의 합은 %d입니다."%(a,b,a+b))
#
# sum(3,4)
# # 8p
# a = sum(3,4)
#
# print(a)
# # 9p
# def say():
#     print('Hi')
#
# say()
#
# 함수를 사용하는 4가지 방법이 있습니다.
# # 10p
# def sum_many(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     return sum
#
# sum_many(1,2,3)
# # 11p
# result = sum_many(1,2,3)
# print(result)
#
# result = sum_many(1,2,3,4,5,6,7,8,9,10)
# print(result)
#
# # 12p
# result = sum_many(1,2,3)
# print(result)
#
# result = sum_many(1,2,3,4,5,6,7,8,9,10)
# print(result)
# # 13p
# def sum_mul(choice, *args):
#     if choice == "sum":
#         result = 0
#         for i in args:
#             result  = result + i
#     elif choice == "mul":
#         result = 1
#         for i in args:
#             result = result * i
#     return result
#
# # 14p
# result = sum_mul('sum',1,2,3,4,5)
# print(result)
#
# result = sum_mul('mul',1,2,3,4,5)
# print(result)
#
# # 15p
#
# def sum_and_mul(a,b):
#     return a+b, a*b
#
# result = sum_and_mul(3,4)
#
# result
# # 16p
# sum, mul = sum_and_mul(3,4)
#
#
# # 17p
# def sum_and_mul(a,b):
#     return a+b
#     return a*b
#     # 두번째 리턴문은 실행되지 않음
#
# result = sum_and_mul(2,3)
# print(result)
#
# def sum_and_mul(a,b):
#     return a+b
# # 따라서 이 함수와같다
#
# # 18p
# def say_nick(nick):
#     if nick == "바보":
#         return
#     print("나의 별명은 %s입니다." %nick)
#
# # 19p
# say_nick('야호')
#
# say_nick('바보')
# # 바보라는 값이 들어오면 리턴
#
# # 20p
# def say_myself(name, old, man=True):
#     print("나의 이름은 %s 입니다."% name)
#     print("나이는 %d살 입니다."% old)
#     if man:
#         print("남자입니다.")
#     else:
#         print("여자입니다.")
#
# # 21p
#
# say_myself("박응용",27)
# say_myself("박응용",27,True)
#
# say_myself("박응용",27,False)
#
# # 22p
#
# def say_myself(name, man=True, old):
#     print("나의 이름은 %s 입니다."% name)
#     print("나이는 %d살입니다."% old)
#     if man:
#         print("남자입니다.")
#     else:
#         print("여자입니다.")
#
# say_myself("박응용",27)
#
# # 이렇게 할경우  27을 변수 둘중 어느곳에 대입해야할지 알 수 없게됨
# # 23p
#
#
# # 24p
# a = 1
# # 함수 밖의 변수 a
# # vartest 함수 선언
# def vartest(a):
#     a = a +1
#
# vartest(a)
# print(a)
# # 답은 2가 아니다 이유는 함수 밖의 변수 이기 때문이다.
#
# # 25p
# #vartest_error.py
# def vartest(a):
#     a=a+1
#
# vartest(3)
# print(a)
#
#
# # 26p
# a = 1
# def vartest(a):
#     a = a + 1
#     return a
#
# a = vartest(a)
# print(a)
#
# # 27p
# #vartest_global.py
# a = 1
# def vartest():
#     global a
#     a = a +1
#
# vartest()
# print(a)
#
#
# # global 가능한 사용하지 말것 리턴 사용하자
#
#
# # 28p
# a=input()
# Life is too short, you need python
#
# a
#
# # 프롬프xm 띄어서 사용자 입력 받기
#
# # 29p
#
# numbers = input("숫자를 입력하세요: ")
# print(numbers)
#
#
#
# # 30p
#
# a = 123
# print(a)
# 123
# a = “Python”
# print(a)
# Python
# a = [1, 2, 3]
# print(a)
# [1, 2, 3]
#
#
#
# # 31p
#
# print("life""is""too short")
#
# print("life"+"is"+"too short")
#
# print("life","is","too short")
#
#
# # 32p
#
# for i in range(10):
#     print(i, end='')
#
# # 33p
#
# f = open("새파일.txt",'w')
# f.close()
#
#
#
# # 34p
#
# r   읽기 모드 – 파일을 읽기만 할 때 사용
#
# w   쓰기 모드 – 파일에 내용을 쓸 때 사용
#
# a   추가 모드 – 파일의 마지막에 새로운 내용을 추가할 때 사용
#
# # 35p
# f = open(“C:\python\새파일.txt", 'w')
# f.close()
#
#
#
# # 36p
#
# f = open("C:\python\새파일.txt",'w')
# for i in range(1,11):
#     data = "%d번째 줄입니다.\n"%i
#     f.write(data)
# f.close()
#
#진도 여까지 나감
#
# # 3p
#
#
#
# # 3p
#
#
# # 3p

