---
layout: post
title: django 04. 장고 개인 프로젝트 4 - 좋아요 버튼, ajax 통신
category: Django
tags: [python, 파이썬, Django, 인증]
comments: true
---
# django 04. 장고 개인 프로젝트 (메모 앱) - 좋아요 버튼, ajax 통신
> 개인 프로젝트에 ajax 통신을 이용한 좋아요 기능을 추가하는 과정을 기록하였습니다.

- 원하는 상태 : 마음에 드는 글에 대해서 좋아요를 누르면 누적된 좋아요 수가 표시된다. 좋아요 버튼는 글 하나당 한번만 누를 수 있다.


## 결과물
- <http://siwabada.pythonanywhere.com/>

## Memos 모델에 likes 컬럼 추가
- 유저는 여러개의 메모에 좋아요를 할 수 있고, 메모는 여러 유저로부터 좋아요를 받을 수 있다.
- 참고로 `ForeignKey` 는 글쓴이 컬럼에 적용 (유저는 어려개의 메모를 작성할 수 있고, 메모는 1사람의 유저(글쓴이)를 갖는다.)
- 참고문서 : [Many-to-many relationships](https://docs.djangoproject.com/es/1.10/topics/db/examples/many_to_many/)
- 참고문서 : [property Decorator](https://www.programiz.com/python-programming/property)
- 참고 문서 : [related_name](http://stackoverflow.com/questions/2642613/what-is-related-name-used-for-in-django)
- models.py 수정

```python
from django.contrib.auth.models import User

class Memos(models.Model):
  name_id = models.ForeignKey(User, on_delete = models.CASCADE)
  likes = models.ManyToManyField(User, related_name='likes')
  # User에서 접근할 때 related_name이 설정되지 않으면 User.memos_set.all()과 같은 방식으로 연관 모델에 접근한다.

  @property
  def total_likes(self):
    return self.likes.count() #likes 컬럼의 값의 갯수를 센다
```

## View에 like 메소드 추가
- 참고문서 : [view decorators](https://docs.djangoproject.com/en/1.10/topics/http/decorators/)
- views.py

```python
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


@login_required
@require_POST
def like(request):
    if request.method == 'POST':
        user = request.user # 로그인한 유저를 가져온다.
        memo_id = request.POST.get('pk', None)
        memo = Memos.objects.get(pk = memo_id) #해당 메모 오브젝트를 가져온다.

        if memo.likes.filter(id = user.id).exists(): #이미 해당 유저가 likes컬럼에 존재하면
            memo.likes.remove(user) #likes 컬럼에서 해당 유저를 지운다.
            message = 'You disliked this'
        else:
            memo.likes.add(user)
            message = 'You liked this'

    context = {'likes_count' : memo.total_likes, 'message' : message}
    return HttpResponse(json.dumps(context), content_type='application/json')
    # dic 형식을 json 형식으로 바꾸어 전달한다.
```

## url 패턴 추가
- urls.py

```python
urlpatterns = [
  url(r'^like/$', views.like, name='like'),
]
```

## 템플릿에 좋아요 버튼 및 ajax 코드 추가
- default.html

```html
{% raw %}
<div class="thumbnail priority">
  <div class="caption">
    <h2>{{memo.title}}
      <span>&nbsp;&nbsp;by <span class= "writer_name">{{memo.name_id}}</span></span><br><span class="date">{{memo.update_date}}</span>
      <span class="control hidden" id = "control_id{{ forloop.counter0 }}">
        <a href="{% url 'modify_memo' memokey=memo.pk %}"><img src="{% static 'image/edit.png' %}" class= "edit" alt="수정"></a>
        <a href="{% url 'delete_memo' memokey=memo.pk %}" onclick="return confirm('정말 삭제하시겠습니까?')"><img src="{% static 'image/delete.png' %}" class="delete" alt="삭제"></a>
      </span>
      <input type="button" class="like" name="{{ memo.id }}" value="Like">
      <p id="count{{ memo.id }}">count : {{ memo.total_likes }}</p>
    </h2>
    <p>{{memo.text}}</p>
  </div>
</div>
{% endraw %}
```

- ajax 통신 error 발생시 아래와 같은 코드를 통해서 문제 내용을 파악하기 쉬워진다.

```html
{% raw %}
<script type="text/javascript">
// 인증에 따른 수정, 삭제 버튼 숨김처리
  for(i = 0; i < $(".writer_name").length; i++){
    if($("#user_name").text() == $(".writer_name")[i].innerHTML){
      $("#control_id"+i).removeClass("hidden");
    }
  }

// 좋아요 버튼 처리
// 버튼 클릭 > ajax통신 (like url로 전달) > views의 like 메소드에서 리턴하는 값 전달받기 > 성공시 콜백 호출
$('.like').click(function(){
  var pk = $(this).attr('name') // 클릭한 요소의 attribute 중 name의 값을 가져온다.
  $.ajax({
      type: "POST", // 데이터를 전송하는 방법을 지정한다.
      url: "{% url 'like' %}", // 통신할 url을 지정한다.
      data: {'pk': pk, 'csrfmiddlewaretoken': '{{ csrf_token }}'}, // 서버로 데이터를 전송할 때 이 옵션을 사용한다.
      dataType: "json", // 서버측에서 전송한 데이터를 어떤 형식의 데이터로서 해석할 것인가를 지정한다. 없으면 알아서 판단한다.
      // 서버측에서 전송한 데이터 views.py like 메소드
      // context = {'likes_count' : memo.total_likes, 'message' : message}
      // json.dump(context)를 통해서 json 형식으로 전달된다.

      success: function(response){ // 성공했을 때 호출할 콜백을 지정한다.
        id = $(this).attr('name')
        $('#count'+ pk).html("count : "+ response.likes_count);
        alert(response.message);
        alert("좋아요수 :" + response.likes_count);
      },
      error:function(request,status,error){
        alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
      }
  });
})
</script>
{% endraw %}
```
