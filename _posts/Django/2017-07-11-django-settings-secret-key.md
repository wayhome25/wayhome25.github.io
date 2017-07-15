---
layout: post
title: Django - settings.py 의 SECRET_KEY 변경 및 분리하기
category: Django
tags: [python, Django, settings, secret key]
comments: true
---
> [Two Scoops of Django](https://www.twoscoopspress.com/products/two-scoops-of-django-1-11) 5장을 읽고 연습한 내용을 정리한 글입니다.  
> 더 좋은 방법이 있거나, 잘못된 부분이 있으면 편하게 의견 주세요. :)

<br>
# 들어가기
django-admin startproject 명령을 통해서 장고 프로젝트를 생성하면, 기본으로 settings.py 파일이 함께 포함된다. settings.py 안에는 다양한 설정 항목이 있는데, 그 중에서 SECRET_KEY 라는 것이 있다. 이는 장고 보안 기능에 활용되는 값으로, 그동안 github의 공개 저장소에 SECRET_KEY를 그대로 노출한 상태로 settings.py 파일을 함께 push 했었다.    

최근 [Two Scoops of Django](https://www.twoscoopspress.com/products/two-scoops-of-django-1-11)의 **5.3 코드에서 설정 분리하기** 를 읽어보니 비밀 값들은 외부에 공개되면 안된다는 내용이 있었다. 누구나 한번 쯤은 SECRET_KEY를 외부에 노출한 경험은 있을 것 같은데, 이번 기회에 settings.py의 비밀 값을 코드에서 분리해야겠다고 생각했다.
> 비밀 값들은 반드시 남이 알 수 없어야 한다. 이를 버전 컨트롤 시스템에 추가하면 코드 저장소에 접근할 수 있는 누구에게나 공개된다

---

## SECRET_KEY
SECRET_KEY는 어디에 사용될까? [Django 공식문서](https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-SECRET_KEY) 를 보면 다음과 같이 안내되어 있다.       

- django.contrib.sessions.backends.cache 이외의 session backend를 사용하고 있거나,   
  기본 get_session_auth_hash()를 사용하는 모든 sessions
- CookieStorage 혹은 FallbackStorage 를 사용하는 모든 messages
- 모든 PasswordResetView
- 다른 키가 제공되지 않는 암호화 서명 사용 시 사용된다.

<center>
<figure>
<img src="/assets/post-img/django/secret_key.png" alt="views">
<figcaption>그리고 SECRET_KEY는 공개하면 안된다</figcaption>
</figure>
</center>
<br>
위 문서와 같이 비밀 키가 노출되면 Django의 보안 기능이 상실될 위험성이 있다.

#### 나는 이미 공개 저장소에 올려버렸는데 어쩌지?!

<center>
<figure>
<img src="/assets/post-img/surprise.png" alt="views">
<figcaption>어쩌면 좋지..!</figcaption>
</figure>
</center>
<br>

나를 포함해서 이렇게 생각할 분들이 많을 것 같아서 찾아보니 배포 후에도 SECRET_KEY 변경이 가능하다는 글이 있었다.
([Is it possible to change the secret key of a Django application after it deployment in production, If so, what would be the impacts?](https://www.quora.com/Is-it-possible-to-change-the-secret-key-of-a-Django-application-after-it-deployment-in-production-If-so-what-would-be-the-impacts)) SECRET_KEY는 주로 쿠키데이터 해시, 암호화 등 임시적인 일에 사용되고, 변경 시 로그인 세션 등의 데이터가 사라질 수 있다. 확인 차 개인 프로젝트의 SECRET_KEY를 변경하여 로컬 서버에서 다시 테스트를 해보니 큰 문제는 발생하지 않았다. 프로젝트 초반이거나, 복잡한 기능이 없는 프로젝트에서는 변경해도 괜찮다고 생각한다. (혹시 아니라면 댓글로 알려주시면 감사합니다!)

SECRET_KEY는 50자의 랜덤 문자로 구성되어 있는데, [Django Secret Key Generator](http://www.miniwebtool.com/django-secret-key-generator/) 라는 것도 존재한다. 혹은 아래의 코드를 실행해서 임의 50글자를 직접 생성하는 것도 가능하다. ([코드 출처](https://github.com/honux77/inflearn-django/blob/master/script/genkey.py))

```python
import string, random


# Get ascii Characters numbers and punctuation (minus quote characters as they could terminate string).
chars = ''.join([string.ascii_letters, string.digits, string.punctuation]).replace('\'', '').replace('"', '').replace('\\', '')

SECRET_KEY = ''.join([random.SystemRandom().choice(chars) for i in range(50)])

print(SECRET_KEY)
```

---

## SECRET_KEY 분리하기  
settings.py 파일에서 비밀 값을 분리하는 방법은 여러가지가 있는데 책에서 소개하는 방법은 2가지이다.
- 환경변수패턴 : SECRET_KEY의 값을 환경변수에 저장하여 참고한다.
- 비밀파일패턴 : SECRET_KEY의 값을 별도 파일에 저장하여 참고한다.

## 1. 환경변수패턴
환경변수란 프로세스가 컴퓨터에서 동작하는 방식에 영향을 미치는, 동적인 값들의 모임이다.([위키](https://ko.wikipedia.org/wiki/%ED%99%98%EA%B2%BD_%EB%B3%80%EC%88%98))
시스템의 실행파일이 놓여 있는 디렉토리의 지정 등 OS 상에서 동작하는 응용소프트웨어가 참조하기 위한 설정이 기록된다. 환경변수를 사용하여 비밀 키를 보관함으로써 걱정 없이 세팅파일을 github 공개 저장소에 추가할 수 있다.

로컬 개발 환경에서 환경 변수를 세팅하려면 다음 코드를 .bashrc 혹은 .bash_profile, .profile, .zshrc 파일에 추가하면 된다. 어느 종류의 shell을 사용하는지에 따라서 편집하는 파일이 달라진다.(mac 사용자 기준)
나의 경우 [zsh](http://ohmyz.sh/)을 사용하고 있어서 .zshrc에 아래와 같이 환경변수 추가 작업을 진행했다.

```shell
$ vim ~/.zshrc # vim을 사용하여 .zshrc 파일을 편집하겠다.

# .zshrc 파일에 아래 코드를 추가해준다.
export INSTA_SECRET_KEY='b_4(!id8ro!1645n@ub55555hbu93gaia0 본인의 고유 비밀 키 추가'

# 환경변수 확인 명령
$ echo $INSTA_SECRET_KEY
```

추가 완료 후, settings.py 파일을 열어서 SECRET_KEY 의 값을 삭제하고 환경변수로 대체한다.

```python
# settings.py
import os


# 환경변수 INSTA_SECRET_KEY 의 값을 참조한다.
SECRET_KEY = os.environ["INSTA_SECRET_KEY"]
```

혹은 아래와 같은 예외 처리를 통해서 환경변수가 존재하지 않을 때 원인을 파악하기 쉽도록 할 수 있다.

```python
# settings.py
import os
from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name):
  """환경 변수를 가져오거나 예외를 반환한다."""
  try:
    return os.environ[var_name]
  except KeyError:
    error_msg = "Set the {} environment variable".format(var_name)
    raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_env_variable("INSTA_SECRET_KEY")
```

쉘에서 python3 manage.py runserver 명령을 입력하니 정상적으로 개발 서버가 구동되는 것을 확인 할 수 있었다. 참고로 실제 운영환경에서 환경변수를 세팅하려면, 각자 사용하는 배포도구에 따라서 변수 지정방법이 달라진다.

---

## 2. 비밀파일패턴

환경변수는 경우에 따라 적용되지 않을 수 있다. (아파치를 웹 서버로 이용하는 등) 이럴 경우에는 JSON 파일에 비밀 키 정보를 입력하고, settings.py에서 참고하도록 설정할 수 있다. 우선 아래와 같이 **secrets.json** 파일을 작성한다. (주의 - 이어지는 항목이 없는 경우, 쌍따옴표 뒤에 콤마(,)를 입력해서는 안된다. python git 갱신이력을 깔끔하게 관리하려고 dictionary 마지막 항목에도 콤마를 추가하는 습관이 있어서 그대로 적용했더니 json에서는 오류가 발생했다.)

```json
{
  "SECRET_KEY": "b_4(!id8ro!1645n@ub55555hbu93gaia0 본인의 고유 비밀 키 추가"
}
```

작성한 secrets.json 파일은 버전관리 시스템에 저장되지 않도록 **.gitignore** 문서에 추가한다. 그리고 해당 파일을 SECRET_KEY 값으로 참고하기 위해서 다음 코드를 settings.py에 추가한다.

```python
# settings.py

import os, json
from django.core.exceptions import ImproperlyConfigured


secret_file = os.path.join(BASE_DIR, 'secrets.json') # secrets.json 파일 위치를 명시

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    """비밀 변수를 가져오거나 명시적 예외를 반환한다."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret("SECRET_KEY")
```

쉘에서 python3 manage.py runserver 명령을 입력하니 이 방법을 사용해도 정상적으로 개발 서버가 구동되는 것을 확인 할 수 있었다.

---

# 결론
AWS 루트키가 github 공개 저장소에 추가되면 악용되어서 요금폭탄을 맞을 수도 있다는 이야기는 많이 들어보았다. 하지만 settings에 대해서는 비교적 신경을 쓰지 못했다. Django 초보라면 대부분 SECRET_KEY를 본인의 공개 저장소에 올려본 경험은 있지 않을까? 물론 배포 전에 변경하고 분리하는 것이 가능 하지만, 그에 따른 부작용이 발생 할 수 있으니 처음부터 관리하는게 좋겠다. 앞으로 first commit 이전에 SECRET_KEY를 환경변수 혹은 json 파일로 분리하거나, 초반에는 .gitignore 파일에 settings.py 파일을 추가해 놓는 것도 괜찮겠다는 생각을 했다.
