# 리스트 반복문
list = [1, 2, 3, 4, 5]
for i, v in enumerate(list):
    print('index : {} value: {}'.format(i, v))

# 튜플로 복수 값을 받기 - 리스트 반복문
list = [1, 2, 3, 4, 5]
for t in enumerate(list):
    print('index : {} value: {}'.format(t[0], t[1]))

# 튜플을 쪼개기 - 리스트 반복문
list = [1, 2, 3, 4, 5]
for t in enumerate(list):
    print('index : {} value: {}'.format(*t))


# 딕셔너리 반복문
ages = {'siwa' : 22, 'sunshine' : 25, 'tom' : 30}
for key, val in ages.items():
    print('{}의 나이는: {}'.format(key, val))


# 튜플로 복수 값을 받기 - 딕셔너리 반복문
ages = {'siwa' : 22, 'sunshine' : 25, 'tom' : 30}
for t in ages.items():
    print('{}의 나이는: {}'.format(t[0], t[1]))



# 튜플을 쪼개기 - 딕셔너리 반복문
ages = {'siwa' : 22, 'sunshine' : 25, 'tom' : 30}
for t in ages.items():
    print('{}의 나이는: {}'.format(*t))





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
