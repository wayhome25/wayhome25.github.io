---
layout: post
title: git 초보를 위한 풀리퀘스트(pull request) 방법
category: git
tags: [git, PR, pull request]
comments: true
---

> 처음으로 github pull request (PR)를 하면서 겪었던 시행착오를 기록합니다.     
> 더 좋은 방법이나, 잘못된 내용이 있으면 편하게 의견 주세요 :)

<br>
# 들어가기

- [8퍼센트 스터디](https://8percent.github.io/2017-06-30/%EC%8A%A4%ED%84%B0%EB%94%94%EC%8B%9C%EC%9E%91/)에 외부인으로 참여하게 되었다!
- 참여 첫날 기술 블로그에 [스터디 후기](https://8percent.github.io/2017-07-07/tsd2/)를 작성해달라는 요청을 받았다.

#### "회사 기술블로그 repository를 포크떠서 후기 작성하시고 저한테 PR 보내주세요"

<center>
<figure>
<img src="/assets/post-img/surprise.png" alt="views">
<figcaption>(포크..PR.. 말로만 들어봤는데 먹는 걸까?)</figcaption>
</figure>
</center>
<br>

- 개인 github repository 관리 경험은 있지만 pull request 는 처음이라 어떻게 해야하나 걱정이 앞섰다.
- 뭐 찾아보면 되겠지..! 하는 마음으로 집에 왔는데, 생각보다 쉽게 설명된 자료를 찾지 못해서 시행착오를 겪었다.
- 앞으로 협업을 하다보면 pull request 할 일이 많을 거라고 생각해서 이번 기회에 정리해두려고 한다.

---

## 개요
- pull request를 위해서 아래와 같은 절차를 거쳤다. 각 절차에서 작업한 내용은 다음 절에 하나씩 정리하려고 한다. 분명 비효율적인 부분이 있을 수 있는데, 댓글로 알려주시면 **정말 정말 도움이 될 것 같다.**

1. Fork
2. clone, remote설정
3. branch 생성
4. 수정 작업 후 add, commit, push
4. Pull Request 생성
5. 코드리뷰, Merge Pull Reqest
6. Merge 이후 branch 삭제 및 동기화

---

## 1. Fork
- 타겟 프로젝트의 저장소를 자신의 저장소로 Fork 한다.

![pr1](http://i.imgur.com/ufBroYo.png)

![p2](http://i.imgur.com/K8J7cmB.png)

---

## 2. clone, remote 설정
- fork로 생성한 본인 계정의 저장소에서 **clone or download** 버튼을 누르고 표시되는 url을 복사한다. (중요 - 브라우저 url을 그냥 복사하면 안 된다)

![p3](http://i.imgur.com/bi6V5Lq.png)

<br>
- 터미널을 켠다. (mac 기준)
- 자신의 컴퓨터에서 작업을 하기 위해서 Fork한 저장소를 로컬에 clone 한다.

```shell
$ git clone https://github.com/wayhome25/blog.github.io.git
```

- 로컬 저장소에 원격 저장소를 추가한다. 위 작업과 동일하게 github 저장소에서 **clone or download** 메뉴를 통해서 확인한 url을 사용한다.
  - 원본 프로젝트 저장소 (직접 추가 필요)
  - fork한 로컬 프로젝트 (origin이라는 별명으로 기본으로 추가되어 있다. 따로 추가할 필요 없음)


```python
# 원본 프로젝트 저장소를 원격 저장소로 추가
$ git remote add real-blog(별명) https://github.com/원본계정/blog.github.io.git

# 원격 저장소 설정 현황 확인방법
$ git remote -v
 ```
---

## 3. branch 생성
- 자신의 로컬 컴퓨터에서 코드를 추가하는 작업은 branch를 만들어서 진행한다.

> 개발을 하다 보면 코드를 여러 개로 복사해야 하는 일이 자주 생긴다. 코드를 통째로 복사하고 나서 원래 코드와는 상관없이 독립적으로 개발을 진행할 수 있는데, 이렇게 독립적으로 개발하는 것이 브랜치다. - pro git book

```shell
# develop 이라는 이름의 branch를 생성한다.
$ git checkout -b develop
Switched to a new branch 'develop'

# 이제 2개의 브랜치가 존재한다.
$ git branch
* develop
  master
```
---

## 4. 수정 작업 후 add, commit, push
- 자신이 사용하는 코드 편집 툴을 활용하여 수정 작업을 진행한다.
- 작업이 완료되면, add, commit, push를 통해서 자신의 github repository (origin)에 수정사항을 반영한다.
- `주의사항` push 진행시에 branch 이름을 명시해주어야 한다.

```python
# develop 브랜치의 수정 내역을 origin 으로 푸시한다.
$ git push origin develop
```
---

## 5. Pull Request 생성
- push 완료 후 본인 계정의 github 저장소에 들어오면 **Compare & pull reqeust** 버튼이 활성화 되어 있다.
- 해당 버튼을 선택하여 메시지를 작성하고 PR을 생성한다.

![p4](http://i.imgur.com/F2d5N13.png)
<br>
![p5](http://i.imgur.com/G08Blvn.png)

---

## 6. 코드리뷰, Merge Pull Reqest  
- PR을 받은 원본 저장소 관리자는 코드 변경내역을 확인하고 Merge 여부를 결정한다.

---

## 7. Merge 이후 동기화 및 branch 삭제
- 원본 저장소에 Merge가 완료되면 로컬 코드와 원본 저장소의 코드를 동기화 한다.
- 작업하던 로컬의 branch를 삭제한다.

```python
# 코드 동기화
$ git pull real-blog(remote 별명)
# 브랜치 삭제
$ git branch -d develop(브랜치 별명)
```

- 나중에 추가로 작업할 일이 있으면 `git pull real-blog(remote 별명)` 명령을 통해 원본 저장소와 동기화를 진행하고 3~7을 반복한다.

---

# 결론
- 시행착오는 있었지만 위와 같은 방법으로 첫 PR을 생성하고 무사히 Merge 까지 되었다! (감격)
- 당장 내가 PR을 해야하는 상황에서 했던 작업들을 정리한 것이라,    
  각 절차의 심오한 의미에 대해서는 다루지 못했다.
- 더 자세한 내용은 [pro git book](https://git-scm.com/book/ko/v1/%EB%B6%84%EC%82%B0-%ED%99%98%EA%B2%BD%EC%97%90%EC%84%9C%EC%9D%98-Git-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%EC%97%90-%EA%B8%B0%EC%97%AC%ED%95%98%EA%B8%B0) 에서 확인할 수 있다.
- 나처럼 급하게 Pull Request 해야하는 분들에게 도움이 되었으면 좋겠다.
