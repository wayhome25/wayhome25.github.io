---
layout: post
title: hackerrank - Finding the percentage
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/
tags: [알고리즘, 프로그래밍]
comments: true
---

> [문제출처](https://www.hackerrank.com/challenges/finding-the-percentage/problem)

## 문제

```
You have a record of  students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer  followed by the names and marks for  students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.

Input Format

The first line contains the integer , the number of students. The next  lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.

Constraints

Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

Sample Input

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
Sample Output

56.00
```

---

## 풀이코드

```python
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
score_list = student_marks[query_name]
print("{0:.2f}".format(sum(score_list) / len(score_list)))
```

## 배운점
- asterisk를 통한 가변인자 사용
- [파이썬의 Asterisk(*) 이해하기](https://mingrammer.com/understanding-the-asterisk-of-python)

```python
>>> one, *others = [1, 2, 3, 4, 5]
>>> one
1
>>> others
[2, 3, 4, 5]
```

- "{0:.2f}".format(e) 를 통해서 소수점 2자리 까지만 표시 가능
- [python3 string — Common string operations](https://docs.python.org/3/library/string.html#formatstrings)

```python
>>> print("{0:.2f}".format(56.000))
56.00
```
