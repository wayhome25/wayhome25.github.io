---
layout: post
title: level 1. 수박수박수박수박수박수? (java, python)
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/

tags: [알고리즘, 프로그래밍]
comments: true
---
# level 1. 수박수박수박수박수박수?
> [출처](http://tryhelloworld.co.kr/challenge_codes/108)

## 문제
water_melon함수는 정수 n을 매개변수로 입력받습니다.
길이가 n이고, 수박수박수...와 같은 패턴을 유지하는 문자열을 리턴하도록 함수를 완성하세요.

예를들어 n이 4이면 '수박수박'을 리턴하고 3이라면 '수박수'를 리턴하면 됩니다.

## 풀이 (python)
```python
def water_melon(n):
    return ("수박"*n)[:n]

# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(3));
print("n이 4인 경우: " + water_melon(4));
```

## 풀이 (java)

```java
public class WaterMelon {
	public String watermelon(int n){
    String result="";

		for(int i=1; i<n+1; i++){
      result += (i % 2 == 1)? "수" : "박";
			}
    return result;
	}

	// 실행을 위한 테스트코드입니다.
	public static void  main(String[] args){
		WaterMelon wm = new WaterMelon();
		System.out.println("n이 3인 경우: " + wm.watermelon(3));
		System.out.println("n이 4인 경우: " + wm.watermelon(4));
	}
}
```
## 다른사람 풀이(java)

```java
public class WaterMelon {
    public String watermelon(int n){
        StringBuffer sf = new StringBuffer();
        for (int i=1; i<=n; ++i) {
            sf.append(i%2==1?"수":"박");
        }
        return sf.toString();
    }

    // 실행을 위한 테스트코드입니다.
    public static void  main(String[] args){
        WaterMelon wm = new WaterMelon();
        System.out.println("n이 3인 경우: " + wm.watermelon(3));
        System.out.println("n이 4인 경우: " + wm.watermelon(4));
    }
}
```

```java
public class WaterMelon {
	public String watermelon(int n){
		String repeated = new String(new char[n]).replace("\0", "수박");
    return repeated.substring(0,n);
	}

	// 실행을 위한 테스트코드입니다.
	public static void  main(String[] args){
		WaterMelon wm = new WaterMelon();
		System.out.println("n이 3인 경우: " + wm.watermelon(3));
		System.out.println("n이 4인 경우: " + wm.watermelon(4));
	}
}
```

## 배운점
- 슬라이싱 기능을 잘 활용하자
- java 3항 연산자
- replace 메소드
- [StringBuffer](https://slipp.net/questions/271#answer-1049) 클래스 (String클래스와 달리 동적 문자열을 처리하는 클래스)
- toString 메소드
