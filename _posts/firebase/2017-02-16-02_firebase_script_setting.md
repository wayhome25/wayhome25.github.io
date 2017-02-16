---
layout: post
title: firebase 스크립트 파일, materialize ui framework
category: firebase
tags: [firebase, 파이어베이스]
comments: true
---

# 설정스크립트, 코딩흐름소개
- MemoApp index.html
  - UI툴 : [materialize ui framework](http://materializecss.com/)
  - 기본구조
    - 메모를 입력하고 다른 포커스를 주면 메모 리스트 생성
    - 신규메뉴버튼을 눌러 신규 메모 생성

## 스트립트 파일  적용
- [firebase console](https://console.firebase.google.com)이동
- 웹 앱에 firebase 추가 선택
- 해당 snippet을 index.html에 붙여넣기


## 기능구현 순서
1. 인증기능을 이용한 구글창 호출
2. 구글인증
  - 성공 > 메모리스트 출력
  - 실패 > 구글창 다시 호출
3. 메모 저장기능
4. 메모 한건 출력기능
5. 메모 수정 기능
6. 메모 삭제 기능
