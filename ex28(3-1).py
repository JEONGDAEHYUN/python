# marks=[90,25,67,45,80]
#
# for number in range(len(marks)):
#     if marks[number] < 60: continue
#     print("%d번 학생 축하합니다.합격입니다."%(number+1))

# for i in range(2,10):
#     for j in range(1,10):
#         print(i*j, end="")
#     print('')

#리스트 안에 메퍼(가독성 떨어짐)
# a=[1,2,3,4]
# result=[]
# for num in a:
#     result.append(num*3)
# print(result)

# 표현식(num*3) for 항목(num) in 반복가능 객체(a)
# a=[1,2,3,4]
# result=[num*3 for num in a]
# print(result)

# 표현식 for 항목 in 반복 가능 객체 if 조건1
# a=[1,2,3,4]
# result =[num*3 for num in a if num % 2 == 0]
# print(result)

# 구구단의 모든 결과를 리스트에 담는다
# result=[x*y for x in range(2,10)
#         for y in range(1,10)]
# print(result)

# a = 0
# while a < 10:
#     a = a+1
#     if a % 2 == 0: continue
#     print(a) 들여쓰기x while 문안에 있는 프린트

# test_list = ['one','two', 'three']
# for i in test_list:
#     print(i)

# 21p
# a = [(1,2),(3,4),(5,6)]
# for (first, last) in a:
#     print(first + last)

# marks = [90,25,67,45,80]

# 24p
# a = range(10)
# a

# a = range(1, 11)
# a

# 29p
# a = [1,2,3,4]
# result = []
# for num in a:
#     result.append(num*3)
#
# print(result)

# a = [1,2,3,4]
# result = [num * 3 for num in a]
# print(result)

