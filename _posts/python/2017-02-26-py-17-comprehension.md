---
layout: post
title: 파이썬 파트17. comprehension - list, dictionary
category: python
tags: [python, 파이썬, list, dictionary]
comments: true
---
# 파이썬 파트17. comprehension - list, dictionary
> [try hello world 파이썬 입문 강의 ](http://tryhelloworld.co.kr/courses/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%AC%B8)      

## List Comprehension
- 파이썬의 유용한 도구
- 예1 [ i*i for i in range(1,11) ] # [ 계산식 for문 ]
- 예2 [ i*i for i in range(1,11) if i % 2 == 0 ] # [ 계산식 for문 조건문 ]
- 예3 [ ( x, y ) for x in range(15) for y in range(15) ] # [ 계산식 for문 for문 ]
