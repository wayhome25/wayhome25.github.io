class Animal():
    def walk(self):
        print('걷는다')

    def eat(self):
        print('먹는다')

    def greet(self):
        print('인사한다')

class Cow(Animal):
    '''소'''

class Human(Animal): # 상속 : 클래스 괄호 안에 다른 (부모)클래스를 넣는 것
    def wave(self):
        print('손을 흔든다')

    def greet(self): # 부모 클래스의 greet 메소드를 덮어쓰기 한다.
        self.wave()

class Dog(Animal): # Animal의 내용을 상속받는다
    def wag(self):
        print('꼬리를 흔든다')

    def greet(self): # 부모 클래스의 greet 메소드를 덮어쓰기 한다.
        self.wag()

person = Human()
person.greet()

dog = Dog()
dog.greet()

cow = Cow()
cow.greet()
# class Human():
#     '''인간'''
#     #__언더바2개__ 는 파이썬에서 특별한 함수라는 의미
#     def __init__(self, name, weight):
#         '''초기화 함수''' # 인스턴스 생성시 자동으로 실행되는 함수
#         self.name = name
#         self.weight = weight
#
#     def __str__(self):
#         '''문자열화 함수''' # 인스턴스 자체를 출력할 때의 형식을 지정하는 함수
#         return "{}(몸무게 {}kg)".format(self.name, self.weight)
#
#
# person = Human('몽키', '47') # 초기화 함수 사용
# print(person) # 문자열화 함수 사용
# 몽키(몸무게 47kg)



# class Human():
#     '''인간 클래스'''
#
# def create_human(name, weight):
#     person = Human()
#     person.name = name
#     person.weight = weight
#     return person
#
# Human.create = create_human
#
# person = Human.create('몽키', 50)
#
# def eat(person):
#     person.weight += 0.1
#     print('{}가 먹어서 {}kg이 되었습니다.'.format(person.name, person.weight))
#
# def walk(person):
#     person.weight -= 0.1
#     print('{}가 걸어서 {}kg이 되었습니다.'.format(person.name, person.weight))
#
# Human.eat = eat
# Human.walk = walk
#
# person.walk()
# person.eat()
# person.walk()
#

# class Human():
#     '''사람'''
#     #인간 클래스 작성
#
# # 한번 만든 클래스는 함수처럼 ()를 붙여서 호출
# person1 = Human() # Human 클래스의 instance person1, person2 정의
# person2 = Human() # 인간 클래스의 인스턴스가 person2에 생긴다.
#
# # 리스트에서 인스턴스 만드는 예
# a = list()
# isinstance(a, list) # True
#
# # 리스트의 다양한 기능을 사용할 수 있었던 건 리스트에 이미 기능들이 구현되어 있기 떄문이다.
# list1 = [1, 2, 3]
# list1.append(4) # [1, 2, 3, 4]
#
# # 각각의 클래스는 특성을 갖고 있다.
# # 인간 클래스의 특성 만들기
#
# person1.language = '한국어'
# person2.language = 'English'
#
# person1.name = '서울사람'
# person2.name = '인도사람'
#
# # 클래스를 사용하는 이유
# # 코드를 만드는데 꼭 필요하지는 않은 인위적인 도구
# # 클래스와 인스턴스를 이용하면 데이터와 코드를 사람이 보기 쉽게 작성할 수 있다.
#
# def speak(person):
#     print('{}이 {}로 말을 합니다'.format(person.name, person.language))
#
# Human.speak = speak
#
# person1.speak()
# person2.speak()
#
# list = [1 , 3, 4, 5, 6]
# str = "hello world"
# str[1 : 5]


# value = input('입력해주세요>') or '아무것도 없어'
# # input이 빈 경우 값은 false => 단락평가로 인해 or 뒤의 값으로 적용됨
# print('입력값 : ', value)

# dic = { 'key2' : 'value2' }
#
# if 'key1' in dic and dic['key1'] == 'value2': # 단락평가를 통해 첫번째 조건이 false 이기에 바로 확인 종료
# # if dic['key1'] == 'value2' and 'key1' in dic: => dic['key1'] 에서 에러 발생
#     print('있네!')
# else:
#     print('없네..')


# school = {'1반' : [150, 156, 179, 191, 199], '2반' : [150, 195, 179, 191, 199]}
#
# try:
#     for class_number, students in school.items():
#         for student in students:
#             if student > 190:
#                 print(class_number, '190을 넘는 학생이 있습니다.')
#                 # break # 바로 상위 for문은 종료되지만 최고 상위 for문은 종료되지 않는다.
#                 raise StopIteration
#                 # 예외가 try 문 안에 있지 않기 때문에 에러 발생시 프로그램이 멈춘다.
# except StopIteration:
#     print('정상종료')


