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
비록 당신이 다른 개발자들과 프로덕트를 위한 API를 개발하고 있지 않더라도, 잘 만들어진 API를 갖고 있는것은 당신의 어플리케이션을 위해서도 좋다.

인터넷에서는 오랜동안 API 디자인을 위한 가장 좋은 방법에 대해서 논의가 이루어졌다. 하지만 통일된 공식적인 가이드라인은 없다.

API는 많은 개발자들이 데이터와 상호작용을 하기 위한 인터페이스이다. 잘 디자인된 API는 사용하기 쉽고, 개발자들의 삶을 편하게 만들어준다. API는 개발자를 위한 GUI이며, 만약 사용하기 혼란스럽거나 설명이 부족하다면 개발자들은 대체물을 찾아서 떠날 것이다. 개발자 경험은 API의 질을 측정하는데 있어서 가장 중요한 기준이라고 할 수 있다.

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
`/getAllEmployees` 는 employees의 리스트를 response하는 API이다. Company에 관련된 API는 다음와 같은 것이 존재할 수 있다.

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
`/companies` endpoint는 action을 포함하지 않는 좋은 예시이다. 그럼 이럴땐 어떻게 서버에게 해당 `companies` resource에 대해서 add, delete, update와 같은 actions을 수행하도록 알려줄 수 있을까?

이는 동사인 HTTP 메소드 (GET, POST, DELETE, PUT)가 그 역할을 수행할 수 있다.

resource는 언제나 API endpoint에서 **복수형** 이어야 한다. 그리고 만약 resource의 특정 인스턴스에 접근하고 싶다면 URL에 id를 전달하여 접근할 수 있다.

- method `GET` path `/companies` 는 companies의 모든 목록을 가져온다.
- method `GET` path `/companies/34` 는 company 34의 상세 내용을 가져온다.
- method `DELETE` path `/companies/34` 는 company 34를 삭제한다.

몇 가지 다른 사용 사례에서 resource 아래에 여러개의 resources가 있는 경우 (예 : 회사의 직원들), API endpoint는 아래와 같을 수 있다.

- `GET /companies/3/employees` 는 company 3에 속하는 employees 전체 목록을 가져온다.
- `GET /companies/3/employees/45` 는 company 3에 속하는 employee 45의 상세 내용을 가져온다.
- `DELETE /companies/3/employees/45` 는 company 3에 속하는 employee 45를 삭제한다.
- `POST /companies` 는 새로운 company를 생성하고, 생성된 company의 상세 내용을 리턴한다.

이런 API가 더 일관성있고 정확하지 않나요?

**결론**: path는 resources의 복수형을 포함해야하고, HTTP 메소드는 해당 resource를 대상으로 수행되는 action의 종류를 정의해야 한다.

### 3) HTTP methods (동사)
HTTP는 resources를 대상으로 수행할 수 있는 몇가지 타입의 methods를 정의해두고 있다.

` URL은 문장이고, resources는 명사이며 HTTP methods는 동사이다.`

주요 HTTP methods 는 아래와 같다.

1. `GET` method는 resource로 부터 데이터를 요청하며, 어떤 side effect도 발생시켜서는 안된다.  
예: `/companies/3/employees` 는 company 3에 속하는 모든 employees를 리턴한다.

2. `POST` method는 database에 resource를 생성하도록 서버에 요청하며, 대부분 web form 형식으로 제출된다.  
예: `/companies/3/employees` 는 company 3에 새로운 employee를 생성한다.    
`POST`는 멱등성을 갖지 않으며 여러번의 request는 각각 다른 영향을 미친다.

3. `PUT` method는 resource를 업데이트 하거나, 만약 존재하지 않는 경우 생성하도록 서버에 요청한다.  
예: `/companies/3/employees/john` 는 company 3에 속하는 employees collection에 john이라는 resource를 업데이트하거나 생성하도록 서버에 요청한다.  
`PUT`은 멱등성을 가지며, 여러번의 request는 같은 영향을 미친다.

4. `DELETE` method는 resources 혹은 그것의 인스턴스를 database에서 삭제하도록 요청한다.  
예: `/companies/3/employees/john/` 는 company 3에 속하는 employees collection에서 john이라는 resource를 삭제하도록 서버에 요청한다.

### 4) HTTP response status codes
