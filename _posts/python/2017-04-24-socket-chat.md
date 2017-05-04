---
layout: post
title: 파이썬 소켓 모듈을 사용한 간단한 채팅프로그램 구현
category: python
comments: true
---
> 개인공부 후 자료를 남기기 위한 목적임으로 내용 상에 오류가 있을 수 있습니다.          

## 소켓 (socket)

- 소켓 : 소켓을 생성한다는 의미는 호스트가 통신을 하기 위해 필요한 리소스를 할당 한다는 의미
- 소켓의 선언 : python의 소켓은 C나 자바에 비해 비교적 단순한 모습을 취하고 있음

```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

## AF(주소 체계)
- AF_INET - IPv4 프로토콜
- AF_INET6 - IPv6 프로토콜
- AF_LOCAL - Local 통신 UNIX 프로토콜

## Client
```python
import socket


s = socket.socket()
host = socket.gethostname()
port = 12222

s.connect((host, port))
print( 'Connected to', host)

while True:
    z = input("Enter something for the server: ")
    s.send(z.encode('utf-8'))
    # Halts
    print ('[Waiting for response...]')
    print ((s.recv(1024)).decode('utf-8'))

```

## Server

```python
import socket


s = socket.socket()
host = socket.gethostname()
port = 12222
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

s.listen(5)
c = None

while True:
   if c is None:
       # Halts
       print( '[Waiting for connection...]')
       c, addr = s.accept() #  (socket object, address info) return
       print( 'Got connection from', addr)
   else:
       # Halts
       print( '[Waiting for response...]')
       print((c.recv(1024)).decode('utf-8'))
       q = input("Enter something to this client: ")
       c.send(q.encode('utf-8'))

```
