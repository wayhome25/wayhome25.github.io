---
layout: post
title: firebase 설치 및 설정
category: firebase
tags: [개발, firebase, 파이어베이스]
comments: true
---
# firebase
> 강의URL : [firebase를 이용한 간단한 웹  어플리케이션 만들기](https://www.inflearn.com/course/%ED%8C%8C%EC%9D%B4%EC%96%B4%EB%B2%A0%EC%9D%B4%EC%8A%A4-%EA%B0%95%EC%A2%8C-%EC%9B%B9-%EC%96%B4%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98/)


## 파이어베이스란    
> 파이어베이스는 웹과 모바일(Android, IOS) 개발에 필요한 기능을 제공하는 **BaaS(BackEnd as a Service)  즉, 백엔드 서비스** 입니다.

>기존의 경우 백엔드서비스를 구현하기위하여 **서버구성, 서버아키텍쳐, 인증,DB설계 및 구현등** 모든 기능을 개발해야 하는 수고로움이 있었으나 파이어베이스의 출시로 앞선 수고로움을 대신 해서 시간을 단축 시키고 프론트 엔드개발에 더욱 집중 할 수 있습니다.

## firebase 개발환경설정

### firebase 프로젝트 생성
1. [firebase 콘솔 사이트 이동](https://console.firebase.google.com/)
2. 새 프로젝트 만들기
3. Authentication (인증) 메뉴 이동
4. 로그인방법 중 google 사용설정 on

### 로컬 개발환경 설정
> Firebase를 이용한 웹어플리케이션 구현을 위한 개발환경 설정 방법

1. nodejs 설치 (firebase 설치를 위한 nodejs 설치)
2. Firebase CLI 설치 (CLI : Command Line Interface)
- `$ npm install firebase-tools -g --save`
- `-g` : 모든 터미널에서 firebase 입력시 바로 작동 가능 옵션

3. Firebase Login (컴퓨터와 firebase를 연결하고 프로젝트에 대한 접근을 혀용)
- `$ firebase Login`
- firebase CLI에 로그인 로컬 컴퓨터와 firebase를 연결하고 프로젝트에 대한 접근을 허용
-  `firebase list`
- 프로젝트 리스트 확인

4. Project Directory 초기화 (firebase init)
- `$ mkdir 프로젝트폴더`
- 프로젝트 폴더 생성 후 이동
- `$ firebase init`
- 프로젝트 선택, 기본 db 이름, public directory 사용 (웹앱)
- `firebase.json `: 파이어베이스 환경설정 파일 (호스팅시 기본폴더, path설정, DB 기본 룰셋파일)
- `database.rule.json` : 파이어베이스 기본 데이터베이스 정책

5. Firebase serve
- `$ pwd` 명령으로 프로젝트 폴더인지 확인 (print working directory)
- `$ firebase serve`

### 참고 사이트
- [firebase 가이드 문서](https://firebase.google.com/docs/hosting/)
