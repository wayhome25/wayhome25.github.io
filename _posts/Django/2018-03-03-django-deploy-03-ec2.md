---
layout: post
title: Django 배포연습 3 - EC2 ubuntu 서버 인스턴스 생성 및 기본 설정
category: Django
tags: [django, deploy, ec2, aws]
comments: false
---

> nginx, uwsgi, docker를 활용한 배포 연습 과정을 기록한 글입니다.   
> 개인 공부 후 자료를 남기기 위한 목점임으로 내용상에 오류가 있을 수 있습니다.
>
> - nginx, uwsgi를 통해서 아마존 EC2에서 장고 앱 어플리케이션을 실행시켜 보는 것을 목표로 한다.
> - 최소한의 설정만을 포함한다.

## 용어정리
- 가상서버 : CPU와 메모리를 가진 클라우드 내 서버
- 인스턴스 (instance) : AWS에서 가상 서버를 부르는 용어
- EC2 (Elastic Compute Cloud) : 가상 인스턴스를 운영하는 서비스
- 보안 그룹(security group) : 인스턴스에 대한 트래픽을 제어하는 가상 방화벽 역할
- IAM (Identity and Access Management) : 사용자 엑세스 및 암호화 키 관리
- 관리 콘솔 : AWS 서비스를 모두 관리하는 사용자 인터페이스


