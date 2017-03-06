---
layout: post
title: 파이썬 파트12. 예외처리 - try / except, raise
category: python
tags: [python, 파이썬, raise, 예외]
comments: true
---
# 파이썬 파트12. 예외처리
> [try hello world 파이썬 입문 강의 ](http://tryhelloworld.co.kr/courses/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%AC%B8)      

## try / except
- 파이썬으로 프로그래밍 중에 다양한 에러가 발생할 수 있다. 이 에러가 발생하는 예외상황은 유연하게 프로그래밍을 할 수 있는 도구가 되기도 한다.

### 에러 예시

```python
# IndexError
>>> list = []
>>> list[0]
IndexError: list index out of range

# ValueError
>>> text = 'abc'
>>> number = int(text)
ValueError: invalid literal for int() with base 10: 'abc'
```

### try / except문 사용 예시
- 에러가 발생할 것 같은 코드를 try안에 넣고 except 뒤에 발생할 수 있는 에러의 이름을 적어두면,
  에러 발생시 `프로그램이 멈추지 않고` 별도 처리가 가능하다.

<center>
<figure>
<img src="/assets/post-img/python/exception.png" alt="views">
<figcaption>exception 처리</figcaption>
</figure>
</center>

```python
text = '100%'

try :
    number = int(text) # 에러가 발생할 가능성이 있는 코드
except ValueError :  # 에러 종류
    print('{}는 숫자가 아닙니다.'.format(text))  #에러가 발생 했을 경우 처리할 코드
```

- 경우에 따라 예외 처리 대신 if else를 사용 할 수 있다.   
  더 간결한 것이나, if문을 사용하는 것이 좋다.

```python
# try-except 문
def safe_pop_print(list, index):
    try:
        print(list.pop(index))
    except IndexError:
        print('{} index의 값을 가져올 수 없습니다.'.format(index))

safe_pop_print([1,2,3], 5) # 5 index의 값을 가져올 수 없습니다.

# if 문
def safe_pop_print(list, index):
    if index < len(list):
        print(list.pop(index))
    else:
        print('{} index의 값을 가져올 수 없습니다.'.format(index))

safe_pop_print([1,2,3], 5) # 5 index의 값을 가져올 수 없습니다.
```

- try 문으로만 해결이 가능한 문제도 있다.

```python
try:
    import your_module
except ImportError:
    print('모듈이 없습니다.')
```

## 예외 이름을 모르는 경우 처리 방법

```python
# 모든 에러 처리
try:
    list = []
    print(list[0])  # 에러가 발생할 가능성이 있는 코드

    text = 'abc'
    number = int(text)
except:
    print('에러발생')

# 에러 이름 확인
try:
    list = []
    print(list[0])  # 에러가 발생할 가능성이 있는 코드

except Exception as ex: # 에러 종류
    print('에러가 발생 했습니다', ex) # ex는 발생한 에러의 이름을 받아오는 변수
    # 에러가 발생 했습니다 list index out of range
```

## 에러를 직접 일으키는 방법 - raise
- 사용자가 직접 에러를 발생시키는 기능
- 많이 사용하면 코드를 읽기 어려워진다.

```python
# 올바른 값을 넣지 않으면 에러를 발생시키고 적당한 문구를 표시한다.
def rsp(mine, yours):
    allowed = ['가위','바위', '보']
    if mine not in allowed:
        raise ValueError
    if yours not in allowed:
        raise ValueError

try:
    rsp('가위', '바')
except ValueError:
    print('잘못된 값을 넣었습니다!')
```

```python
# 190이 넘는 학생을 발견하면 반복을 종료한다.
school = {'1반' : [150, 156, 179, 191, 199], '2반' : [150, 195, 179, 191, 199]}

try:
    for class_number, students in school.items():
        for student in students:
            if student > 190:
                print(class_number, '190을 넘는 학생이 있습니다.')
                # break # 바로 상위 for문은 종료되지만 최고 상위 for문은 종료되지 않는다.
                raise StopIteration
                # 예외가 try 문 안에 있지 않으면 에러 발생시 프로그램이 멈춘다.
except StopIteration:
    print('정상종료')                
```
