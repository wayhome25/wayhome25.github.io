---
layout: post
title: level 1. 삼각형출력하기 (java, python)
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/
tags: [알고리즘, 프로그래밍]
comments: true
---
# level 1. 삼각형출력하기
> [출처](http://tryhelloworld.co.kr/challenge_codes/108)

## 문제
printTriangle 메소드는 양의 정수 num을 매개변수로 입력받습니다.
다음을 참고해 `*`(별)로 높이가 num인 삼각형을 문자열로 리턴하는 printTriangle 메소드를 완성하세요
printTriangle이 return하는 String은 개행문자('\n')로 끝나야 합니다.


## 풀이 (python)

```python
def printTriangle(num):
	s = ""
	for i in range(num):
		s += '*'*(i+1)+'\n'
	return s

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( printTriangle(3) )
```

## 다른사람 풀이

```python
def printTriangle(num):
    return ''.join(['*'*i + '\n' for i in range(1,num+1)])
```

## 배운점
- ''.join(List) 를 통해서 리스트의 각 요소를 그대로 붙여서 스트링으로 만들 수 있다.

---

## 풀이 (java)

```java
public class PrintTriangle {
  public String printTriangle(int num){
    String result = "";
    for(int i=1; i<=num; i++){
      String star = new String(new char[i]).replace("\0", "*");
      result += star + "\n";
    }
    return result;
  }

  // 아래는 테스트로 출력해 보기 위한 코드입니다.
  public static void main(String[] args) {
    PrintTriangle pt = new PrintTriangle();
    System.out.println(pt.printTriangle(3) );
  }
}
```

## 다른사람 풀이

```java
public class PrintTriangle {
    public String printTriangle(int num){
      String result = "";
      String stars = "*";
      for(int i=0; i<num; ++i){
          result += stars+"\n";
          stars += "*";
      }
      return result;
    }

    // 아래는 테스트로 출력해 보기 위한 코드입니다.
    public static void main(String[] args) {
        PrintTriangle pt = new PrintTriangle();
        System.out.println( pt.printTriangle(3) );
    }
}
```

## 배운점
- String 클래스의 replace 메소드
