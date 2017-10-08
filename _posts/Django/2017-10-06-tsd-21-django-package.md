---
layout: post
title: Django - 서드 파티 패키지
category: Django
tags: [django, package]
comments: true
---
<br>

> [Two Scoops of Django](https://www.twoscoopspress.com/products/two-scoops-of-django-1-11) 21장을 읽고 정리한 내용입니다.     

<br>



- 장고의 진정한 강력함은 오픈 소스 커뮤니티에서 제공하는 파이썬 패키지와 서드파티 장고 패키지들이다.
- 장고와 파이썬 개발 과정에서 전문적으로 이루어지는 작업의 대부분은 서드파티 패키지들을 장고 프로젝트 안으로 이식시키는 것이다.

# 21.1 서드 파티 패키지의 예
- '부록 A 이 책에서 언급된 패키지들' : 우선적으로 고려해볼만한 유용한 패키지 목록

# 21.2 파이썬 패키지 인덱스

- [PyPI](https://pypi.python.org/pypi)는 Python Package Index의 약자
- 파이썬 패키지를 업로드하기 위한 공용 저장소 (현재 장고를 포함하여 11만개 이상의 패키지가 있다)
- pip는 PyPI에서 패키지를 설치하는데 사용하는 명령줄 도구 (파이썬 3.4 이후 기본 포함)

![screen 7](https://i.imgur.com/Y1QMo53.png)
<br>

# 21.3 [djangopackages.org](https://djangopackages.org/)

- djangopackages.org은 장고 앱을 위한 재사용 가능한 앱, 사이트, 도구들을 모아 놓은 디렉토리다.
- 각 패키지의 기능을 비교하기에 가장 좋은 사이트이다.

![screen 9](https://i.imgur.com/gVkdffy.png)
<br>
# 21.4 다양한 패키지를 알아두자
- 장고(파이썬) 개발자로서 필요할 때마다 바퀴(라이브러리)를 다시 만드는 대신에 서드 파티 라이브러리를 이용하는 것을 목표로 삼기를 바란다.
- 다양한 패키지를 이용함에 따라 그 패키지들의 코드를 공부하고 배울 수 있다.
- 동시에 나쁜 패키지들로부터 좋은 패키지를 선별해 내는 능력도 중요하다. (21.10 좋은 장고 패키지의 조건 참고)

# 21.5 패키지 설치, 관리를 위한 도구들
- virtualenv와 pip 설치는 필수 (자세한 내용은 2장 최적화된 장고 환경 꾸미기 참고)
- [홍민희님의 파이썬의 개발 "환경"(env) 도구들](https://spoqa.github.io/2017/10/06/python-env-managers.html)

# 21.6 패키지 요구사항
- 장고와 파이썬의 의존성을 requirements 파일로 관리한다.
- 파일의 위치는 프로젝트 루트 아래 requirements/ 디렉토리

# 21.7 장고 패키지 이용하기: 기본
- 1단계: 패키지 문서 읽기
- 2단계: 패키지 버전 번호를 requirements에 추가하기
- 3단계: virtualenv에 requirements 설치
- 4단계: 패키지의 설치 문서를 그대로 따라하기

# 21.8 서트 파티 패키지에 문제가 생겼을 때
- 패키지 저장소의 이슈 트래커 살펴보기
- 누구도 올린 문제가 아니라면 버그를 보고하기
- 스택오버플로, IRC 활용

# 21.9 자신의 장고 패키지 릴리스 하기
- 장고 문서 참고 :[심화 튜토리얼: 재사용 가능한 앱을 만드는 법](https://docs.djangoproject.com/ko/1.11/intro/reusable-apps/)
- 추가로 다음과 같은 절차를 추천한다.
  - 코드를 포함하는 공개 저장소 생성
  - 파이썬 패키지 인덱스에 패키지를 릴리즈 [Uploading your Project to PyPI](https://packaging.python.org/tutorials/distributing-packages/#uploading-your-project-to-pypi)
  - 패키지를 [djangopackages.org](https://djangopackages.org/)에 추가
  - Read the Docs를 사용하여 스핑크스(Sphinx) 문서 호스팅하기 (23장 참고)

# 21.10 좋은 장고 패키지의 요건

## 목적
- 패키지 이름은 목적과 기능을 잘 설명할 수 있어야하 한다.
- 장고에 관련된 패키지는 저장소의 루트 폴더를 django- 라는 접두어로 시작하게 한다.

## 범위
- 패키지 자체의 역할 범위는 작은 태스크에만 초점이 맞추어져야 한다.

## 문서화
- reStructuredText(마크업 언어의 한 종류로 파씽시스템도 포함)를 활용하여 문서작성
- 스핑크스를 사용하면 잘 정돈된 버전의 문서를 제작 가능 (Rst문서를 HTML, PDF 등으로 변환)
- 23장 문서화에 집착하자 참고
- [[Pycon KR 2017] Rst와 함께하는 Python 문서 작성 & OpenStack 문서 활용 사례](https://www.slideshare.net/ianychoi/pycon-kr-2017-rst-python-openstack)

## 테스트
- 제작되는 패키지는 반드시 테스트를 거쳐야한다.
- 테스트는 다른 사람들이 좀 더 효과적으로 패키지에 공헌할 수 있게 해준다.

## 템플릿
- 최근에는 뼈대 역할을 하는 템플릿 세트를 제공하는 것이 표준 (css는 제외한 상태로 최소한의 html, 자바스크립트)

## 유지보수
- 저장소에 마이너, 메이저 릴리스 코드를 업데이트 하면 파이썬 패키지 인덱스에도 자동으로 업데이트 하도록 고려

## 커뮤니티
- 모든 기여자에게 해당 작업에 대한 귀속 조건을 담은 CONTRIBUTORS.rst나 AUTHORS.rst 파일을 제공해야 한다.
![screen 10](https://i.imgur.com/GQ0hmmB.png)

## 모듈성
- 패키지는 장고 프로젝트의 코어 컴포넌트(템플릿, ORM 등)를 다른 모듈로 교체하지 않고도 문제 없이 적용되어야 한다.
- 설치는 기존 프로젝트에 최소한의 영향을 미쳐야 한다.

## 파이썬 패키지 인덱스에 올리기
- 패키지의 모든 메이저, 마이너 릴리스는 PyPI에서 다운로드 할 수 있도록 해야한다.

## 가능한 자세하게 requirements 스펙을 작성하기
- setup.py 파일 안에 정의되는 installed_requires 인자에는 제작된 서드파티 라이브러리를 이용하기 위해 어떤 다른 종류의 패키지가 필요한지 정보가 담겨있다.
- 이를 가능한 다양한 환경과 호환되도록 설정해야한다.
- 요구되는 라이브러리가 단 하나의 버전만으로 매우 좁게 정의되어 있으면 다른 개발자의 다른 사이트 프로젝트에서는 해당 패키지가 작동할 수 없는 상황이 발생한다.
- 따라서 서드 파트 패키지들의 requirements를 다른 패키지들의 라이브러리 호환성을 위해 가능 한 넓게 기술해야 한다.

```python
Django>=1.5,<1.9
requirements>=1.2.3,<=2.6.0
```

## 버전 번호 붙이기
- 장고, 파이썬처럼 [PEP386](https://www.python.org/dev/peps/pep-0386/) 이름 규약에 따라서 버전 번호를 붙이는 방법을 선호
- 'A. B. C' 패턴
  - A : 메이저 버전 번호
  - B : 마이너 버전 번호
  - C : 버그 수정 릴리스 (마이크로 릴리스)
  - [참고 : 위키-소프트웨어 버전 작성](https://ko.wikipedia.org/wiki/%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4_%EB%B2%84%EC%A0%84_%EC%9E%91%EC%84%B1)
-  alpha, beta, rc(release-candidate) 접미사는 앞으로 릴리스될 버전에 대해서 이용
  (예: django-crispy-forms 1.4.0-beta)
- 완성되지 않은 코드를 PyPI에 올려서는 안된다.
  - PyPI는 알파, 베타, rc 코드가 아닌 안정적이고 신뢰할 수 있는 패키지만 모아 놓은 공간  

## 이름
- 오픈소스 장고 패키지 이름 정하기 팁
  - 파이썬 패키지 인덱스에 이미 등재된 이름인지
  - djangopackages.org에 이름이 있는지

## 라이센스
- 완성된 패키지 저장소의 루트에 LICENSE.rst 파일을 제작하자
- 개인이라면 MIT 라이센스를 추천한다.

## URL Namespaces 이용
- URL Namespaces 이용을 통해서 프로젝트들 사이에서 서로 충돌이 나는 것을 막을 수 있다.

<br>
# 쉬운 방법으로 패키지 제작하기
- [cookiecutter](https://github.com/audreyr/cookiecutter)를 사용하여 프로젝트 템플릿을 쉽게 만들어 보자
<br>
<br>
# 오픈 소스 패키지 관리하기
## 풀 요청에 대한 보상
- CONTRIBUTORS.txt 또는 AUTHORS.txt 같은 프로젝트 저작자 문서를 만들고 공헌한 사람들의 이름을 반드시 넣어야 한다.

![screen 10](https://i.imgur.com/yu4PTB3.png)

## 반영될 수 없는 풀 요청에 대해
- 테스트 케이스를 통과하지 못한 풀 요청 (22장 참고)
- 테스트 범위를 벗어난 코드들 (22장 참고)
- 풀 요청은 가능한 한 최소의 범위에 대한 수정과 변경을 담고 있어야 한다.
- 너무 복잡한 코드
- PEP8 규약을 따르지 않는 코드
- 빈 칸 정리로만 이루어진 코드

## 파이썬 패키지 인덱스에 정식으로 릴리스하기
- PyPI에 올라온 패키지의 버전이 예전 버전이라고 해서 스테이블 마스터나 트렁크 브랜치를 이용하라고 하는 것은 무책임한 일로 간주된다.
- 오픈소스 프로젝트의 저장소는 제품 품질을 지닌 코드로 볼 수 없으며,
  파이썬 패키지 인덱스는 설치 가능한 패키지를 안전하게 제공하는 리소스로 설계되어 있음
- 명확하게 언제 릴리스 해야하는지는 [python-request의 변경이력](https://github.com/requests/requests/blob/master/HISTORY.rst)을 참고하면 좋다.
- 트와인(Twine)은 파이썬 패키지 인덱스로 패키지를 올리는데 사용되는 라이브러리
- 인증된 TLS를 이용해 패키지를 업로드 함으로써 SSH 연결을 이용하지 않는 python setup.py의 보안 문제를 해결한다.
- 참고
  - [나만의 파이썬 패키지를 작성하는 법](https://code.tutsplus.com/ko/tutorials/how-to-write-your-own-python-packages--cms-26076)  


## 기본 예제 템플릿을 제공하라
- 제작된 프로젝트를 이용한 기본적인 에제 템플릿을 제공하면 이용을 고려할 때 패키지를 테스트하기 쉽기 때문에 도움이 된다.

## 패키지의 수명
- 프로젝트에 활동적으로 참여하는 사람에게 권한을 넘겨줌으로써 해당 프로젝트가 다시 활성화 될 수 있다.
- 예시 : pip/virtualenv, django-debug-toolbar, django-uni-form 등
