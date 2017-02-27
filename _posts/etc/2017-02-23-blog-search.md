---
layout: post
title: 지킬 블로그 검색기능 추가 - 구글맞춤검색, 검색라이브러리
category: etc
tags: [검색, 지킬, 블로그검색, google custom search]
comments: true
---

# 지킬 블로그 내용 검색창 추가하기
블로그 글이 점점 늘어나면서 검색창을 추가할 필요성이 생겼다.    
찾아보니 2가지 방법이 있는데 (구글맞춤검색, 라이브러리) 둘 다 장단점이 있는 것 같다.
둘 다 적용해서 사용해본 결과, 검색 정확도를 위해서 구글맞춤검색을 사용하기로 했다.

## 구글 맞춤 검색 (google custom search)

- [구글 맞춤 검색](http://www.google.co.kr/coop) 사이트 접속
- 메뉴에서 `새 검색엔진` 선택
- 필요한 내용을 입력 후 검색엔진 추가
- 메뉴에서  `검색엔진 수정`을 선택하여 검색창 레이아웃 등을 수정 가능
- `코드생성`을 선택하여 해당 코드를 자신의 웹페이지에 추가

<center>
<figure>
<img src="/assets/post-img/etc/search-google.png" alt="">
<figcaption>구글맞춤검색 적용화면</figcaption>
</figure>
</center>

### 장점
- 라이브러리 보다 간편하게 블로그 검색기능을 추가할 수 있다.
- 검색 정확도가 높고 내용을 미리 볼 수 있다.
- 검색 통계를 확인할 수 있다.  

### 단점
- 검색 결과에 구글 광고가 표시된다.     
  (애드센스 계정이 있으면 광고클릭 수익을 자신의 계정으로 돌릴 수 있음, `Make money` 메뉴를 통해 애드센스 계정정보 등록)
- 스타일을 100% 자유롭게 수정하기는 어렵다.


## 라이브러리 추가

- [지킬블로그 검색 라이브러리](https://github.com/christian-fei/Simple-Jekyll-Search)
- 사용방법은 한량님의 블로그에 자세히 설명되어 있어서 생략 [한국어 설명 - 한량넷](http://www.halryang.net/simple-jekyll-search/)

<center>
<figure>
<img src="/assets/post-img/etc/search-lib.png" alt="">
<figcaption>검색라이브러리 적용화면</figcaption>
</figure>
</center>

### 장점
- 스타일을 자신의 취향에 맞추어 자유롭게 수정할 수 있다.

### 단점
- 검색결과가 정확하지 않은 것 같다.
  예를 들어 `카페` 라는 검색어를 입력하면, `카페`라는 단어를 포함하지 않는 글도 검색 결과로 표시된다.
- 라이브러리 적용 중에 내가 실수를 해서 그럴지도 모르겠는데, 한국어 소개글을 올려주신 [한량넷](http://www.halryang.net/simple-jekyll-search/)에서도 검색결과가 정확하지 않은 것을 확인할 수 있었다. 라이브러리를 만드신 분의 [코드]((https://github.com/christian-fei/Simple-Jekyll-Search))에 한국어 검색결과 문제가 있을수도 있겠다.


## 결론
- 디자인을 생각하면 라이브러리를 추가해서 검색창을 만들고 싶었지만, 검색은 정확도가 가장 중요하니 구글 맞춤 검색을 사용하기로 했다.
