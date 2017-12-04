---
layout: post
title: (번역) RESTful API Designing guidelines — The best practices
category: etc
comments: true
---

> [RESTful API Designing guidelines — The best practices](https://hackernoon.com/restful-api-designing-guidelines-the-best-practices-60e1d954e7c9) 번역글 입니다.

<center>
<img src="https://i.imgur.com/mJeU8Gg.jpg" alt="views">
</center>
<br>

Facebook, Google, Github, Netflix와 같은 거대한 테크기업은 API를 통해서 개발자들과 프로덕트들이 자신들의 데이터를 사용할 수 있도록 하고, 그들을 위한 플랫폼이 되었다.
비록 당신이 다른 개발자들과 프로덕트를 위한 API를 개발하고 있지 않더라도, 잘 만들어진 API를 갖고 있는 것은 당신의 어플리케이션을 위해서도 좋다.

인터넷에서는 오랫동안 API 디자인을 위한 가장 좋은 방법에 대해서 논의가 이루어졌다. 하지만 통일된 공식적인 가이드라인은 없다.

API는 많은 개발자들이 데이터와 상호작용을 하기 위한 인터페이스이다. 잘 디자인된 API는 사용하기 쉽고, 개발자들의 삶을 편하게 만들어준다. API는 개발자를 위한 GUI이며, 만약 사용하기 혼란스럽거나 설명이 부족하다면 개발자들은 대체물을 찾아서 떠날 것이다. 개발자 경험은 API의 질을 측정함에 있어서 가장 중요한 기준이라고 할 수 있다.

<br>
<center>
<figure>
<img src="https://i.imgur.com/wr8xXR5.jpg" alt="views">
<figcaption>API는 무대에서 공연하는 아티스트이고, 사용자는 관객이다.</figcaption>
</figure>
</center>


### 1) 용어
다음은 REST API에 관련된 가장 중요한 용어들이다.
- **Resource** 는 어떤 것의 대표 혹은 객체이다. 이는 관련 데이터를 갖고 있고, 이를 운용하기 위한 메소드 집합을 가질 수 있다.  
예:  Animals, schools, employees는 resources이고 delete, add, update는 이 resources들에서 수행되는 operations이다.
- **Collections** 는 resources의 집합이다.   
예: Companies는 Company resource의 집합니다.
- **URL** (Uniform Resource Locator)은 어느 resource가 어디에 위치할 수 있고, 어떤 action들이 수행될 수 있는지를 나타내는 경로이다.

### 2) API endpoint
더 이해하기 위해서 Employees를 가진 Companies에 대한 API를 작성해보자.
`/getAllEmployees` 는 employees의 리스트를 response하는 API이다. Company에 관련된 API는 다음과 같은 것이 존재할 수 있다.

- /addNewEmployee
- /updateEmployee
- /deleteEmployee
- /deleteAllEmployees
- /promoteEmployee
- /promoteAllEmployees

그리고 다른 operations을 위해서 아주 많은 API endpoints가 존재할 수 있다. 이는 많은 중복을 포함하고 있고, 이러한 API endpoints는 수가 증가함에 따라서 유지보수가 힘들어진다.

#### 무엇이 문제일까?
URL은 오직 resources(명사)만 포함해야 하며 동사나 actions를 포함해서는 안된다. API path `/addNewEmployee` 는 action 인 `addNew` 를 resource 이름은 Employee와 함께 포함하고 있다.

#### 그럼 무엇이 올바른 방법일까?
`/companies` endpoint는 action을 포함하지 않는 좋은 예시이다. 그럼 이럴 땐 어떻게 서버에게 해당 `companies` resource에 대해서 add, delete, update와 같은 actions을 수행하도록 알려줄 수 있을까?

이는 동사인 HTTP 메소드 (GET, POST, DELETE, PUT)가 그 역할을 수행할 수 있다.

resource는 언제나 API endpoint에서 **복수형** 이어야 한다. 그리고 만약 resource의 특정 인스턴스에 접근하고 싶다면 URL에 id를 전달하여 접근할 수 있다.

- method `GET` path `/companies` 는 companies의 모든 목록을 가져온다.
- method `GET` path `/companies/34` 는 company 34의 상세 내용을 가져온다.
- method `DELETE` path `/companies/34` 는 company 34를 삭제한다.

몇 가지 다른 사용 사례에서 resource 아래에 여러 개의 resources가 있는 경우 (예 : 회사의 직원들), API endpoint는 아래와 같을 수 있다.

- `GET /companies/3/employees` 는 company 3에 속하는 employees 전체 목록을 가져온다.
- `GET /companies/3/employees/45` 는 company 3에 속하는 employee 45의 상세 내용을 가져온다.
- `DELETE /companies/3/employees/45` 는 company 3에 속하는 employee 45를 삭제한다.
- `POST /companies` 는 새로운 company를 생성하고, 생성된 company의 상세 내용을 리턴한다.

이와 같은 API가 더 일관성 있고 정확하지 않은가?

**결론**: path는 resources의 복수형을 포함해야 하고, HTTP 메소드는 해당 resource를 대상으로 수행되는 action의 종류를 정의해야 한다.

### 3) HTTP methods (동사)
HTTP는 resources를 대상으로 수행할 수 있는 몇 가지 타입의 methods를 정의해두고 있다.

` URL은 문장이고, resources는 명사이며 HTTP methods는 동사이다.`

주요 HTTP methods 는 아래와 같다.

1. `GET` method는 resource로 부터 데이터를 요청하며, 어떤 side effect도 발생시켜서는 안 된다.  
예: `/companies/3/employees` 는 company 3에 속하는 모든 employees를 리턴한다.

2. `POST` method는 database에 resource를 생성하도록 서버에 요청하며, 대부분 web form 형식으로 제출된다.  
예: `/companies/3/employees` 는 company 3에 새로운 employee를 생성한다.    
`POST`는 멱등성을 갖지 않으며 여러번의 request는 각각 다른 영향을 미친다.

3. `PUT` method는 resource를 업데이트 하거나, 만약 존재하지 않는 경우 생성하도록 서버에 요청한다.  
예: `/companies/3/employees/john` 는 company 3에 속하는 employees collection에 john이라는 resource를 업데이트하거나 생성하도록 서버에 요청한다.  
`PUT`은 멱등성을 가지며, 여러 번의 request는 같은 영향을 미친다.

4. `DELETE` method는 resources 혹은 그것의 인스턴스를 database에서 삭제하도록 요청한다.  
예: `/companies/3/employees/john/` 는 company 3에 속하는 employees collection에서 john이라는 resource를 삭제하도록 서버에 요청한다.

### 4) HTTP response status codes
API를 통해서 클라이언트가 서버에 request를 발생시키면 클라이언트는 해당 request가 성공, 실패 혹은 request 자체가 잘못되었는지 등의 결과를 얻을 수 있어야 한다. HTTP status code는 다양한 시나리오에서의 상황을 설명할 수 있는 표준화된 코드이다. 아래는 HTTP 코드의 주요 카테고리 분류이다.

#### 2xx (Success  Category)
해당 status code 들은 request가 정상 수신되고 서버를 통해서 성공적으로 수행되었음을 나타낸다.

- **200 Ok** GET, PUT, POST 성공을 대표하는 표준 HTTP response
- **201 Created** 해당 status code는 새로운 인스턴스 생성 시 리턴되어야 한다. 예를 들면 POST 메소드를 사용하여 새로운 인스턴스가 생성되면 항상 201 status code를 리턴한다.
- **204 No Content** 는 request가 성공적으로 수행되었으나 아무것도 리턴되지 않음을 의미한다. 대표적인 예로 DELETE가 있다. API `DELETE /companies/43/employees/2` 는 employee 2를 삭제하고 리턴되는 API response body에는 아무런 데이터도 필요하지 않다. 이는 시스템에 명시적으로 삭제하도록 요청했기 때문이다.
만약 `employee 2`가 데이터베이스에 존재하지 않는 것과 같은 에러가 발생한다면, `2xx Success Category` 가 아닌, `4xx Client Error category` response code를 리턴하게 된다.

#### 3xx (Redirection Category)
- **304 Not Modified** 는 client가 해당 response를 이미 캐시로 갖고 있음을 의미한다. 따라서 같은 데이터를 다시 전달할 필요가 없다.

#### 4xx (Client Error Category)
아래의 status code들은 client가 잘못된 request를 전달했음을 의미한다.
- **400 Bad Request** 는 client의 요청사항을 서버가 이해하지 못해서 request가 정상적으로 수행되지 않았음을 의미한다.
- **401 Unauthorized** 는 client가 resources에 대한 접근 권한이 없으며 필요한 자격을 갖추고 다시 request 해야 함을 의미한다.
- **403 Forbidden** 는 request가 유효하며, client의 권한에도 문제가 없지만 어떠한 이유로 인해서 client가 resource 페이지에 접근할 수 없음을 의미한다. 예를 들어 때때로 인증된 client가 서버의 디렉토리에 접근할 수 없는 경우가 있다.
- **404 Not Found** 는 요청된 resource가 현재 사용 불가능 함을 의미한다.
- **410 Gone** 는 요청된 resource가 의도적으로 이동되어 더 이상 사용 불가능 함을 의미한다.

#### 5xx (Server Error Category)
- **500 Internal Server Error** 는 request가 유효하지만, 서버에 문제가 발생하여 예상치 못한 조건을 제공하도록 요청받았음을 의미한다.
- **503 Service Unavailable** 는 서버가 다운되거나 request를 처리할 수 없음을 의미한다. 대부분 서버 점검시에 발생한다.

### 5) 필드 네이밍 컨벤션
원하는 네이밍 컨벤션을 사용할 수 있지만, 어플리케이션 전체에 걸쳐서 일관성을 갖는 것이 중요하다. 만약 request body 혹은 response type이 JSON이라면 일관성을 위해서 카멜케이스 규칙을 따르는 것이 좋다.

### 6) 검색, 정렬, 필터링, 페이지네이션
이러한 모든 작업은 하나의 데이터 집합에 대한 쿼리일 뿐이다. 이 같은 action을 처리하기 위한 별도의 API set은 존재하지 않는다. 다만 API의 GET 메소드에 쿼리 파라미터를 추가 할 필요가 있다. 몇가지 예시를 통해서 해당 action 들을 어떻게 구현할 수 있는지 살펴보자.

- **Sorting** 정렬된 companies 리스트를 원하는 경우, `GET /companies` endpoint는 여러개의 정렬 매개변수를 쿼리에서 받아야 한다. 예를 들어 `GET /companies?sort=rank_asc` 는 rank 오름차순으로 companies를 정렬해야 한다.
- **Filtering** 데이터셋 필터링을 위해서 쿼리 매개변수를 통해 다양한 조건을 전달할 수 있다. 예를 들어 `GET /companies?category=banking&location=india` 는 india에 위치하는 banking 카테고리의 companies를 필터링해야 한다.
- **Searching** companies list 중에서 이름을 검색하려면 API endpoint는 `GET /companies?search=Digital Mckinsey` 와 같아야 한다.
- **Pagination** 데이터셋이 너무 큰 경우, 데이터를 작은 덩어리로 나눔으로써 퍼포먼스를 향상시키고 response 핸들링을 좀 더 편하게 할 수 있다. 예를 들어 `GET /companies?page=23` 은 companies 리스트의 23번째 페이지를 의미한다.

만약 GET 메소드에 많은 쿼리 매개변수를 전달하여 URI가 너무 길어진다면 서버는 `414 URI Too long` HTTP status를 응답할 것이다. 이런 경우에는 POST 메소드의 request body를 통해서도 매개변수를 전달할 수 있다.

### 7) Versioning
당신의 API가 여러 곳에서 사용되고 있을 때 일부 변경 사항으로 API를 업그레이드하면, 기존의 API를 사용하는 제품이나 서비스에 문제가 발생할 수 있다.

`http://api.yourservice.com/v1/companies/34/employees` 처럼 경로에 API의 버전을 포함하는 것은 좋은 예시이다. 만약 주요 업데이트가 있는 경우에는 v2, v1.x.x 와 같은 새로운 API set을 위한 이름을 사용할 수 있다.
