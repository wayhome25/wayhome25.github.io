---
layout: post
title: 파이썬 파트17. comprehension - list, dictionary
category: python
tags: [python, 파이썬, list, dictionary, zip]
comments: true
---
# 파이썬 파트17. comprehension - list, dictionary
> [try hello world 파이썬 입문 강의 ](http://tryhelloworld.co.kr/courses/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%AC%B8)      

## List Comprehension (리스트 내포)
- 원하는 구성요소를 가지는 리스트를 `쉽게` 만들 수 있는 기능     
  (한번 익숙해지면, List Comprehension이 없는 다른 프로그래밍 언어는 쓰기 싫어진다고 함)
- 파이썬의 유용한 도구
  - 예1 [ i*i for i in range(1,11) ] # [ 계산식 for문 ]
  - 예2 [ i*i for i in range(1,11) if i % 2 == 0 ] # [ 계산식 for문 조건문 ]
  - 예3 [ ( x, y ) for x in range(15) for y in range(15) ] # [ 계산식 for문 for문 ]

```python
# 길이가 1~10 인 정사각형 중에 길이가 짝수인 정사각형의 넓이 구하기
areas = []
for i in range(1,11):
    if i % 2 == 0:
        areas.extend([i*i])

print('areas :', areas)  # [4, 16, 36, 64, 100]

# list comprehension 방법
areas2 = [i * i for i in range(1,11) if i % 2 ==0]
print('areas2 :', areas2)  # [4, 16, 36, 64, 100]

# for 문을 돌면서 i를 하나씩 가져오고,
# if 조건에 맞는 i만 보낸다.
# 조건에 맞는 i 를 원하는대로 계산해서 리스트에 넣는다.


# 길이가 3*3 인 바둑판의 좌표 만들기
[(x, y) for x in range(3) for y in range(3)]
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
```

## Dictionary Comprehension (딕셔너리 내포))
- 원하는 구성요소를 가지는 딕셔너리를 `쉽게` 만들 수 있는 기능

```python
# 번호를 key로 갖고 이름을 value로 가지는 dictionary 만들기
students = ['몽키', '선샤인', '시와', '톰']
for number, name in enumerate(students):
    print('{}번의 이름은 {}입니다'.format(number+1, name))

# Dictionary Comprehension
students_dic = {
    '{}번'.format(number+1) : name for number, name in enumerate(students)
}

print(students_dic)
```

### zip
- zip(iterable*)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.
- 2개 이상의 리스트나 스트링을 받아서 인덱스에 맞게 for in문에서 하나씩 던져줄 수있게 만들어준다.

```python
students = ['몽키', '선샤인', '시와', '톰']
scores = [85, 92, 78, 100]

for x, y in zip(students, scores):
    print(x, y)
    # 몽키 85
    # 선샤인 92
    # 시와 78
    # 톰 100    
```

### zip을 활용한 dictionary comprehension 만들기

```python
students = ['몽키', '선샤인', '시와', '톰']
scores = [85, 92, 78, 100]

score_dic = {
    students : score for students, score in zip(students, scores)
}

print(score_dic)
# {'몽키': 85, '선샤인': 92, '시와': 78, '톰': 100}
```
