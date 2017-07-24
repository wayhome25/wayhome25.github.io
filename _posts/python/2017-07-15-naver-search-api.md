---
layout: post
title: 파이썬 - 네이버 검색 Open API를 이용하여 책 검색하기
category: python
tags: [python, api]
comments: true
---

> 개인적인 연습 내용을 정리한 글입니다.      
> 더 좋은 방법이 있거나, 잘못된 부분이 있으면 편하게 의견 주세요. :)

<br>

# 들어가기
개발을 공부하면서 API 라는 단어는 많이 들어보았다. 하지만 구체적으로 API가 무엇인지 언제 어떻게 사용하는지에 대한 개념이 모호한 상태였다.

최근 친구와 함께 [AskDjango 해커톤](https://nomade.kr/moim/askdjango-hackathon-2017/)에 참여하기로 했다. 주제는 책에 관련된 것으로 하고, 교보문고와 같은 사이트에서 책 정보를 크롤링으로 가져오자는 의견이 있었다. 크롤링 보다 더 좋은 방법이 있지 않을까 하는 생각이 들어서 고민 중이었는데, 마침 참여 중인 [8퍼센트 스터디](https://8percent.github.io/2017-06-30/%EC%8A%A4%ED%84%B0%EB%94%94%EC%8B%9C%EC%9E%91/)에서 도서검색 API에 대한 이야기가 나왔다. 찾아보니 네이버에서 [검색 API](https://developers.naver.com/products/intro/plan/)를 제공하고 있었고, 테스트를 해보니 아주 간편하게 원하는 도서 정보를 가져올 수 있었다. (이걸 모르고 크롤링을 하려고 했다니..!)

구체적인 API 사용법에 대해서는 [네이버 API 사이트](https://developers.naver.com/docs/common/openapiguide/) 에서 확인할 수 있다. 여기서는 샘플로 제공하는 API 호출 코드의 각각의 기능에 대해서 공부할 겸 정리하려고 한다.

---

## 코드개요
- 네이버 책 검색 API를 활용하여 '파이썬'이 포함된 검색결과를 JSON으로 가져온다.
- 조건
  - 검색어 : '파이썬' (query)
  - 검색결과는 3개 출력 (display=3)
  - 정렬 옵션 : 판매량순 (sort=count)

 ```python
 import urllib.request
 client_id = "MY_CLIENT_ID" # 애플리케이션 등록시 발급 받은 값 입력
 client_secret = "MY_CLIENT_SECRET" # 애플리케이션 등록시 발급 받은 값 입력
 encText = urllib.parse.quote("파이썬")
 url = "https://openapi.naver.com/v1/search/book?query=" + encText +"&display=3&sort=count"
 request = urllib.request.Request(url)
 request.add_header("X-Naver-Client-Id",client_id)
 request.add_header("X-Naver-Client-Secret",client_secret)
 response = urllib.request.urlopen(request)
 rescode = response.getcode()
 if(rescode==200):
     response_body = response.read()
     print(response_body.decode('utf-8'))
 else:
     print("Error Code:" + rescode)
 ```

- JSON 형식의 결과 데이터는 [json.loads()](https://docs.python.org/3/library/json.html?highlight=json.loads#json.loads) 메소드를 통해서 파이썬에서 활용 가능한 객체 (예: dict) 로 변환하여 사용한다.

```python
import json
json_rt = response.read().decode('utf-8')
py_rt = json.loads(json_rt)
```

#### 결과값 예시
- JSON 형식으로 예쁘게 결과값을 가져온다.

```
{
    "lastBuildDate": "Sat, 15 Jul 2017 18:28:50 +0900",
    "total": 486,
    "start": 1,
    "display": 3,
    "items": [
        {
        "title": "Do it! 점프 투 <b>파이썬</b> (이미 50만 명이 '점프 투 <b>파이썬</b>'으로 시작했다!)",
        "link": "http://book.naver.com/bookdb/book_detail.php?bid=10290989",
        "image": "http://bookthumb.phinf.naver.net/cover/102/909/10290989.jpg?type=m1&udate=20160528",
        "author": "박응용",
        "price": "18800",
        "discount": "16920",
        "publisher": "이지스퍼블리싱",
        "pubdate": "20160303",
        "isbn": "8997390910 9788997390915",
        "description": "스스로 <b>파이썬</b> 프로그램을 만들 수 있는 실력을 키워보자!《DO IT! 점프 투 <b>파이썬</b>》은 지난 10년간 온라인 독자들의 질문 댓글에 답변하며 쌓아온... 책은 <b>파이썬</b>의 문법들을 실생활에서 쉽게 접할 수 있는 일들을 사례로 들어 설명하는 저자의 탁월함이 돋보인다. 더불어 최신 <b>파이썬</b> 3버전을 기준으로 내용을... "

        }
}
```

---

## 각 코드의 의미

### urllib 모듈 import

```python
 import urllib.request
```

- 웹 서버에 웹 페이지를 요청하고 응답받기 위해서 일반적으로 브라우저를 사용한다.
- python에서 브라우저 없이 http 프로토콜에 따라서 서버 요청/응답을 할 수 있도록 도와주는 것이 [urllib](https://docs.python.org/3/library/urllib.html) 모듈이다. (파이썬 표준 모듈)
  - request는 클라이언트의 요청을 처리한다.
  - response는 서버의 응답을 처리한다.
  - parse는 URL을 분석한다.

### request url 생성

```python
encText = urllib.parse.quote("파이썬") # 한글을 URL에 추가하기 위해서 UTF-8 형식으로 URL 인코딩
url = "https://openapi.naver.com/v1/search/book?query=" + encText +"&display=3&sort=count" # 요청 URL + 요청 변수
```

- [urllib.parse.quote](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.quote)를 통해서 비 ASCII 문자를 UTF-8 형식으로 URL 인코딩 해준다. (한글이 들어간 url은 UNICODE이고 url은 ASCII여야 하기 때문에 한글이 들어간 url은 UTF-8로 encoding 되어야 한다. [참고-강의노트 06. ASCII, UNICODE, utf8](https://wayhome25.github.io/cs/2017/04/05/cs-06/) )
- 요청 URL과 요청 변수는 [naver api 사이트](https://developers.naver.com/docs/search/book/)에서 확인할 수 있다.

### Request 객체 생성 및 header 추가

```python
search_request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
```
- [urllib.request.Request](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request) 클래스는 URL 요청과 관련된 정보를 담는 추상화된 클래스이다. http 통신 시 header 값을 설정하거나, HTTP request method 등을 설정 가능하다.
- Request 클래스의 [add_header](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.add_header)메소드를 활용하여 헤더 정보를 추가한다. 네이버 API를 사용하려면 클라이언트 정보를 헤더에 포함시켜야 한다.
> HTTP 헤더는 웹서버로 보내는 요청과 요청 데이터를 설명하는 메타 정보들이 들어있습니다. 즉 메서드가 무엇인지, 요청 URL이 무엇인지, http 프로토콜 버전 등이며, 여기에 추가적으로 지정된 이름과 값을 전송할 수 있습니다. 네이버 오픈 API는 기본적으로 클라이언트 아이디와 시크릿값을 헤더에 포함하여 전송해야 이용할 수 있도록 되어 있습니다. ([출처](https://developers.naver.com/docs/common/openapiguide/#/apiterms.md#42-http-헤더))

### urlopen 및 response 획득

```python
response = urllib.request.urlopen(request)
```

- [urllib.request.urlopen](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen) 메소드는 url string 혹은 request 객체를 전달 받는다. 여기서는 header 정보를 포함한 request 객체를 전달한다. urlopen 메소드는 http.client.HTTPResponse 객체를 리턴하며 해당 객체는 아래와 같은 메소드를 가진다.
  - geturl() : source 의 url을 반환한다. 일반적으로 redirect 여부를 확인하기 위해 사용한다.
  - getcode() : response의 HTTP status code 를 리턴한다.


### HTTP status code 확인 및 response 데이터 디코딩

```python
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
```

- getcode 메소드를 통해서 response의 HTTP status code를 확인한다.
- [네이버 오픈 API 에러 코드 목록](https://developers.naver.com/docs/common/openapiguide/#/errorcode.md)
- status code가 200인 경우 (정상 호출) read() 메소드를 통해서 http.client.HTTPResponse 객체로 부터 데이터를 읽어온다. (바이트형식)
- decode('utf-8')을 통해서 UTF-8 형식으로 디코딩하여 print 한다.

---

# 결론

- API에 대해서 막연한 두려움이 있었는데, 이번 기회를 통해서 그동안 가졌던 모호한 이미지를 구체화 시킬 수 있었다.
- 예전에 [처음 시작하는 파이썬](http://www.hanbit.co.kr/store/books/look.php?p_code=B2827459900)의 파이썬 라이브러리 모듈 부분은 재미가 없어서 대충 읽고 넘겼었다. api 샘플 코드를 공부하면서 urllib.request 모듈 부분을 다시 찾아서 읽으니 도움이 많이 되었다.
- 역시 필요성이 발생할 때 공부하는게 효율은 최고인 것 같다.
