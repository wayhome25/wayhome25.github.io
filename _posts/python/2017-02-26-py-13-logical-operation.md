---
layout: post
title: 파이썬 파트13. 논리연산과 if문 더 알아보기
category: python
tags: [python, 파이썬, 논리연산]
comments: true
---
# 파이썬 파트13. 논리연산과 if문 더 알아보기
> [try hello world 파이썬 입문 강의 ](http://tryhelloworld.co.kr/courses/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%AC%B8)      

## 논리연산의 단락평가
- `단락평가` : 논리연산에서 코드의 앞만 보고 값을 정할 수 있는 경우 뒤는 보지 않고 값을 결정
- 복잡한 코드를 단순하게 하는 방식

```python
dic = { 'key2' : 'value2' }

if 'key1' in dic and dic['key1'] == 'value2': # 단락평가를 통해 첫번째 조건이 false 이기에 바로 확인 종료
# if dic['key1'] == 'value2' and 'key1' in dic: => dic['key1'] 에서 에러 발생
    print('있네!')
else:
    print('없네..')
```

## bool 값과 논리연산의 활용
- 숫자 0을 제외한 모든 수 - true
- 빈 딕셔너리, 빈 리스트를 제외한 모든 딕셔너리, 리스트 - true
- 아무 값도 없다는 의미인 None - false
- 빈문자열을 제외한 모든 문자열 - true

```python
>>> bool(9) #True
>>> bool(-1) #True
>>> bool(0) #False
>>> bool(None) #False
>>> bool('') #False
>>> bool([]) #False
```
### 논리연산의 활용
- 파이썬을 더 강력하게 만들어 주는 도구

```python
value = input('입력해주세요>') or '아무것도 없어'
# input이 빈 경우 값은 false => 단락평가로 인해 or 뒤의 값으로 적용됨
print('입력값 : ', value)
# input 값이 있는경우 input 값, 없는경우 '아무것도 없어' 출력  
```
