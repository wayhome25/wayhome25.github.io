---
layout: post
title: jupyter notebook 배경화면 색 변경하기
tags: [단축키, zsh]
category: etc
comments: true
---

python수업을 듣거나 알고리즘 문제를 풀 때 [jupyter notebook](http://jupyter.org/)을 자주 사용하고 있다.
코드를 수정하기 편하고 결과를 바로 확인 할 수 있어서 좋은데, 배경화면이 흰색이라 눈이 아팠다.
레티나에서 볼 때는 봐줄만 하지만 외부모니터(DELL Ultrasharp)는 눈이 부셔서 흰 화면을 띄우기가 힘들다.

그래서 찾아보니 간단하게 iPython Jupyter Notebook 테마를 바꿀수 있었다!

# jupyter notebook 배경화면 색 변경하는 방법

## css 수정
- custom.css 파일을 만들고 원하는 테마의 CSS 코드를 입력한다.
- custom.css 파일의 경로는 아래와 같다. 나는 atom으로 파일을 편집했다.

```shell
# css 파일 편집하기
$ atom ~/.jupyter/custom/custom.css
```

## 테마 종류
- [jupyter GitHub repo](https://github.com/nsonnad/base16-ipython-notebook/tree/master/ipython-3/output)에서 다양한 테마의 css 파일을 확인 할 수 있다.
- 나는 **[base16-ocean-dark.css](https://github.com/nsonnad/base16-ipython-notebook/blob/master/ipython-3/output/base16-ocean-dark.css)** 테마를 적용했다.

<center>
 <figure>
 <img src="/assets/post-img/etc/before-jupyter.png" alt="views">
 <figcaption>변경 전</figcaption>
 </figure>
 </center>

<center>
 <figure>
 <img src="/assets/post-img/etc/after-jupyter.png" alt="views">
 <figcaption>변경 후</figcaption>
 </figure>
 </center>

## (참고) 사라진 toolbar 되돌리기
- 테마색을 바꾸고 만족스럽게 사용하고 있었는데, 상단의 toolbar가 사라져 있는걸 발견했다.
  가이드 문서를 보니 테마 개발자가 쓸모가 없다고 생각해서 숨김처리 (display: none) 했다고 한다.
- toolbar를 원래 상태로 되돌리려면 css 내용 중에서 아래 부분을 삭제하면 된다. 

```css
div#maintoolbar, div#header {display: none !important;}
```
