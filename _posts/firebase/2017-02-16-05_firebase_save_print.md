---
layout: post
title: firebase 데이터 출력 및 저장
category: firebase
tags: [firebase, 파이어베이스]
comments: true
---

# 데이터 출력, 저장과 메모 상세보기 기능

## 데이터 출력

### DB 예시 (jason)

```jason
{
  "users": {
    "alovelace": {
      "name": "Ada Lovelace",
      "contacts": { "ghopper": true },
    },
    "ghopper": { ... },
    "eclarke": { ... }
  }
}
```



### 참고문서
- [Firebase 실시간 데이터베이스](https://firebase.google.com/docs/database/)
- [Firebase 데이터베이스 구조화](https://firebase.google.com/docs/database/web/structure-data)
- [Firebase 웹에서 데이터 검색](https://firebase.google.com/docs/database/web/retrieve-data)


## 데이터 저장

### .push()
- 데이터베이스 [레퍼런스 객체](https://firebase.google.com/docs/reference/js/firebase.database.Reference)의 [push 함수(메소드)](https://firebase.google.com/docs/reference/js/firebase.database.Reference#push)를 사용
- A Reference represents a specific location in your Database and can be used for reading or writing data to that Database location.
- You can reference the root or child location in your Database by calling firebase.database().ref() or firebase.database().ref("child/path").
- 데이터 목록에 추가, push()를 호출할 때마다 Firebase에서 고유 식별자로도 사용할 수 있는 ***고유 키(예: user-posts/<user-id>/<unique-post-id>)*** 를 생성
- textarea에 글이 있는 경우만 save를 하는 로직 추가
- 함수 내에서 return이 들아가면 그 부분에서 함수는 종료

```javascript
function save_data(){
  var memoRef = database.ref('memos/'+userInfo.uid);
  var txt = $(".textarea").val();
  if (txt === ''){
    return; // 함수를 종료시킨다
  }
  //push
  memoRef.push({
    txt : txt,
    creatData : new Date().getTime()
  })
}
```

## 데이터 검색 (상세보기 기능)

### .ref().once()
- value 이벤트를 사용하여 이벤트 발생 시점에 특정 경로에 있던 내용의 정적 스냅샷을 읽을 수 있습니다.
- 변경을 수신 대기하지 않고 단순히 데이터의 스냅샷만 필요한 경우가 있습니다. 이후에 변경되지 않는 UI 요소를 초기화할 때가 그 예입니다. 이러한 경우 once() 메소드를 사용하면 시나리오가 단순해집니다. 이 메소드는 한 번 호출된 후 다시 호출되지 않습니다.

### 참고문서
- [firebase reference](https://firebase.google.com/docs/reference/js/firebase.database.Database)
- [데이터 검색](https://firebase.google.com/docs/database/web/retrieve-data)
