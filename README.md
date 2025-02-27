두비두 프로젝트 백엔드 깃허브 입니다.
ERD, API명세서, 데이터베이스 설정, 아나콘다…해줘야하나?
파이썬 3.11 아나콘다
데이터 베이스 mysql사용


api/todos/score가 계속 불러와진다고요?

네 그거 맞아요…ㅠㅠ

api명세서
회원 기능 명세서
| 기능 | HTTP 메서드 | 엔드포인트 | Body (JSON) | 토큰 (헤더) |
|------|------------|------------|-------------|-------------|
| **회원가입** | `POST` | `/api/accounts/register/` | `username`<br>`nickname`<br>`password` | 없음 |
| **로그인** | `POST` | `/api/accounts/login/` | `username`<br>`password` | 없음 |
| **로그아웃** | `POST` | `/api/accounts/logout/` | 없음 | `Authorization: Bearer [액세스 토큰]` |
| **비밀번호 변경** | `PUT` | `/api/accounts/password_change/` | `old_password`<br>`new_password` | `Authorization: Bearer [액세스 토큰]` |
| **회원 탈퇴** | `DELETE` | `/api/accounts/delete_account/` | 없음 | `Authorization: Bearer [액세스 토큰]` |
| **토큰 유효성 검증** | `POST` | `/api/accounts/token/verify/` | `token` | `Authorization: Bearer [액세스 토큰]` |



투두 기능 명세서
### ✅ 투두 관련 API

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




루틴 기능 명세서
### 🗂 루틴 관련 API

| 기능 | HTTP 메서드 | 엔드포인트 | Body (JSON) | 토큰 (헤더) |
|------|------------|------------|-------------|-------------|
| **루틴 생성** | `POST` | `/api/routines/` | `name` | `Authorization: Bearer [액세스 토큰]` |
| **루틴 조회** | `GET` | `/api/routines/` | 없음 | `Authorization: Bearer [액세스 토큰]` |
| **루틴 상세 조회** | `GET` | `/api/routines/{id}/` | 없음 | `Authorization: Bearer [액세스 토큰]` |
| **루틴 수정** | `PUT` | `/api/routines/{id}/` | `name` | `Authorization: Bearer [액세스 토큰]` |
| **루틴 삭제** | `DELETE` | `/api/routines/{id}/` | 없음 | `Authorization: Bearer [액세스 토큰]` |
| **루틴별 투두 조회** | `GET` | `/api/todos/?routine={루틴ID}` | 없음 | `Authorization: Bearer [액세스 토큰]` |
