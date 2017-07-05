---
layout: post
title: 파이썬 자료형 별 주요 연산자의 시간 복잡도 (Big-O)
category: python
comments: true
---

## 들어가기

알고리즘 문제를 풀다 보면 시간복잡도를 생각해야 하는 경우가 종종 생긴다.
특히 [codility](https://codility.com)는 문제마다 시간복잡도 기준이 있어서,
기준을 넘기지 못하면 문제를 풀어도 score가 50 이하로 나오는 경우가 많다.

찾아보니 파이썬 주요 함수, 메소드의 시간복잡도를 정리한 페이지가 있었다. ([Complexity of Python Operations](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt))
자주 사용하는 것들을 이곳에 정리하고 종종 참고하려고 한다.  


## list

Operation     | Example      | Big-O         | Notes|
--------------|--------------|---------------|-------------------------------|
Index         | l[i]         | O(1)	     ||
Store         | l[i] = 0     | O(1)	     ||
Length        | len(l)       | O(1)	     ||
Append        | l.append(5)  | O(1)	     ||
Pop	      | l.pop()      | O(1)	     |  l.pop(-1) 과 동일|
Clear         | l.clear()    | O(1)	     | l = [] 과 유사|
Slice         | l[a:b]       | O(b-a)	     | l[:] : O(len(l)-0) = O(N)|
Extend        | l.extend(...)| O(len(...))   | 확장 길이에 따라 |
Construction  | list(...)    | O(len(...))   | 요소 길이에 따라 |
check ==, !=  | l1 == l2     | O(N)          | 비교 |
Insert        | ㅣ.insert(i, v) | O(N)	     | i 위치에 v를 추가|
Delete        | del l[i]     | O(N)	     ||
Remove        | l.remove(...)| O(N)	     ||
Containment   | x in/not in l| O(N)	     | 검색|
Copy          | l.copy()     | O(N)	     | l[:] 과 동일 - O(N)|
Pop	      | l.pop(i)     | O(N)	     | l.pop(0):O(N)|
Extreme value | min(l)/max(l)| O(N)	     | 검색|
Reverse	      | l.reverse()  | O(N)	     | 그대로 반대로|
Iteration     | for v in l:  | O(N)          ||
Sort          | l.sort()     | O(N Log N)    ||
Multiply      | k*l          | O(k N)        | [1,2,3] * 3 >> O(N**2)|


## Dict


Operation     | Example      | Big-O     | Notes |
--------------|---------------|------------|---------|
Index         | d[k]         | O(1)	     ||
Store         | d[k] = v     | O(1)	     ||
Length        | len(d)       | O(1)	     ||
Delete        | del d[k]     | O(1)	     ||
get/setdefault| d.method     | O(1)	     ||
Pop           | d.pop(k)     | O(1)	     ||
Pop item      | d.popitem()  | O(1)	     ||
Clear         | d.clear()    | O(1)	     | s = {} or = dict() 유사|
View          | d.keys()     | O(1)	     | d.values() 동일|
Construction  | dict(...)    | O(len(...))   | |
Iteration     | for k in d:  | O(N)          | |

---

# reference
- [Python wiki's Time Complexity](https://wiki.python.org/moin/TimeComplexity)
- [Python Set Slice Complexity](http://techqa.info/programming/question/34356780/python-set-slice-complexity)
- [Complexity of Python Operations](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)
