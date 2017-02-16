---
layout: post
title: firebase 사용자 인증
category: firebase
tags: [firebase, 파이어베이스]
comments: true
---
# 사용자 인증

## firebase 인증 서비스 사용
- Firebase App은 여러 Firebase 서비스를 사용할 수 있습니다. firebase 네임스페이스로 각 서비스에 액세스할 수 있습니다.
  - firebase.auth() - 인증
  - firebase.storage() - 저장소
  - firebase.database() - 실시간 데이터베이스


## 인증 제공업체 개체의 인스턴스[^1] 생성
[^1]: 인스턴스는 객체를 생성하기 위해 만들어진 또 다른 객체를 바로 인스턴스(instance)라고 부른다.

```javascript
var provider = new firebase.auth.GoogleAuthProvider();
```

## 현재 로그인한 사용자 가져오기
- 현재 사용자를 가져올 때 권장하는 방법은 다음과 같이 Auth 개체에 관찰자를 설정하는 것입니다.
```javascript
firebase.auth().onAuthStateChanged(function(user) {
  if (user) {
    // User is signed in.
  } else {
    // No user is signed in.
  }
});
```

## 로그인 팝업창 띄우기
```javascript
firebase.auth().signInWithPopup(provider);
```


#### 참고문서
- [firebase 인증가이드](https://firebase.google.com/docs/auth/web/manage-users)
- [JavaScript에서 Google 로그인으로 인증하기](https://firebase.google.com/docs/auth/web/google-signin)
- [Firebase에서 사용자 관리하기](https://firebase.google.com/docs/auth/web/manage-users)
