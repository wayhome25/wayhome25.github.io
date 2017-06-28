---
layout: post
title: Django - Ajax / jQuery를 활용하여 새로고침 없이 좋아요 기능 구현하기   
category: Django
tags: [python, Django, ajax]
comments: true
---
> 개인적인 연습 내용을 정리한 글입니다.      
> 더 좋은 방법이 있거나, 잘못된 부분이 있으면 편하게 의견 주세요. :)

## 목차

<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->

* [들어가기](#들어가기)
* [Ajax](#ajax)
  * [Ajax의 장점](#ajax의-장점)
* [기존의 방식으로 좋아요 기능구현 (새로고침 O)](#기존의-방식으로-좋아요-기능구현-새로고침-o)
  * [좋아요 구현코드1 (새로고침 O)](#좋아요-구현코드1-새로고침-o)
    * [Model](#model)
    * [urls](#urls)
    * [view](#view)
    * [Template](#template)
* [Ajax/jQuery를 활용하여 인스타그램 좋아요 구현 (새로고침 X)](#ajaxjquery를-활용하여-인스타그램-좋아요-구현-새로고침-x)
  * [좋아요 구현코드2 (새로고침 X)](#좋아요-구현코드2-새로고침-x)
    * [Model](#model-1)
    * [urls](#urls-1)
    * [View](#view-1)
    * [Template](#template-1)
* [느낀점](#느낀점)
* [reference](#reference)

<!-- tocstop -->


## 들어가기
요즘 연습중인 [인스타그램st 프로젝트](https://github.com/wayhome25/Instagram) 를 진행하며 좋아요 버튼을 눌렀을 때 새로고침 없이 좋아요 숫자가 증감하도록 구현하고 싶었다.

![ezgif.com-video-to-gif](http://i.imgur.com/Njc8k8D.gif)
<center><figcaption>내가 원하는 것 (좋아요 숫자가 바로 변경된다)</figcaption></center>
<br>


찾아보니 jQuery와 ajax를 활용하면 페이지 새로고침 없이 서버와 데이터를 주고 받을 수 있다고 하여 적용해 보았다. ajax 통신은 페이스북, 인스타에서 사용하는 무제한 스크롤, 구글의 라이브 검색 등 널리 사용되고 있다. 이번 연습 과정을 기록하여, ajax 개념을 다시 정리하고 유사한 기능 구현시 활용하려고 한다.

좋아요를 구현한 2가지 방법의 **전체적인 처리 프로세스를 그려보면 아래와 같다.**      
각 구현방법에 대해서는 아래에서 하나씩 다루어 보려고 한다.
<br><br>
![New Mockup 1](http://i.imgur.com/0IABCSq.png)
<center><figcaption>새로고침이 필요한 방식 / Ajax를 활용한 방식 </figcaption></center>
<br>



## Ajax
[위키](https://namu.wiki/w/ajax)에 따르면 AJAX는 Asynchronous Javascript and XML의 약자로, 말그대로 Javascript와 XML을 이용한 **비동기적 정보 교환 기법이다.** 이름에 XML이라고 명시되어있긴 하지만, JSON이나 일반 텍스트 파일과 같은 다른 데이터 오브젝트들도 사용 가능하다.

간단하게, Ajax는 **전체 페이지를 새로 고치지 않고도 페이지의 일부만을 위한 데이터를 로드하는 기법** 이라고 할 수 있다
jQuery는 Ajax 요청을 생성하고 서버로부터 전달 받은 데이터 처리를 쉽게 만들어 준다.

**동기처리모델 (synchronouse processing model)** 의 경우,     
브라우저는 스크립트가 서버로부터 데이터를 수집하고 이를 처리한 후 페이지의 나머지 부분이 모두 로드될 때 까지 대기한다.   

반면에 **비동기 처리 모델 (asynchronouse processing model)** 의 경우,   
브라우저가 서버에 데이터를 요청하면, 작업이 완료되는 것을 기다리지 않고 나머지 페이지를 계속해서 로드하고 사용자와의 상호작용을 처리한다.

### Ajax의 장점
- 페이지 이동없이 고속으로 화면을 전환할 수 있다.
- 서버 처리를 기다리지 않고, 비동기 요청이 가능하다.
- 수신하는 데이터 양을 줄일 수 있고, 클라이언트에게 처리를 위임할 수도 있다.


---

# 기존의 방식으로 좋아요 기능구현 (새로고침 O)

기존 방식대로 구현하니 당연하게도 새로고침 후에 좋아요 처리정보가 반영되었다.   

- 좋아요 버튼에 url pattern을 연결
- view로 좋아요 작업 처리
- template에 context 데이터를 담아서 response
- 해당 template을 랜더링하여 좋아요 처리정보 반영 (새로고침 필요)

이와 같은 처리방식을 그림으로 표현하면 아래와 같다.


<center>
<figure>
<img src="/assets/post-img/django/non-ajax.png" alt="views">
<figcaption>페이지 새로고침이 필요한 좋아요 처리과정</figcaption>
</figure>
</center>

## 좋아요 구현코드1 (새로고침 O)
- 기존의 방식대로 구현한 전체 코드는 [github](https://github.com/wayhome25/Instagram/commit/356b2ac64acdcce530a68bfe6f0902e99d5fef81)에서 확인 가능하다.

### Model

```python
class Post(models.Model):
  # ...생략...
  like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        blank=True,
                                        related_name='like_user_set',
                                        through='Like')

  @property
  def like_count(self):
      return self.like_user_set.count()


class Like(models.Model):
  # ...생략...
  post = models.ForeignKey(Post)
```

### urls
```python
urlpatterns=[
  # ...생략...
  url(r'^(?P<pk>\d+)/like/$', views.post_like, name='post_like'),
]
```

### view
```python
@login_required
def post_like(request, pk):
  post = get_object_or_404(Post, pk=pk)
  # 중간자 모델 Like 를 사용하여, 현재 post와 request.user에 해당하는 Like 인스턴스를 가져온다.
  post_like, post_like_created = post.like_set.get_or_create(user=request.user)

  if not post_like_created:
    post_like.delete()

    return redirect('post:post_list')
```


### Template
```html
{% raw %}
<!-- 생략 -->
<li>
  <a href="{% url "post:post_like" post.pk %}">좋아요 {{ post.like_count }}개</a>
  {% for like_user in post.like_user_set.all %}
    {{ like_user.profile.nickname }}
  {% endfor %}
</li>
{% endraw %}
```
<br>

---

# Ajax/jQuery를 활용하여 인스타그램 좋아요 구현 (새로고침 X)

Ajax 를 통하여 전체 페이지를 새로 고치지 않고도 서버로 부터 좋아요 데이터만 로드하여 페이지에 적용할 수 있다. jQuery 는 Ajax 요청 생성 및 서버로부터의 데이터 처리를 쉽게 만들어 준다.

이와 같은 처리방식을 그림으로 표현하면 아래와 같다.
<br>
<center>
<figure>
<img src="/assets/post-img/django/ajax.png" alt="views">
<figcaption>Ajax/jQuery를 활용한 좋아요 처리과정</figcaption>
</figure>
</center>
<br>

## 좋아요 구현코드2 (새로고침 X)
- Ajax/jQuery를 할용하여 작성한 전체 코드는 [github](https://github.com/wayhome25/Instagram/commit/72b5649b8c4b38dda210d9a1bab00df55c1016a6)에서 확인 가능하다.

### Model
- 상기 코드와 동일

```python
class Post(models.Model):
  # ...생략...
  like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        blank=True,
                                        related_name='like_user_set',
                                        through='Like')

  @property
  def like_count(self):
      return self.like_user_set.count()


class Like(models.Model):
  # ...생략...
  post = models.ForeignKey(Post)
```

### urls
```python
urlpatterns=[
  # ...생략...
  url(r'^like/$', views.post_like, name='post_like'),
]
```

### View
```python
@login_required
@require_POST # 해당 뷰는 POST method 만 받는다.
def post_like(request):
    pk = request.POST.get('pk', None) # ajax 통신을 통해서 template에서 POST방식으로 전달
    post = get_object_or_404(Post, pk=pk)
    post_like, post_like_created = post.like_set.get_or_create(user=request.user)

    if not post_like_created:
        post_like.delete()
        message = "좋아요 취소"
    else:
        message = "좋아요"

    context = {'like_count': post.like_count,
               'message': message,
               'nickname': request.user.profile.nickname }

    return HttpResponse(json.dumps(context), content_type="application/json")
    # context를 json 타입으로
```


### Template
- jQuery 를 사용하여 Ajax 통신을 수행한다.

```html
{% raw %}
<!-- 생략 -->
<li>
  <input type="button" class="like" name="{{ post.id }}" value="Like">
  <p id="count-{{ post.id }}">{{ post.like_count }}개</p>
  <p id="like-user-{{post.id}}">
  {% for like_user in post.like_user_set.all %}
    {{ like_user.profile.nickname }}
  {% endfor %}
  </p>
</li>

<script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
<script type="text/javascript">
  $(".like").click(function(){
    var pk = $(this).attr('name')
    $.ajax({ // .like 버튼을 클릭하면 <새로고침> 없이 ajax로 서버와 통신하겠다.
      type: "POST", // 데이터를 전송하는 방법을 지정
      url: "{% url 'post:post_like' %}", // 통신할 url을 지정
      data: {'pk': pk, 'csrfmiddlewaretoken': '{{ csrf_token }}'}, // 서버로 데이터 전송시 옵션
      dataType: "json", // 서버측에서 전송한 데이터를 어떤 형식의 데이터로서 해석할 것인가를 지정, 없으면 알아서 판단
      // 서버측에서 전송한 Response 데이터 형식 (json)
      // {'likes_count': post.like_count, 'message': message }
      success: function(response){ // 통신 성공시 - 동적으로 좋아요 갯수 변경, 유저 목록 변경
        alert(response.message);
        $("#count-"+pk).html(response.like_count+"개");
        var users = $("#like-user-"+pk).text();
        if(users.indexOf(response.nickname) != -1){
          $("#like-user-"+pk).text(users.replace(response.nickname, ""));
        }else{
          $("#like-user-"+pk).text(response.nickname+users);
        }
      },
      error: function(request, status, error){ // 통신 실패시 - 로그인 페이지 리다이렉트
        alert("로그인이 필요합니다.")
        window.location.replace("/accounts/login/")
        //  alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
      },
    });
  })
</script>
{% endraw %}
```

## 느낀점
- 생각보다 많은 곳에서 Ajax가 활용되고 있다는 것을 알았다. (좋아요, 무한스크롤, 라이브검색, 계정 정보 표시 등)
- 이걸 간단하게 만들어주는 jQuery가 새삼 더 고맙게 느껴진다.
- 앞으로 Ajax를 잘 활용할 수 있도록 연습해야겠다.
- (추가) 이 글을 작성한 이후에 Ajax를 활용하여 무한스크롤 기능, 댓글 추가, 팔로우 기능을 구현해보았다. 알고나니 계속 쓰게 된다. (이왕이면 새로고침 없는게 좋으니..!)[코드상세](https://github.com/wayhome25/Instagram/commit/9731cdc0cc9148a6270f412c37e920ba5f02d137)

## reference
- [생활코딩 Ajax](https://opentutorials.org/course/1375/6843)
- [자바스크립트 Ajax 개념 및 활용방향](http://visualize.tistory.com/402)
