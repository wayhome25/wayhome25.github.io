---
layout: post
title: django 04. 장고 개인 프로젝트 5 - 정렬방식 변경하기 (좋아요, 최신, 내가쓴글)
category: Django
tags: [python, 파이썬, Django, 인증]
comments: true
---
> 개인 프로젝트에 여러가지 정렬 기준에 따라서 정렬방식을 변경하는 과정을 기록하였습니다.

- 원하는 상태 : 최신순/좋아요/내가쓴글 순으로 정렬방식을 변경한다.


## 결과물
- <http://siwabada.pythonanywhere.com/>

## template 수정
- 화면에 정렬 기준을 변경하기 위한 요소(셀렉트박스)를 추가한다.

```html
{% raw %}
<select id="sort-select" onchange="location = this.value;">
  <option class="sort-date" value="/">최신순</option>
  <option class="sort-likes" value="?sort=likes">좋아요순</option>
  {% if user.is_authenticated %}
  <option class="sort-mypost" value="?sort=mypost">내가쓴글</option>
  {% endif %}
</select>
{% endraw %}
```

## views.py 수정
- views.py 내용중 정렬이 필요한 index 화면 부분을 수정한다.
- `request.GET.get('sort','')` 을 통해서 url 쿼리스트링 ?sort=like 의 값을 가져온다.
- `request.GET['sort']`와 같은 방법을 통해서도 쿼리스트링 값을 가져올 수 있지만, 없는 경우 오류가 발생한다.
- `ManyToManyField`인 likes 컬럼을 기준으로 하려면 `annotate` 메소드 사용이 필요하다.
- 1번째 기준인 '좋아요 수'가 같은 경우는 2번째 기준으로 '작성일'을 기준으로 정렬한다.
- 참고글 : [(엑셀만큼 쉬운) Django Annotation/Aggregation](http://raccoonyy.github.io/django-annotate-and-aggregate-like-as-excel/)
- `.objects.filter()` 을 통해서 조건에 맞는 복수의 오브젝트를 가져올 수 있다. (`.objects.get()` 에서는 오류 발생)

```python
def index(request):
    sort = request.GET.get('sort','') #url의 쿼리스트링을 가져온다. 없는 경우 공백을 리턴한다

    if sort == 'likes':
        memos = Memos.objects.annotate(like_count=Count('likes')).order_by('-like_count', '-update_date')
        return render(request, 'memo_app/index.html', {'memos' : memos})
    elif sort == 'mypost':
        user = request.user
        memos = Memos.objects.filter(name_id = user).order_by('-update_date') #복수를 가져올수 있음
        return render(request, 'memo_app/index.html', {'memos' : memos})
    else:
        memos = Memos.objects.order_by('-update_date')
        return render(request, 'memo_app/index.html', {'memos' : memos})
```

## 참고 - 셀렉트박스 유지를 위한 스크립트
```javascript
// get url query string
var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = decodeURIComponent(window.location.search.substring(1)),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : sParameterName[1];
        }
    }
};
// 정렬방식 셀렉트 박스 유지
$(document).ready(function(){
  var sort = getUrlParameter('sort');
  if(sort == 'likes'){
    $('.sort-likes').prop('selected', 'selected')
  }else if(sort == 'mypost'){
    $('.sort-mypost').prop('selected', 'selected')
  }else{
    $('.sort-date').prop('selected', 'selected')
  }
});
```
