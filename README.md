# 🎵 두비두 프로젝트 - 백엔드  

## 📌 프로젝트 개요  
**두비두 프로젝트**는 사용자가 하루를 효과적으로 계획하고 실행할 수 있도록 돕는 **루틴 및 투두 관리 서비스**입니다.  
Python **3.11** 및 **Django REST Framework** 기반으로 개발되었으며, **MySQL**을 데이터베이스로 사용합니다.  

---

## 🛠 **기술 스택**  
- **백엔드**: Django, Django REST Framework (DRF)  
- **데이터베이스**: MySQL  
- **환경**: Python 3.11 (Anaconda)  
- **인증 방식**: JWT (JSON Web Token)  

---

## 📊 **ERD (데이터베이스 설계)**  
(⚠ ERD 이미지 삽입 필요)  
📌 ERD는 `media/todo_images/dodoERD.png`에 저장되어 있습니다.  

---

## 📜 **API 명세서**  

### 🛠 **1. 회원 기능**  

| 기능 | HTTP 메서드 | 엔드포인트 | Body (JSON) | 토큰 (헤더) |
|------|------------|------------|-------------|-------------|
| **회원가입** | `POST` | `/api/accounts/register/` | `username`<br>`nickname`<br>`password` | 없음 |
| **로그인** | `POST` | `/api/accounts/login/` | `username`<br>`password` | 없음 |
| **로그아웃** | `POST` | `/api/accounts/logout/` | 없음 | `Authorization: Bearer [액세스 토큰]` |
| **비밀번호 변경** | `PUT` | `/api/accounts/password_change/` | `old_password`<br>`new_password` | `Authorization: Bearer [액세스 토큰]` |
| **회원 탈퇴** | `DELETE` | `/api/accounts/delete_account/` | 없음 | `Authorization: Bearer [액세스 토큰]` |
| **토큰 유효성 검증** | `POST` | `/api/accounts/token/verify/` | `token` | `Authorization: Bearer [액세스 토큰]` |

---

### ✅ **2. 투두 기능**  

| 기능 | HTTP 메서드 | 엔드포인트 | Body (JSON) | 토큰 (헤더) |
|------|------------|------------|-------------|-------------|
| **오늘의 투두 보기** | `GET` | `/api/todos/today/` | 없음 | `Authorization: Bearer [액세스 토큰]` |
| **다음 투두 보기** | `GET` | `/api/todos/next/` | 없음 | `Authorization: Bearer [액세스 토큰]` |
| **일정 생성** | `POST` | `/api/todos/` | `title`<br>`dueDate`<br>`priority` | `Authorization: Bearer [액세스 토큰]` |
| **일정 상세 조회** | `GET` | `/api/todos/{id}/` | 없음 | `Authorization: Bearer [액세스 토큰]` |
| **일정 수정** | `PUT` | `/api/todos/{id}/` | `title`<br>`(선택: dueDate, priority)` | `Authorization: Bearer [액세스 토큰]` |
| **일정 삭제** | `DELETE` | `/api/todos/{id}/` | 없음 | `Authorization: Bearer [액세스 토큰]` |
| **중요도별 조회** | `GET` | `/api/todos/?priority=RED~BLACK` | 없음 | `Authorization: Bearer [액세스 토큰]` |
| **검색하기** | `GET` | `/api/todos/?query=검색어` | 없음 | `Authorization: Bearer [액세스 토큰]` |
| **완료 상태 토글** | `POST` | `/api/todos/{id}/toggle/` | 없음 | `Authorization: Bearer [액세스 토큰]` |
| **점수 조회** | `GET` | `/api/todos/score/` | 없음 | `Authorization: Bearer [액세스 토큰]` |

---

### 🗂 **3. 루틴 기능**  

| 기능 | HTTP 메서드 | 엔드포인트 | Body (JSON) | 토큰 (헤더) |
|------|------------|------------|-------------|-------------|
| **루틴 생성** | `POST` | `/api/routines/` | `name` | `Authorization: Bearer [액세스 토큰]` |
| **루틴 조회** | `GET` | `/api/routines/` | 없음 | `Authorization: Bearer [액세스 토큰]` |
| **루틴 상세 조회** | `GET` | `/api/routines/{id}/` | 없음 | `Authorization: Bearer [액세스 토큰]` |
| **루틴 수정** | `PUT` | `/api/routines/{id}/` | `name` | `Authorization: Bearer [액세스 토큰]` |
| **루틴 삭제** | `DELETE` | `/api/routines/{id}/` | 없음 | `Authorization: Bearer [액세스 토큰]` |
| **루틴별 투두 조회** | `GET` | `/api/todos/?routine={루틴ID}` | 없음 | `Authorization: Bearer [액세스 토큰]` |

---

## 🛠 **설치 및 실행 방법**  

### 📌 **1️⃣ 환경 설정 (Anaconda + Python 3.11)**
아래 명령어로 가상 환경을 생성하고 필요한 패키지를 설치하세요.  

```sh
# 가상 환경 생성
conda create -n doobee_env python=3.11
conda activate doobee_env

# 필수 패키지 설치
pip install -r requirements.txt
