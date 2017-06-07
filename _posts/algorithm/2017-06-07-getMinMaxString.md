---
layout: post
title: level 1. 최대값과 최소값 (Java, Python)
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/
tags: [알고리즘, 프로그래밍]
comments: true
---

> [문제출처](http://tryhelloworld.co.kr/challenge_codes/125#)

Java 공부를 시작하고 처음 풀어본 간단한 알고리즘 문제이다.    
_문자열을 배열로 만드려면 어떻게 하지? 오름차순 정렬은 어떻게 하지?_    
아직 모르는 것이 많지만 이렇게 하나씩 찾아가면서 익히는게 재미있기도 하고 기억에도 잘 남는 것 같다.


파이썬을 처음 공부하고 알고리즘 문제를 풀기 시작했을 때가 생각난다.    
리스트 원소의 합을 구하는 sum() 함수를 찾아보고 메모해둔 글을 다시 읽었는데,  
이렇게 간단한걸 모르던 때도 있었구나 싶었다. (옛날 같은데 그게 겨우 3개월 전이라니!)  

그래도 다행인건 간단한 문제라면 어떻게 접근해서 해결해야겠다는 그림이 그려진다는 것이다.  
그다음에 해야 하는건 원하는 걸 구현하려면 Java의 무슨 메소드, 패키지를 사용해야 하는지 찾아보는 것  
그리고 codility 덕분에 시간복잡도에 대한 고민을 한번 더 할 수 있게 된 것 같다.  

처음이라 약간 막막한 느낌이 들기는 하지만  
이것도 금방 지나가겠지!  

## 문제
> getMinMaxString 메소드는 String형 변수 str을 매개변수로 입력받습니다.
str에는 공백으로 구분된 숫자들이 저장되어 있습니다.
str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 String을 반환하는 메소드를 완성하세요.
예를들어 str이 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.

## 풀이코드

### Java
**접근**
- 문자열을 배열로 변경한다. (.split() 메소드 활용)
- 배열의 각 요소를 정수로 변경하여 새로운 배열(arrayInt)에 담는다. (Integer.parseInt() 활용)
- 배열을 오름차순으로 정렬한다. (Arrays.sort() 활용)
- 맨 처음 요소(최소값) 맨 마지막 요소(최대값)을 문자열로 리턴한다.

**고민**
- sorting 을 하려면 최소 O(N LogN)의 시간복잡도가 발생한다.
- 차라리 배열을 순회하면서 최대값, 최소값을 찾는게 효율적일 것 같다.


```java
import java.util.Arrays;

public class GetMinMaxString2 {
	public String getMinMaxString(String str) {
		String[] array = str.split(" ");
		int[] arrayInt = new int[array.length];

		for (int i = 0; i < arrayInt.length; i++) {
			arrayInt[i] = Integer.parseInt(array[i]); // 배열의 각 요소를 정수로 변경
		}

		Arrays.sort(arrayInt); // 최소 O(N LogN)의 시간복잡도
		String result = arrayInt[0] + " " + arrayInt[arrayInt.length - 1];

		return result;

	}

	public static void main(String[] args) {
		String str = "1 2 3 4";
		GetMinMaxString2 minMax = new GetMinMaxString2();
		System.out.println("최소값과 최대값은?" + minMax.getMinMaxString(str));
	}
}
```


### Python
- min, max 함수를 사용해서 간단하게 구현 가능하다.

```python
def solution(str):
    li = str.split(' ')
    return print("최소값과 최대값은", min(li), max(li))
```

## 다른사람 풀이

```java
public class GetMinMaxString {
	public String getMinMaxString(String str) {
		String[] tmp = str.split(" ");
		int min, max, n;
		min = max = Integer.parseInt(tmp[0]);
		for (int i = 1; i < tmp.length; i++){
			n = Integer.parseInt(tmp[i]);
			if (min > n) min = n;
			if (max < n) max = n;
		}

		return min + " " + max;

	}

	public static void main(String[] args) {
		String str = "1 2 3 4";
		GetMinMaxString minMax = new GetMinMaxString();
		System.out.println("최대값과 최소값은?" + minMax.getMinMaxString(str));
	}

}
```
