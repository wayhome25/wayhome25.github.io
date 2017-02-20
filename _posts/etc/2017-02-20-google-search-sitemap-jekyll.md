---
layout: post
title: 지킬 블로그 구글 검색 가능하게 하는 방법
category: etc
tags: [jekyll, 지킬, 검색, 구글검색, sitemap]
comments: true
---

# jekyll 블로그 글이 구글에서 검색되도록 만들기

jekyll로 만든 블로그 글은 구글에서 검색이 되지 않는다고 한다.   
구글 검색이 가능하도록 하려면 몇가지 절차가 필요하다.

## 구글 웹마스터 도구(Search Console)에 속성 추가 및 인증
1. [구글 웹 마스터 도구](https://www.google.com/webmasters/tools/home?hl=ko) 접속
2. `속성추가` 버튼을 선택
3. 자신의 jekyll 블로그 주소를 입력하여 속성 추가 (ex.https://wayhome25.github.io/)
4. 구글에서 제공하는 html 다운로드
5. 해당 파일을 자신의 github jekyll 블로그 루트 디렉토리에 올리고 (github 커밋 필요) 확인을 눌러서 인증 완료

## sitemap.xml 파일 작성
1. sitemap.xml 파일을 작성하여 자신의 github jekyll 블로그 루트 디렉토리에 업로드 (github 커밋 필요) [sitemap.xml 내용 참고](https://github.com/wayhome25/wayhome25.github.io/blob/master/sitemap.xml)
2. `주의사항 1` 루트 디렉토리에 존재하는 \_config.yml 파일 내의 url 부분에 자신의 `블로그 url을 입력`해야 sitemap.xml에서 site.url 부분을 사용 할 수 있다.
```
url: https://wayhome25.github.io
```
3. `주의사항 2` sitemap.xml은 [파일링크](https://github.com/wayhome25/wayhome25.github.io/blob/master/sitemap.xml) 내용을 복사&붙여넣기 하여 작성한다. 1~2 행의 `-------` 부분도 포함시켜야 한다.    
(나는 포함시키지 않고 작성해서 여러번 테스트 에러가 발생했다.)    

## 구글 웹마스터 도구(Search Console)에 sitemap.xml 제출
> 구글에게 sitemap.xml을 제출해야 구글이 내 블로그를 크롤링 하는 방식을 판단하고 검색엔진에 노출할 수 있다.

1. [구글 웹 마스터 도구](https://www.google.com/webmasters/tools/home?hl=ko) 접속
2. 자신이 추가한 속성 (블로그)을 선택
3. 왼쪽 메뉴 중 크롤링 > Sitemaps 선택
4. 우측 상단의 `SITEMAP 추가/테스트` 버튼 선택
5. 자신의 github에 커밋한 sitemap.xml 주소를 입력. (ex.https://wayhome25.github.io/ `sitemap.xml`)
6. 테스트 후 문제가 발생하지 않으면 제출


- [참고 글](http://joelglovier.com/writing/sitemaps-for-jekyll-sites)
