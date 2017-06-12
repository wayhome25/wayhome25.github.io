---
layout: post
title: level 1. 문자열 내림차순으로 배치하기 (java)
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/
tags: [알고리즘, 프로그래밍]
comments: true
---


## 문제
> reverseStr 메소드는 String형 변수 str을 매개변수로 입력받습니다.
str에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 String을 리턴해주세요.
str는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.
예를들어 str이 "Zbcdefg"면 "gfedcbZ"을 리턴하면 됩니다.

## 풀이코드 (java)

```java
import java.util.Arrays;
import java.util.Collections;

public class ReverseStr {
  public String reverseStr(String str){
    String[] array = str.split("");
    Arrays.sort(array);
    Collections.reverse(Arrays.asList(array));
    return  String.join("",array);
  }

// 아래는 테스트로 출력해 보기 위한 코드입니다.
  public static void main(String[] args) {
    ReverseStr rs = new ReverseStr();
    System.out.println( rs.reverseStr("Zbcdefg") );
  }
}
```

## 다른사람 코드

```java
import java.util.Arrays;

public class ReverseStr {
    public String reverseStr(String str){
      char[] sol = str.toCharArray();
      Arrays.sort(sol);
      return new StringBuilder(new String(sol)).reverse().toString();
    }

    // 아래는 테스트로 출력해 보기 위한 코드입니다.
    public static void main(String[] args) {
        ReverseStr rs = new ReverseStr();
        System.out.println( rs.reverseStr("Zbcdefg") );
    }
}
```

```java
import java.util.Arrays;
import java.util.Collections;

public class ReverseStr {
    public String reverseStr(String str){
        String[] array = str.split("");
        Arrays.sort(array,  Collections.reverseOrder());

        return String.join("", array);
    }

    // 아래는 테스트로 출력해 보기 위한 코드입니다.
    public static void main(String[] args) {
        ReverseStr rs = new ReverseStr();
        System.out.println( rs.reverseStr("Zbcdefg") );
    }
}
```