# def rsp(mine, yours):
#     allowed = ['가위','바위', '보']
#     if mine not in allowed:
#         raise ValueError
#     if yours not in allowed:
#         raise ValueError
#
# try:
#     rsp('가위', '바')
# except ValueError:
#     print('잘못된 값을 넣었습니다!')

# try:
#     list = []
#     print(list[0])  # 에러가 발생할 가능성이 있는 코드
#
# except Exception as ex: # 에러 종류
#     print('에러가 발생 했습니다', ex) #
#     # 에러가 발생 했습니다 list index out of range
#     import your_module
# except ImportError:
#     print('모듈이 없습니다.')

# def safe_pop_print(list, index):
#     if index < len(list):
#         print(list.pop(index))
#     else:
#         print('{} index의 값을 가져올 수 없습니다.'.format(index))
#
# safe_pop_print([1,2,3], 5) # 5 index의 값을 가져올 수 없습니다.


# def safe_pop_print(list, index):
#     try:
#         print(list.pop(index))
#     except IndexError:
#         print('{} index의 값을 가져올 수 없습니다.'.format(index))
#
# safe_pop_print([1,2,3], 5) # 5 index의 값을 가져올 수 없습니다.
#
# # text = '100%'
#
# try :
#     number = int(text)
# except ValueError :
#     print('{}는 숫자가 아닙니다.'.format(text))
#


# # 홀수를 4번 3번 출력
# for i in range(10) :
#     if i % 2 != 0 :
#         print(i)
#         print(i)
#         print(i)
#
# # 홀수를 4번 3번 출력 - continue 활용
# for i in range(10) :
#     if i % 2 = 0 :
#         continue  # 반복문의 나머지를 실행시키지 않고 처음으로 돌아간다
#     print(i)
#     print(i)
#     print(i)
# 제외하는 경우를 첫번째에 처리해서 핵심이 되는 부분이 너무 깊게 들어가지 않다록 한다.

# list = [1, 2, 3, 4, 5, 6, 66, 90, 100]
#
# for val in list:
#     if val % 3 == 0:
#         print(val)
#         break

# patterns = ['가위', '보', '보']
# for p in patterns :
#     print(p)
#
# patterns = ['가위', '보', '보']
# for i in range(len(patterns)): # 0~2
#     print(patterns[i])
#
# patterns = ['가위', '보', '보']
# i = 0
# while i < len(patterns) :
#     print(patterns[i])
#     i = i + 1


# selected = None
# while selected not in ['가위', '바위', '보']:
#     selected = input('가위 바위 보 중에 선택하세요 >')
# print('선택한 값은 : ', selected)



# # 리스트 반복문
# list = [1, 2, 3, 4, 5]
# for i, v in enumerate(list):
#     print('index : {} value: {}'.format(i, v))
#
# # 튜플로 복수 값을 받기 - 리스트 반복문
# list = [1, 2, 3, 4, 5]
# for t in enumerate(list):
#     print('index : {} value: {}'.format(t[0], t[1]))
#
# # 튜플을 쪼개기 - 리스트 반복문
# list = [1, 2, 3, 4, 5]
# for t in enumerate(list):
#     print('index : {} value: {}'.format(*t))
#
#
# # 딕셔너리 반복문
# ages = {'siwa' : 22, 'sunshine' : 25, 'tom' : 30}
# for key, val in ages.items():
#     print('{}의 나이는: {}'.format(key, val))
#
#
# # 튜플로 복수 값을 받기 - 딕셔너리 반복문
# ages = {'siwa' : 22, 'sunshine' : 25, 'tom' : 30}
# for t in ages.items():
#     print('{}의 나이는: {}'.format(t[0], t[1]))
#
#
#
# # 튜플을 쪼개기 - 딕셔너리 반복문
# ages = {'siwa' : 22, 'sunshine' : 25, 'tom' : 30}
# for t in ages.items():
#     print('{}의 나이는: {}'.format(*t))
#




# # 딕셔너리 (dictionary) 선언
# wintable = {
#     '가위' : '보',
#     '바위' : '가위',
#     '보' : '바위'
# }
#
# def rsp(mine, yours) :
#     if mine == yours :
#         return 'draw'
#     elif wintable[mine] == yours :
#         return 'win'
#     else :
#         return 'lose'
#
# result = rsp('가위', '바위')
#
# message = {
#     'draw' : '비겼다',
#     'win' : '이겼다!',
#     'lose' : '졌어..'
# }
#
# print(message[result]) # 졌어..
