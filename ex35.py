# 빅데이터 프로그래밍_3장
#
# --------------------------------
# if문
# --------------------------------

# 3-1
# money = 1
# if money:
#     print("택시를 타고 가라")
# else:
#     print("걸어 가라")

# 3-5 만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어 가라
# money = 2000
# if money >= 3000:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")

# 3-6 돈이 3000원 이상 있거나 카드가 있으면 택시를 타고 그렇지 않으면 걸어 가라
# money = 2000
# card = 1
# if money >= 3000 or card:
#     print("택시를 타고 가라")
# else:
#     print("걸어가라")

# treeHit = 0
# while treeHit < 10:
#     treeHit = treeHit + 1
#     print("나무를 %d번 찍었습니다."%treeHit)
#     if treeHit == 10:
#         print("나무 넘어갑니다.")


# coffee=10
# money=300
# while money:
#     print("돈을 받았으니 커피를 줍니다.")
#     coffee=coffee-1
#     print("남은 커피의 양은 %d개입니다."%coffee)
#     if not coffee:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break


# coffee=10
# while True:
#     money=int(input("돈을 넣어 주세요:"))
#     if money==300:
#         print("커피를 줍니다.")
#         coffee=coffee-1
#     elif money>300:
#         print("거스름돈 %d를 주고 커피를 줍니다."%(money-300))
#         coffee=coffee-1
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#         print("남은 커피의 양은 %d개입니다."%coffee)
#     if not coffee:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break


# a=0
# while a<10:
#     a=a+1
#     if a%2==0:continue
#     print(a)


# while True:
#     print("CTRL+C를 눌러야 while문을 빠져나갈 수 있습니다.")


# test_list = ['noe','two','three']
# for i in test_list:
#     print(i)


# a=[(1,2),(3,4),(5,6)]
# for (first, last) in a:
#     print(first + last)


# for문의 응용
# 총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다.
# 합격인지 불합격인지 결과를 보여주시오.
#
# #우선 학생 5명의 시험 점수를 리스트로 표현함
# marks=[90,25,67,45,80]
# #학생에게 붙여 줄 번호
# number=0
# for mark in marks:
#     number=number+1
#     if mark>=60:
#         print("%d번 학생은 합격입니다."%number)
#     else:
#         print("%d번 학생은 불합격입니다."%number)


# continue문 활용 -> false일 경우 print 하지 않고 continue 작동하게
# 60점 이상인 사람에게는 축하 메시지를 보내고 나머지 사람에게는 아무런 메시지도 전하지 않음
#
# marks=[90,25,67,45,80]
# number=0
# for mark in marks:
#     number = number +1
#     if mark < 60: continue
#     print("%d번 학생 축하합니다. 합격입니다."%number)


# range함수 활용 -> for문에서 자주 활용
#
# 0부터 범위 지정시
# a=range(10)
# a
#
# 원하는 곳 부터 범위 지정시
# a=range(1,11)
# a


# range 함수 예제
# for문과 range 함수를 이용하여 1부터 10까지 더하기
#
# sum=0
# for i in range(1,11):
#     sum=sum+i
#
# print(sum)


# range 함수 및 len 함수 예제 -> len 리스트 내 요소의 개수를 돌려주는 함수
# 60점 이상이면 합격이라는 문장을 출력하는 예제를 range 함수를 이용하여 출력
#
# marks=[90,25,67,45,80]
# for number in range(len(marks)):
#     if marks[number] < 60: continue
#     print("%d번 학생 축하합니다. 합격입니다."%(number + 1))


# for문과 range 함수 를 이용한 구구단
#
# for i in range(2,10):
#     for j in range(1,10):
#         print(i*j,end="")
#     print('')

# for문이 두 번 사용되었는데 첫 번째 for문에서 2부터 9까지의 숫자 (range(2,10))
# 차례로 i에 대입됨
# i가 처음 2일때 두 번째 for문을 만나게 되는 데 두 번째 for문에서 1부터 9까지의
# 숫자(range(1,10))가 j에 대입되고 그 다음인 pritn(i*j)를 수행함
# i가 2일 때 2*1, 2*2, ..., 2*9까지 차례로 수행되며 그 값을 출력함
# 그 다음 i가 3일 때 역시 2일 때와 마찬가지로 수행되고 i가 9일 때까지 계속 반복됨
#
# 입력 인수 end를 넣어 준 이유
# print(i*j, end="")와 같이 입력 변수 end를 넣어 준 이유는 결과 값을 출력할 때
# 다음 줄로 넘기지 않고 그 줄에 계속해서 출력하기 위해서임


# 리스트 안에 for문 포함하기
#
# a=[1,2,3,4]
# result=[]
# for num in a:
#     result.append(num*3)
#
# print(result)
# 요것은 가독성이 떨어짐
#
# 리스트 내포를 이용하면 아래와 같이 간단히 해결됨
# a=[1,2,3,4]
# result=[]
# result = [num * 3 for num in a]
# print(result)


# 짝수에만 3을 곱하여 담기 -> if 조건 활용
#
# a = [1, 2, 3, 4]
# result = []
# result=[num*3 for num in a if num % 2 == 0]
# print(result)


# 구구단의 모든 결과를 리스트에 담고 싶다면 리스트 내포를 이용하여 구현
#
# result = [x*y for x in range(2,10)
#           for y in range(1,10)]
# print(result)




if문
돈이 있으면 택시를 타고, 돈이 없으면 걸어 간다.

money=1
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")


조건문 활용

x=3
y=2
x>y

x는 y보다 크기 때문에 True를 반환한다.

x<y

x는 y보다 크기 때문에 False를 반환한다.

x==y

x는 y와 같지 않기 때문에 False를 반환한다.

x != y

x와 y는 같지 않기 때문에 True를 반환함


if문을 활용
만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어 가라

money=2000
if money>=3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")


if문 활용
돈이 3000원 이상 있거나카드가 있으면 택시를 타고 그렇지 않으면 걸어 가라

money=2000
card=1
if money>=3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")


if문에서의 조건문

1 in[1,2,3]

True 결과 나옴

1 not in[1,2,3]

False 결과 나옴


튜플과 문자열에 적용한 예

'a'in('a','b','c')

True 결과 나옴

'j'not in 'python'

True 결과 나옴


if문 에서 list 활용
만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어가라

pocket=['paper','cellphone','money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")


if문 에서 list 활용
주머니에 돈이 있으면 가만히 있고 주머니에 돈이 없으면 카드를 꺼내라

pocket=['paper','money','cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

pocket이라는 리스트 안에 money라는 문자열이 있기 때문에 if문 다음 문장인 pass가
수행되고 아무런 결과값도 보여 주지 않음


다양한 조건을 판단하는 elif
주머니에 돈이 있으면 택시를 타고, 주머니에 돈이 없지만 카드가 있으면 택시를 타고,
돈도 없고 카드도 없으면 걸어가라

if문과 else 만으로 표현

pocket=['paper','cellphone']
card=1
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")

다중 조건 판단을 가능하게 하는 elif

pocket=['paper','cellphone']
card=1
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라")


if문 한 줄로 작성

pocket=['paper','money','cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

위에 것을 한줄로
pocket=['paper''money','cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")