## EC2 인스턴스 생성
- [aws amazon](https://aws.amazon.com/ko/) 서비스에서 EC2 => 인스턴스 시작 선택
- 프리티어에서 사용 가능한 Ubuntu Server 16.04 LTS (HVM), SSD Volume Type 선택
- 검토 및 시작을 선택하여 기본 조건을 사용하는 인스턴스를 생성

### 키페어 생성
- EC2 인스턴스 생성시 키 페어 지정이 필요
  - 퍼블릭 키 : AWS에 저장
  - 프리이빗 키 : 사용자가 저장
- 프라이빗 키는 키 페어 생성 시점에 한번만 다운로드 가능
- 키페어를 사용하여 SSH를 통해 EC2 인스턴스에 접속 가능
- 다운받은 .pem파일을 ~/.ssh폴더에 넣기

![screen 35](https://i.imgur.com/wjweMWs.png)

### SSH를 통한 EC2 접속
- [SSH를 사용하여 Linux 인스턴스에 연결](https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)
- .zshrc에 alias를 추가하면 손쉽게 EC2에 접속할 수 있다.

```shell
ssh -i <인증서위치> <계정>@<인스턴스 퍼블릭 DNS>
ssh -i ~/.ssh/key.pem ubuntu@ec2-1111-11-111lap-northeast-2.compute.amazonaws.com
```

- 아래와 같은 에러 발생시 chmod 400 <pem file>로 소유주만 읽을 수 있도록 권한설정을 해준다.

```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0644 for '/Users/Leehyunjoo/.ssh/key-pairs-test.pem' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "/Users/Leehyunjoo/.ssh/key-pairs-test.pem": bad permissions
Permission denied (publickey).

❯ chmod 400 key-pairs-test.pem
```

### IAM 유저 생성
- 사용자 엑세스 및 암호화 키 관리 (Identity and Access Management)
- AWS에서 모든 권한을 다 사용할 수 있는 ROOT 유저 대신, 특정 권한만 가진 유저 생성
- [aws amazon](https://aws.amazon.com/ko/) 서비스에서 IAM 선택
- AmazonEC2FullAccess 권한을 가진 IAM 유저 추가
- 참고 : [AWS 계정의 IAM 사용자 생성](https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/id_users_create.html#id_users_create_console)


## EC2 인스턴스 ubuntu 기본 설정
- EC2 인스턴스를 생성후 ssh로 ubuntu 서버에 접속하여 기본적인 프로그램을 설치한다.


### python-pip설치

```
sudo apt-get install python-pip
```

### zsh 설치

```
sudo apt-get install zsh
```


### oh-my-zsh 설치

```
sudo curl -L http://install.ohmyz.sh | sh
```


### Default shell 변경

```
sudo chsh ubuntu -s /usr/bin/zsh
```

### pyenv requirements설치

[공식문서](https://github.com/yyuu/pyenv/wiki/Common-build-problems)

```
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils
```

### pyenv 설치

```
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
```

### pyenv 설정을 .zshrc에 기록

```
vi ~/.zshrc
export PATH="/home/ubuntu/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

## Django 관련 설정


### 장고 애플리케이션은 /srv Directory 사용
- 폴더 권한 계정 변경 (root 유저 => ubuntu 유저)
- scp 명령 실행시 쓰기 권한을 주기 위함
- [Linux Directory Structure (File System Structure) Explained with Examples](http://www.thegeekstuff.com/2010/09/linux-file-system-structure/?utm_source=tuicool)

```  
sudo chown -R ubuntu:ubuntu /srv/
```

### 프로젝트 소스코드 추가 1 - git clone
- github에 올라간 프로젝트 소스코드를 ubuntu 서버에 clone
- secret_key 등이 포함된 폴더는 공개저장소에 올리지 않기 때문에 별도로 설정해줘야 함

```
git clone <자신의 프로젝트>
```

### 프로젝트 소스코드 추가 2 - secure copy (clone으로 대체 가능)
- [SCP를 사용하여 Linux에서 Linux 인스턴스로 파일 전송](https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)

```
scp -i <인증서위차> -r <프로젝트폴더> ubuntu@<인스턴스 퍼블릭 DNS>:/srv/deploy_ec2
scp -i ~/.ssh/key.pem -r /Users/Dev/deploy_ec2/ ubuntu@ec2-111-1111-111.ap-northeast-2.compute.amazonaws.com:/srv/deploy_ec2"
```

### pyenv 3.4.3설치 및 virtualenv생성

```
cd <clone 혹은 copy한 프로젝트 폴더>
pyenv install 3.4.3
pyenv virtualenv deploy_ec2
pyenv local deploy_ec2
```

### requirements설치

```
pip install -r requirements.txt
```

## runserver 테스트
- 0:8000 으로 지정필요
- 웹 브라우저에서 <퍼블릭 DNS:8000> 로 접속하기 위해서는 보안그룹(security group) 설정이 필요

```
cd deploy_ec2/django_app/
python manage.py runserver 0:8000 --settings=config.settings.debug
```

### 보안그룹 인바운드 설정 수정
- 보안 그룹(security group)은 하나 이상의 인스턴스에 대한 트래픽을 제어하는 가상 방화벽 역할
- [Linux 인스턴스에 대한 Amazon EC2 보안 그룹](https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/using-network-security.html)
- 보안그룹 기본 인바운드 설정
   - Type: SSH
   - Protocol: TCP
   - Port Range: 22
   - Source : 0.0.0.0/0 (전세계 어디서나)
- SSH 접속은 사무실 혹은 집의 ip 에서만 가능하도록
- Custom TCP Rule 8000번 포트 추가 (runserver시 8000번 포트를 통해서 접속)

![screen 36](https://i.imgur.com/gtjIuzD.png)

#### ALLOWED_HOSTS 설정
- settings.py의 ALLOWED_HOSTS에 특정 서버의 IP주소나 도메인에 대해서만 장고 웹어플리케이션이 서빙을 수행할 수 있도록 한다.

```
ALLOWED_HOSTS = [
	'<ec2 domain name'>,
	또는
	'.amazonaws.com',  # 구체적으로 작성하는 편이 좋음
]
```

## 참고
- [Django Girs를 위한 Django on AWS](http://awsblogskr.s3-ap-northeast-2.amazonaws.com/pdf/2015-06-djangogirls-seoul-aws.pdf)
- [당신이 AWS 계정을 만들고 가장 먼저 해야 할 일 들과 하지 말아야 할 일 들](http://www.awskr.org/2017/01/your-aws-first-days-todo-list/)
