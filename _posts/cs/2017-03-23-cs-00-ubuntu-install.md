---
layout: post
title: 강의노트 00. 우분투(ubuntu) 설치
category: 컴퓨터공학
permalink: /cs/:year/:month/:day/:title/
tags: 
comments: true
---
# 우분투(ubuntu)
- Debian GNU/Linux에 기초한 컴퓨터 운영체제로, `리눅스 배포판`이다.
- 데비안 GNU/리눅스와 견주어 볼 때 사용자 편의성에 많은 초점을 맞추고 있다.
- 일반적으로 우분투 운영 체제 사용자들 사이에서,
  우분투는 반투어로 __네가 있으니 내가 있다__ 라는 의미로 사용되고 있다.

---

# 우분투 설치

## ubuntu 이미지 다운로드
- 다운로드 메뉴의 desktop 항목에서 [다운로드](https://www.ubuntu.com/download/desktop) 진행
- 우분투 이미지 파일 다운로드


## VirtualBox 설치
- 버추얼박스 :  리눅스, OS X, 솔라리스, 윈도를 게스트 운영 체제로 가상화하는 x86 가상화 소프트웨어
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads) 다운로드 메뉴에서 환경에 맞는 파일을 다운로드
- 설치후 새로 만들기 선택
  - 이름을 ubuntu로 지정 (종류, 버전 항목은 자동 선택 됨)
  - 메모리 크기는 1600MB 정도 할당 (붉은 색을 넘어가면 원래 운영체제가 느려지는 문제 발생)
  - 파일 크기는 40G 정도 할당
- 시작을 눌러 가상머신 시작
  - 시동디스크로 다운로드 받은 ubuntu 이미지 파일 선택
  - 가상머신이기 때문에 디스크를 지우고 Ubuntu 설치 선택
  - 키보드는 한국어(101/104키 호환 선택)
  - 이름은 영문으로 설정
