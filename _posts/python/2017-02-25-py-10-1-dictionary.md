---
layout: post
title: 파이썬 파트10. 딕셔너리와 튜플 - 딕셔너리
category: python
tags: [python, 파이썬, 딕셔너리]
comments: true
---
# 파이썬 파트10. 딕셔너리와 듀플
> [try hello world 파이썬 입문 강의 ](http://tryhelloworld.co.kr/courses/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%AC%B8)      

## 딕셔너리 만들기
### 딕셔너리
- 자바스크립트 객체(object)와 유사
- 여러 값을 저장해 두고 필요한 값을 꺼내 쓰는 기능
- 이름표를 이용하여 값을 꺼내 사용
- 사용할 때는 리스트와 비슷한 방식

```python
wintable = {
    '가위' : '보',
    '바위' : '가위',
    '보' : '바위',
}

print(wintable['가위'])
```

### 딕셔너리 사용 예시

```python
# 딕셔너리 (dictionary) 선언
wintable = {
    '가위' : '보',
    '바위' : '가위',
    '보' : '바위'
}

def rsp(mine, yours) :
    if mine == yours :
        return 'draw'
    elif wintable[mine] == yours :
        return 'win'
    else :
        return 'lose'

result = rsp('가위', '바위')

message = {
    'draw' : '비겼다',
    'win' : '이겼다!',
    'lose' : '졌어..'
}

print(message[result]) # 졌어..
```

## 딕셔너리 수정하기

### 리스트 수정
```python
# 수정
>>> list = [1, 3, 5, 7, 9, 11]
>>> list[0] = 7
>>> list
[7, 3, 5, 7, 9, 11]

# 추가
>>> list.append(17)
>>> list
[7, 3, 5, 7, 9, 11, 17]

# 삭제 - del()
>>> del(list[0])
>>> list
[3, 5, 7, 9, 11, 17]

# 삭제 - .pop()
>>> list.pop(0)
3 # 삭제되는 값이 반환
>>> list
[5, 7, 9, 11, 17]
```

### 딕셔너리 수정
```python
# 수정
>>> dic = { 'one':1, 'two':2 }
>>> dic['one'] = '하나'
>>> dic
{'one': '하나', 'two': 2}

# 추가
>>> dic['three'] = 3
>>> dic
{'one': '하나', 'two': 2, 'three': 3}
>>>

# 삭제 - del()
>>> del(dic['one'])
>>> dic
{'two': 2, 'three': 3}

# 삭제 - .pop()
>>> dic.pop('two')
2 # 작제되는 값이 반환
>>> dic
{'three': 3}
```

## 딕셔너리 반복문 활용 - for in
- 경우에 따라 가져올 값을 정할 수 있다.

```python
# key 를 가져온다.
>>> ages = {'siwa': 33, 'sunshine': 29, 'tom': 27}
>>> for key in ages.keys():  # keys() 생략 가능
...     print(key)
...
siwa
sunshine
tom

# value를 가져온다.
>>> for value in ages.values():
...     print(value)
...
33
29
27
```

- key와 value 둘 다 가져올 수 있다.

```python
>>> for key, value in ages.items():
...     print('{}의 나이는 {}입니다'.format(key, value))
...
siwa의 나이는 33입니다
sunshine의 나이는 29입니다
tom의 나이는 27입니다
```

- `딕셔너리는 값의 순서를 지키지 않는다.`

## 딕셔너리와 리스트의 비교
### 공통점

구분   | List         |Dictionary
------|--------------|------------
생성   | list=[1,2,3] |dict={'one':1, 'two':2}
호출   | list[0]      | dict['one']
삭제   | del(list[0]) | del(dic['one'])
개수확인| len(list)    | len(dic)
값 확인 | 2 in list    | 'one' in dict.keys()
전부 삭제|  list.clear()| dict.clear()  

###  차이점

구분 | List | Dictionary
--------|------|-----------
순서 | 삭제 시 순서가 바뀌기 때문에 인덱스에 대한 값이 바뀐다 | key로 값을 가져오기 때문에 삭제 여부와 상관 없다
결합 | list1 + list2 | dict1.update(dict2) - 덮어쓰기
