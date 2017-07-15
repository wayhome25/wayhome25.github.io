---
layout: post
title: level 2. 이상한 문자 만들기
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/

tags: [알고리즘, 프로그래밍]
comments: true
---
# level 2. 이상한 문자 만들기
> [출처](http://tryhelloworld.co.kr/challenge_codes/115)

## 문제
toWeirdCase함수는 문자열 s를 매개변수로 입력받습니다.
문자열 s에 각 단어의 짝수번째 인덱스 문자는 대문자로, 홀수번째 인덱스 문자는 소문자로 바꾼 문자열을 리턴하도록 함수를 완성하세요.
예를 들어 s가 "try hello world"라면 첫 번째 단어는 "TrY", 두 번째 단어는 "HeLlO", 세 번째 단어는 "WoRlD"로 바꿔 "TrY HeLlO WoRlD"를 리턴하면 됩니다.

주의 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단합니다.

## 풀이 (python)

### 1
map을 활용해서 풀었다.

```python
def toWeirdCase(s):
    def change(t):
        result = ""
        for i, v in enumerate(t):
            if i % 2:  # 홀수
                result += v.lower()
            else:  # 짝수
                result += v.upper()
        return result
    return ' '.join(list(map(change, s.split())))


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(toWeirdCase("try hello world")));
```
### 2
```python
def toWeirdCase(s):    
	s = s.split()
	i = 0
	j = 0
	while i < len(s):
		for j, v in enumerate(s[i]):
			if j % 2 == 1:
				s[i] = s[i][:j] + s[i][j:].replace(v, v.lower(), 1)
			else:
				s[i] = s[i][:j] + s[i][j:].replace(v, v.upper(), 1)
		i += 1       
	return ' '.join(s)


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(toWeirdCase("try hello world")));
```

## 다른사람 풀이
```python
def toWeirdCase(s):    
  return ' '.join(''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split())
```

## 배운점
- 문자열은 인덱스를 통해서 문자열 일부를 수정 교체 할 수 없다.
- 문자열을 수정하려면 replace를 하거나, + 연산자를 사용해야 한다.
- `3항 연산자`를 잘 활용하자 A if 조건 else B
