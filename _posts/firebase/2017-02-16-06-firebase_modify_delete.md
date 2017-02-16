---
layout: post
title: firebase 데이터 수정과 삭제, deploy
category: firebase
tags: [firebase, 파이어베이스]
comments: true
---
# 데이터 수정과 삭제, deploy 배포

## 데이터 수정
#### .update()
- 데이터베이스 [레퍼런스 객체](https://firebase.google.com/docs/reference/js/firebase.database.Reference)의 [].update() 메소드](https://firebase.google.com/docs/database/web/save-data) 사용
- 정의된 경로에서 모든 데이터를 대체하지 않고 일부 키를 업데이트

```javascript
if (selectedKey){
    //update 수정
    memoRef = database.ref('memos/'+userInfo.uid+'/'+selectedKey);
    memoRef.update({
        txt : txt,
        updateDate : new Date().getTime()
    });
}
```

## 데이터 삭제
#### .remove()
- 데이터를 삭제하는 가장 간단한 방법은 해당 데이터 위치의 참조에 대해 remove()를 호출하는 것
- 일반적인 DB는 실시간 변경, 삭제가 불가능하지만 fb는 리얼타임 베이스이기 때문에 가능하다.


## deploy
#### firebase deploy
- firebase 호스팅 기능을 이용한 deploy 전세계 배포!
- CLI 명령어 : `firebase deploy`
