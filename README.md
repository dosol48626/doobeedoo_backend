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



루틴 기능 명세서
https://www.notion.so/API-1a15f780fad780d68d22fae94fb73dbd?pvs=4#1a15f780fad7807e8d32e23589ba69ef

투두 기능 명세
https://www.notion.so/API-1a15f780fad780d68d22fae94fb73dbd?pvs=4#1a15f780fad7808d93eeca79095728ec
