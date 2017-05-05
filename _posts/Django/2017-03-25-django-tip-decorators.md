---
layout: post
title: 로그인 사용자에게만 특정 view 표시하기 (보안)
category: Django
tags: [python, Django]
comments: true
---

게시판 사이트 등을 만들다 보면 로그인한 사용자만 특정 view(삭제, 수정 등)에 접근할 수 있도록 해야하는 상황이 자주 발생한다.
django는 decorators를 통해서 이를 쉽게 구현할 수 있도록 한다.


```python
# myapp/views.ppy

from django.contrib.auth.decorators import login_required

@login_required
def post_new(request):
    [...
```

만약 로그인 하지 않은 사용자가 해당 view에 접근하는 경우, django는 자동으로 로그인 화면으로 연결한다.
