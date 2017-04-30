---
layout: post
title: codility - OddOccurrencesInArray
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/
tags: [알고리즘, 프로그래밍]
comments: true
---

> [문제출처](https://codility.com/programmers/lessons/1-iterations/)

## 문제

A non-empty zero-indexed array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Assume that:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1),

beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.


## 풀이과정
- 빈 배열 idxs 를 정의
- list A 를 for문으로 순환하면서 해당 item과 동일한 요소가 list A 안에 있다면
  - 배열 idxs 에 해당하는 요소들의 index 값을 추가한다.
  - 배열 idxs 에 추가된 index에 해당하는 요소들은 비교를 수행하지 않는다.(continue 처리)
-  list A 를 for문으로 순환하면서 해당 item과 동일한 요소가 list A 안에 없다면
  - 해당 item을 리턴한다.

## 풀이코드
- detected time complexity: O(N**2)
- for 문 안에서 if 문을 통해 배열을 탐색 => N^2
- 시간복잡도 O(N**2)이라서 몇가지 테스트는 시간 초과로 통과하지 못했다.

```python
def solution(A):
    idxs = []
    for idx, item in enumerate(A):
        if idx in idxs:
            continue
        elif item in A[idx+1:]:
            idxs.append(idx)
            idxs.append(A[idx+1:].index(item) + idx + 1)
        else:
            return item
```

##  다른사람 코드 1
- Detected time complexity: O(N) or O(N*log(N))
- 파이썬에서 sorted() 메소드는 O(N*log(N)) 의 성능을 가진다고 한다.
- 간단하고 빠르다! 이렇게 단순하게 문제에 접근하는 습관을 들여야겠다. 이런 코드 좋다 :)

```python
def test3(A):
    if len(A) == 1:
        return A[0]

    A = sorted(A)
    print(A)
    for i in range(0, len(A), 2):
        if i+1 == len(A):
            return A[i]
        if A[i] != A[i+1]:
            return A[i]

test3([1,2,1,2,3])
```

##  다른사람 코드 2

- Detected time complexity: O(N) or O(N*log(N))
- 한 줄로 풀어버리다니..
- 파이썬의 ^ 연산자에 대한 [설명](https://www.tutorialspoint.com/python/bitwise_operators_example.htm)
- 2개의 수를 2진수로 바꿔서 비교한다. 각 자리수가 같으면 0, 다르면 1

```python
def solution(A):
  return reduce(lambda x,y: x^y, A)
```
