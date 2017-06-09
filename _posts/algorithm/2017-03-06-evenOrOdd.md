---
layout: post
title: level 1. 짝수와 홀수 - 삼항연산자 (Java, Python)
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/

tags: [알고리즘, 프로그래밍]
comments: true
---
# level 1. 짝수와 홀수
> [출처](http://tryhelloworld.co.kr/challenge_codes/121)

## 문제
evenOrOdd 메소드는 int형 num을 매개변수로 받습니다.
num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하도록 evenOrOdd에 코드를 작성해 보세요.
num은 0이상의 정수이며, num이 음수인 경우는 없습니다.

## 풀이 (python)

```python
def evenOrOdd(num):
	return 'Odd' if num % 2 else 'Even'

#아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + evenOrOdd(3))
print("결과 : " + evenOrOdd(2))
```


## 다른사람 풀이 (Python)

```python
def evenOrOdd(num):
    if num%2==0 :
        s = "Even"
    else :
        s = "Odd"

    return s
```

## 배운점
- 파이썬에도 삼항연산자가 있다는걸 배웠다.
- `a if test else b` : test가 true일 경우 a를, 그렇지 않으면 b를 리턴한다.

---

## 풀이 (Java)

```java
public class EvenOrOdd {
    String evenOrOdd(int num) {
        String result;
      	if(num % 2 == 1){
          result = "Odd";
        }else{
          result = "Even";
        }
        return result;
    }

    public static void main(String[] args) {
        String str = "1 2 3 4";
        EvenOrOdd evenOrOdd = new EvenOrOdd();
        //아래는 테스트로 출력해 보기 위한 코드입니다.
        System.out.println("결과 : " + evenOrOdd.evenOrOdd(3));
        System.out.println("결과 : " + evenOrOdd.evenOrOdd(2));
    }
}
```

## 다른사람 풀이 (Java)

```java
public class EvenOrOdd {
    String evenOrOdd(int num) {
        return (num % 2 == 0) ? "Even" : "Odd";
    }

    public static void main(String[] args) {
        EvenOrOdd evenOrOdd = new EvenOrOdd();
        //아래는 테스트로 출력해 보기 위한 코드입니다.
        System.out.println("결과 : " + evenOrOdd.evenOrOdd(3));
        System.out.println("결과 : " + evenOrOdd.evenOrOdd(2));
    }
}
```
