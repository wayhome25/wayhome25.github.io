---
layout: post
title: firebase를 활용한 to-do list 웹페이지 만들기
category: firebase
tags: [firebase, 파이어베이스]
comments: true
---
# firebase를 활용한 to-do list 웹페이지를 만들어 보았다.

## 웹페이지 경로
- <https://simple-todolist.firebaseapp.com/>


## 사용언어, 플랫폼
- HTML/CSS
- Javascript
- firebase[^1]
- 화면 UI :  materialize ui framework


## 어려웠던 점
- 모든 유저에게 디폴트로 안내 to-do list를 표시하는 부분
  - 로그인시에 push() 메소드를 통해 안내 내용을 DB로 추가하여 표시
  - 매번 로그인시 안내 내용이 중복으로 추가되는 문제 발생 **(해결필요)**

- 화면을 새로고침 해도 to-do list의 체크박스의 상태가 초기화 되지 않도록 유지
  - DB에서 가져온 특정 체크박스를 자바스크립트, jQuery로 잡아내지 못하는 문제 발생
  - DB에서 화면에 체크박스를 뿌리는 부분에 코드를 넣어서 해결
  - 해당 코드에 대한 **충분한 이해 필요**

- 체크박스 체크시 해당 레이블 텍스트에 취소선 표시
  - CSS로 해결

## 개선하고 싶은 점
- 모바일 화면 적용
- 안내문구 중복 표시 수정

***

  [^1]: 파이어베이스는 안드로이드, iOS 앱 및 모바일웹 개발에 필요한 요소들을 제공하는 백엔드 플랫폼이다. 파이어베이스는 2014년 구글에 인수된 회사로, 데이터베이스, 사용자 인증, 호스팅 등 앱 개발자가 익숙지 않은 백엔드 시스템을 간편히 사용할 수 있게 해준다. ([원문](http://www.zdnet.co.kr/news/news_view.asp?artice_id=20160526171640))  
