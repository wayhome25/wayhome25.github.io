---
layout: post
title: django 04. 장고 개인 프로젝트 3 - 자신의 글만 수정, 삭제 가능하도록 만들기
category: Django
tags: [python, 파이썬, Django, 인증]
comments: true
---
# django 04. 장고 개인 프로젝트 (메모 앱) - 자신의 글만 수정, 삭제 가능하도록 만들기
> 인증에 따른 기능 제한을 추가하는 과정에서 고민한 부분과 배운 것을 기록합니다.

## 결과물
- <http://siwabada.pythonanywhere.com/>

-------

# 삭제, 수정 제한 - 내가 쓴 글만 수정, 삭제하기
- 현재 상태 : 회원가입, 로그인, 로그아웃 기능을 추가했지만 누구나 글을 수정, 삭제할 수 있는 상태이다.
- 원하는 상태 : 로그인한 사용자가 자신이 쓴 글만 수정, 삭제할 수 있도록 하고싶다.

## 어떻게 할 수 있을까? 1 (아이디어)

- 삭제 버튼 숨김 / 표시   
  - 로그인 전 : 모든 글에 수정, 삭제 버튼이 보이지 않는다.
  - 로그인 후 : 자신이 쓴 글에만 수정, 삭제 버튼이 보인다.
-  수정, 삭제 시 사용자 확인
  - 수정, 삭제하려는 글의 글쓴이와, 로그인 되어있는 유저가 일치하는지 비교한다.

-------

## 어떻게 할 수 있을까? 2 (구현방법)

### 삭제 버튼 숨김 / 표시
- 로그인 전 : 모든 글에 수정, 삭제 버튼이 보이지 않는다.
    - .hidden 클래스의 추가/삭제 를 통해서 해당 태그 요소의 숨김/표시를 제어한다.
    - 수정, 삭제 버튼을 `<span class="control hidden">` 태그로 둘러싸고  `.hidden{display:none.}`을 통해서 해당 요소를 숨김처리한다.

    ```html
    {% raw %}
    <span class="control hidden">
      <a href="{% url 'modify_memo' memokey=memo.pk %}"><img src="{% static 'image/edit.png' %}" class= "edit" alt="수정"></a>
      <a href="{% url 'delete_memo' memokey=memo.pk %}" onclick="return confirm('정말 삭제하시겠습니까?')"><img src="{% static 'image/delete.png' %}" class="delete" alt="삭제"></a>
    </span>
    {% endraw %}
    ```
- 로그인 후 : 자신이 쓴 글에만 수정, 삭제 버튼이 보인다.
  - `로그인한 유저`와 `메모의 글쓴이`를 비교하여 일치하는 경우만 수정, 삭제 버튼을 표시한다.(.hidden 클래스 삭제)
  - 로그인한 유저는 탬플릿 내에서 {user.username} 으로 표시할 수 있다.
  - 하지만, 자바스크립트에서는 {} 을 사용할 수 없다. 어쩌지?
  - {user.username}을 `<span id="user_name"></span>` 으로 둘러싸고 제이쿼리를 이용하여 해당 태그 안의 텍스트 값을 가져오자.

  ```javascript
  {% raw %}
  // html
  <span id="user_name">{{ user.username }}</span>

  // javascript
  $("#user_name").text() // user_name id를 가진 태그 안의 텍스트 값 가져오기
  {% endraw %}

  ```
  - 각 메모의 글쓴이는 탬플릿 내에서 for 문을 돌면서 {memo.name_id} 로 표시한다.
  - {memo.name_id}는 값이 여러개라서 ID를 쓸 수가 없네 어쩌지?
  - {memo.name_id}을 `<span class="writer_name"></span>` 으로 둘러싸고 제이쿼리를 이용하여 해당 태그 안의 텍스트를 리스트로 가져온다.

  ```javascript
  {% raw %}
  // html
  <span class= "writer_name">{{memo.name_id}}</span>

  // javascript
  $(".writer_name") // .writer_name 클래스를 가진 태그 전체를 리스트로 출력
  $(".writer_name")[0].innerHTML  // .innerHTML로 태그 안의 텍스트 값 가져오기
  {% endraw %}

  ```

  - for 문으로 반복을 돌면서, 로그인한 유저명 - `user_name`과 메모의 글쓴이 - `writer_name`이 일치한다면, 반복 순서 i에 해당하는 메모의 `수정,삭제 버튼 블럭 태그`를 선택하여 클래스값 hidden을 지워준다.
    - `수정,삭제 버튼 블럭 태그`에 {forloop.counter} 를 통해서 특정 숫자를 포함한 아이디를 추가한다.
    - forloop.counter : 템플릿 내에서 for문으로 반복시 1씩 증가하는 숫자를 생성 [가이드문서](https://docs.djangoproject.com/en/1.10/ref/templates/builtins/#for) (forloop.counter0 : 0부터 숫자를 생성)

  ```html
  {% raw %}
  <!-- html -->
  <span class="control hidden" id = "control_id{{ forloop.counter0 }}">
    <a href="{% url 'modify_memo' memokey=memo.pk %}"><img src="{% static 'image/edit.png' %}" class= "edit" alt="수정"></a>
    <a href="{% url 'delete_memo' memokey=memo.pk %}" onclick="return confirm('정말 삭제하시겠습니까?')"><img src="{% static 'image/delete.png' %}" class="delete" alt="삭제"></a>
  </span>
  {% endraw %}
  ```

  ```javascript
  // javascript
  for(i = 0; i < $(".writer_name").length; i++){
    if($("#user_name").text() == $(".writer_name")[i].innerHTML){
      $("#control_id"+i).removeClass("hidden");
    }
  }
  ```

### 수정, 삭제 시 사용자 확인
- 문제가 생겼다. 개발자 도구로 hidden 클래스를 지워주면 남의 글도 삭제, 수정할 수 있다. 어떻게 하지?
- 수정, 삭제시 로그인 되어있는 유저와 해당 글의 글쓴이가 일치하는지 비교한다.
- 삭제 : views.py 의 delete 메소드 수정

```python
def delete(request, memokey):
    memo = Memos.objects.get(pk = memokey)
    if memo.name_id == User.objects.get(username = request.user.get_username()):
        memo.delete()
        return redirect('index')
    else:
        return render(request, 'memo_app/warning.html')
```

- 수정 : views.py 의 modify 메소드 수정

```python
def modify(request, memokey):
    if request.method == "POST":
        #수정 저장
        memo = Memos.objects.get(pk = memokey)
        form = PostForm(request.POST, instance=memo)
        if form.is_valid():
             form.save()
             return redirect('index')
    else:
        #수정 입력
        memo = Memos.objects.get(pk = memokey)
        if memo.name_id == User.objects.get(username = request.user.get_username()):
            memo = Memos.objects.get(pk = memokey)
            form = PostForm(instance = memo)
            return render(request, 'memo_app/modify.html', {'memo' : memo, 'form' : form})
        else:
            return render(request, 'memo_app/warning.html')
```
