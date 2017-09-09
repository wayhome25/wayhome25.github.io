---
layout: post
title: 파이썬 - try, except, finally 안에서 return 사용시 동작순서
category: python
tags: [python, try, finally, except]
comments: true
---
> 개인적인 연습 내용을 정리한 글입니다.      
> 더 좋은 방법이 있거나, 잘못된 부분이 있으면 편하게 의견 주세요. :)

### 의문
아래와 같이 try ~ except 구문에서 return을 사용하면 finally 문은 어떻게 될까?
return문이 사용되면 함수가 그자리에서 바로 종료되지 않을까?

```python
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("0으로 나눌 수 없어요!")
        return False
    else:
        print("결과:", result)
        return True
    finally:
        print("나누기 연산을 종료합니다.")
```

### 확인
확인해보니 finally문은 try ~ except 구문이 종료되기 전에 무조건 실행된다고 한다.
return 이외에 continue, break 에서도 동일하게 동작한다.

> A finally clause is always executed before leaving the try statement, whether an exception has occurred or not. When an exception has occurred in the try clause and has not been handled by an except clause (or it has occurred in a except or else clause), it is re-raised after the finally clause has been executed. The finally clause is also executed “on the way out” when any other clause of the try statement is left via a **break, continue or return statement.**

위의 코드를 실행해보니 아래와 같다.  

```python
>>> divide(6, 0)
0으로 나눌 수 없어요!
나누기 연산을 종료합니다.
False

>>> divide(6, 3)
결과: 2.0
나누기 연산을 종료합니다.
True

>>> divide("칠", "삼")
나누기 연산을 종료합니다.
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-12-f3d6ad32f1c7> in <module>()
----> 1 divide("칠", "삼")

<ipython-input-7-1579274aac92> in divide(x, y)
      1 def divide(x, y):
      2     try:
----> 3         result = x / y
      4     except ZeroDivisionError:
      5         print("0으로 나눌 수 없어요!")

TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

### 참고문서
- [Defining Clean-up Actions](https://docs.python.org/3.3/tutorial/errors.html#defining-clean-up-actions)
