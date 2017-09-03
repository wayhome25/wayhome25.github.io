---
layout: post
title: Django - Slacker를 활용하여 간단하게 슬랙 봇 메시지 보내기
category: Django
tags: [django, slack, bot, 슬랙]
comments: true
---
<br>

# 하고 싶었던 것
도서관리 사이트에서 신규도서가 등록되거나, 연체도서가 발생하는 등의 이벤트가 있었을때 슬랙으로 알람을 보내는 기능을 추가하고 싶었다.

<center>
<figure>
<img src="/assets/post-img/django/slack-bot.png" alt="views" style="width:824px; height:108px;">
<figcaption>새책을 등록하면 슬랙으로 이런 메시지를 보내고 싶었다.</figcaption>
</figure>
</center>
<br>

찾아보니 [slack api 공식 사이트](https://api.slack.com/community)에서 추천하는 [slacker](https://github.com/os/slacker/) 라는 오픈소스 라이브러리를 사용해서 간단하게 bot으로 원하는 채널에 메시지를 보낼 수 있었다.

---

# 준비과정

- [slack api 사이트](https://api.slack.com/)에서 build 선택
![slack1](https://i.imgur.com/4szsds3.png)
- create app 선택
![slack2](https://i.imgur.com/vuY6KbS.png)
- Bot Users 메뉴에서 Add Bot User 선택
![slack3](https://i.imgur.com/3Dy2jsn.png)
- OAuth & Permissions 에서 Install App to Team 선택
![slack4](https://i.imgur.com/LMyAXK3.png)
- 생성된 Token(Bot User OAuth Access Token)을 확인하고 복사해두기
![slack5](https://i.imgur.com/aTW7sQm.png)

---

# 코드
- 여러 앱에서 범용적으로 사용할 수 있도록, utils 폴더의 slack.py 파일에 아래와 같은 코드를 작성했다.
- token 값은 공개저장소에 노출되지 않도록 주의해야한다.
- 비밀 값을 설정 파일에서 분리하는 방법은 다른 포스팅 ([Django - settings.py 의 SECRET_KEY 변경 및 분리하기](https://wayhome25.github.io/django/2017/07/11/django-settings-secret-key/))에 정리해보았다.



```python
# utils/slack.py
from slacker import Slacker

def slack_notify(text=None, channel='#test', username='알림봇', attachments=None):
    token = 'xoxb-235어쩌구-저쩌구-발급받은토큰을여기에' #토근값은 공개저장소에 공개되지 않도록 주의
    slack = Slacker(token)
    slack.chat.post_message(text=text, channel=channel, username=username, attachments=attachments)
```

- 위의 slack_notify 함수를 views 에서 활용하는 예시는 아래와 같다.
- 신규 도서가 저장되면 슬랙메시지를 발송한다.

```python
# views.py
from utils.slack import slack_notify

@require_POST
def register_save(request):
    isbn = request.POST['isbn']
    message, book = register_book(isbn)
    messages.info(request, message)
    if book:
        slack_message = "*[신규도서]* {}".format(book.title)
        slack_notify(slack_message, '#new_book', username='새책 알림봇')
    return redirect('books:register')
```

- 위 코드에서는 [Slacker 활용 예시](https://github.com/os/slacker/)를 참고해서 단순 메시지만 보내도록 했지만, [attachments](https://api.slack.com/docs/message-attachments)등을 활용하면 더 화려하게 메시지를 보낼 수 있다.

![screen 6](https://i.imgur.com/Jqx28Ug.png)

```python
# attachments 활용예시
attachments = [{
    "color": "#36a64f",
    "title": "신규도서",
    "title_link": "http://127.0.0.1:7000/books/list/",
    "fallback": "신규도서 알림",
    "text": "{}".format(book.title)
}]
slack_notify(channel='#new_book', username='새책 알림봇', attachments=attachments)
```
