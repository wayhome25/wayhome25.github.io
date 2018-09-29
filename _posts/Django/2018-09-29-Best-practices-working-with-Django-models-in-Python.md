---
layout: post
title: (번역) Best practices working with Django models in Python
category: Django
tags: [django, model]
comments: true
---

> [Best practices working with Django models in Python](https://steelkiwi.com/blog/best-practices-working-django-models-python/) 를 번역한 글입니다. 기존의 모델을 예쁘게 다시 리팩토링 해야하는 일이 생겨서 참고하려고 합니다. 보기 편하려고 정리한 글이라 원문과 일치하지 않는 곳이 있습니다.

## 1. Correct model Naming

- 모델 이름은 단수로 한다. (ex. User, Post, Article)
- 이름 마지막은 명사로 한다. (ex. Some New Shiny Item)
- 모델의 한 단위에 여러 객체에 대한 정보가 포함되지 않은 경우 단수를 사용하는 것이 맞다.

## 2. Relationship Field Naming

-  `ForeignKey`, `OneToOneKey`, `ManyToMany` 같은 관계형 필드의 이름은 때때로 구체적으로 명확하게 지어주는 편이 좋다. (ex. User 모델과  `ForeignKey` 관계를 가진 Article 모델의 경우, 작가에 대한 필드명은 `user` 보다 `author`가 더 적절하다.)

## 3. Correct Related-Name

- queryset 을 리턴하는 관계형 필드의 이름은 `복수형` 이 적절하다.

- 대부분의 경우, 모델명의 복수형을 사용하며 꼭 `related_name` 옵션을 지정해주자.



  ```python
  class Owner(models.Model):
      pass
  class Item(models.Model):
      owner = models.ForeignKey(Owner, related_name='items')
  ```

## 4. Do not use ForeignKey with unique=True

- `ForeignKey` 필드에는 `unique=True` 옵션을 사용하지 않는다.  (`OneToOneField` 를 사용하면 된다)

## 5. Attributes and Methods Order in Model

- 모델에서의 속성과 메소드의 순서는 아래가 바람직하다.
  (아래의 순서는 공식문서를 참고하여 작성됨)
  - constants (choices 등에 사용될 상수값)
  - 모델 필드
  - 커스텀 manager 지정
  - class Meta
  - def __str__()
  - def clean()
  - def save()
  - def get_absolute_url()
  - 그 밖의 커스텀 메소드


## 6. Adding a Model via Migration

- 모델을 추가해야하는 경우 모델 클래스를 생성 한 후 manage.py `makemigrations` 과 `migrate` 명령을 연속적으로 실행한다.

## 7. Denormalisations

- 관계형 데이터베이스에서 비정규화를 무분별하게 사용해서는 안된다.
- 일부러 의식적으로 비정규화하는 경우는 제외한다. (예 : 생산성을 위해서)
- 데이터베이스 설계 단계에서 많은 양의 데이터를 비정규화 해야 한다면 NoSQL을 사용하는 것이 좋다.
- 그러나 많은 양의 데이터가 어쩔수 없는 비정규화를 필요로 하지 않는다면, `JsonField` 를 사용하여 데이터를 저장하는것을 고려하자.

## 8. BooleanField

- `BooleanField`에서 `null=True` `blank=True` 옵션은 사용하지 말자.  (필요한 경우에는 `NullBooleanField` 를 쓰면 된다. )
- `default` 옵션을 꼭 주자.

## 9. Business Logic in Models

- 프로젝트의 비지니스 로직을 둘 가장 적절한 위치는 모델의 메소드와 매니저이다.
- 비지니스 로직을 모델에 두는 것이 어렵거나 불가능한 경우,  form 이나 serializer를 활용할 수 있다.

## 10. Field Duplication in ModelForm

-  ModelForm 이나 ModelSerializer 에서 모델 필드를 중복으로 정의하지 말자
- form 에서 모델의 모든 필드를 사용하도록 지정하려면 MetaFields를 사용하자.
- 필드의 위젯을 다시 정의해야하는 경우 Meta 위젯을 사용하여 위젯을 정의할 수 있다.

## 11. Do not use ObjectDoesNotExist

- `ObjectDoesNotExist` 대신에  `ModelName.DoesNotExist` 를 사용하자

## 12. Use of choices

choices 를 사용할 때는 아래를 주의한다.

- 데이터베이스에 저장하는 값은 숫자 대신 문자열을 명시적으로 사용하자

- 상수명은 대문자를 사용한다.

- 모델 필드 정의 전에 choices 용 상수를 먼저 정의한다.

- choices가 status 목록인 경우 상태 순서에 맞게 정의한다. (ex. new, in_progress, completed)

- [model_utils](https://github.com/jazzband/django-model-utils) 라이브러리의 Choices 를 활용해보자. (+ 추가: [django-choices](https://pypi.org/project/django-choices/) 도 활용해보자)

  ```python
  # model_utils 라이브러리 활용 예시
  from model_utils import Choices

  class Article(models.Model):
      # Choices
      STATUSES = Choices(
          (0, 'draft', _('draft')),
          (1, 'published', _('published'))   )

      # Fields
      status = models.IntegerField(choices=STATUSES, default=STATUSES.draft)


  # django choices 라이브러리 활용 예시
  from djchoices import DjangoChoices, ChoiceItem

  class Person(models.Model):
      # Choices
      class PersonType(DjangoChoices):
          customer = ChoiceItem("C")
          employee = ChoiceItem("E")
          groundhog = ChoiceItem("G")

      # Fields
      name = models.CharField(max_length=32)
      type = models.CharField(max_length=1, choices=PersonType.choices)
  ```

## 13. Why do you need an extra .all()?

- ORM에서 filter(), count() 등을 사용하기 전에 불필요한 .all() 을 쓰지말자

## 14. Many flags in a model?

- 여러개의 BooleanFields 필드는 하나의 필드로 교체하자 (ex. status)


  ```python
  # 변경전
  class Article(models.Model):
      is_published = models.BooleanField(default=False)
      is_verified = models.BooleanField(default=False)
      …

  # 변경후
  class Article(models.Model):
      STATUSES = Choices('new', 'verified', 'published')
      status = models.IntegerField(choices=STATUSES, 								 default=STATUSES.draft)
      …
  ```


## 15. Redundant model name in a field name

- 필드명에 모델명을 중복해서 사용하지 않는다 (ex. User모델의 user_status 필드는 status 필드명이 더 적합하다.)

## 16. Dirty data should not be found in a base

- 특별한 경우가 아니면 IntegerField 대신에 항상 PositiveIntegerField 를 사용하자.
  이를 통해서 의도치 않은 데이터가 저장되는 것을 원천 차단 할 수 있다.
- 같은 이유로 유니크한 데이터에는 항상 unique, unique_together 옵션을 사용하자
-  required=False 를 모든 필드에 사용하는 것을 피하자

## 17. Getting the earliest/latest object

- order_by('created')[0]  대신에 ModelName.objects.earliest('created') 를 사용할 수 있다.
- Meta 클래스에 get_latest_by 을 정의하여 순서를 지정할 수 있다.
- .first(), .last() 는 값이 없으면 None 을 리턴하지만 .earliest(), .latest() 는 값이 없으면 DoesNotExist 예외를 발생시키기 때문에 주의해야 한다.
- (+ 추가: 익숙하지 않은 문법이라 찾아보니 가독성 향상을 위해 활용하는 경우가 있다고 한다.  참고 - [Django Tips #17 Using QuerySet Latest & Earliest Methods](https://simpleisbetterthancomplex.com/tips/2016/10/06/django-tip-17-earliest-and-latest.html))

## 18. Never make len(queryset)

- queryset 결과의 길이를 확인하기 위해서 len 을 쓰지말자. 대신 .count()를 활용하자.
- 예를들면 `len(ModelName.objects.all())` 는 DB 테이블에서 모든 데이터를 가져오고 이를 파이썬 객체로 변환하는 작업을 수행한다. `ModelName.objects.count()` 를 활용하면 SQL의 `COUNT()`를 사용하기 때문에 파이썬 객체로 변환할 필요가 없어서 더 적은 리소스를 사용하게 된다.

## 19. if queryset is a bad idea

-  `if queryset: do something` 대신에  `queryset.exists(): do something` 을 사용하여 불필요한 데이터베이스 접근을 줄이자.

## 20. Using help_text as documentation

- 모델의 `help_text` 옵션을 활용하여 각 필드에 대한 설명을 추가하자.
- [추가: ModelForm 을 사용하지 않더라도 documentation을 위해서 help_text를 활용하면 좋다](https://docs.djangoproject.com/ko/2.1/ref/models/fields/#django.db.models.Field.help_text)

## 21. Money Information Storage

- 돈에 관련된 필드는 DecimalField 를 사용하자.

## 22. Remove _id

-  _id 접미어를 ForeignKeyField 와  OneToOneField에 사용하지 말자.

## 23.  Define __str__

-  abstract models 을 제외한 모든 모델에 `__str__` 메소드를 정의하자

## 24. Transparent fields list

- ModelForm 을 정의할때 사용할 필드를 명시하기 위해서  Meta.fields 를 활용하자.
- `Meta.fields="__all__"` / `Meta.exclude` 는 사용하지 말자.

## 25. Do not heap all files loaded by user in the same folder

- 하나의 폴더에 많은 파일을 저장하면 파일 시스템이 필요한 파일을 검색하는데 시간이 더 걸린다.
  유저가 업로드한 파일등을 저장할때는 아래와 같이 폴더를 나눠서 저장하는 편이 좋다.

```python
def get_upload_path(instance, filename):
    return os.path.join('account/avatars/', now().date().strftime("%Y/%m/%d"), filename)

class User(AbstractUser):
    avatar = models.ImageField(blank=True, upload_to=get_upload_path)
```

아래 링크를 통해서 더 많은 정보를 얻을 수 있다.

- [case study page.](https://steelkiwi.com/projects/)  
- [top 10 Python frameworks in 2018](https://steelkiwi.com/blog/top-10-python-web-frameworks-to-learn/)
- [choose Django for your project](https://steelkiwi.com/blog/why-django-best-web-framework-your-project/).
