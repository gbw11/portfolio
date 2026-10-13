# SSAFY 급식봇

> 매일 점심 메뉴와 실제 배식 사진을 Mattermost 채널로 자동 전송하는 봇

- **기간**: 2026.08 ~ 2026.09
- **인원**: 1명 (기획 · 개발 · 운영)
- **저장소**: [gbw11/ssafy-lunch-bot](https://github.com/gbw11/ssafy-lunch-bot)
- **스택**: Python, requests, holidays, pytest, GitHub Actions, cron-job.org

## 구조

```
lunchbot/
  __main__.py   CLI + 파이프라인 (메뉴 조회 → 사진 채우기 → 전송)
  welplan.py    메뉴 원본 + 당일 사진 1차 소스
  mealcloud.py  사진 폴백 (welstory-meal.cloud)
  welstory.py   사진 폴백 (웰스토리 API)
  message.py    Mattermost 마크다운 (사진 크기 통일)
  notify.py     전송 (여러 웹훅 / API 토큰)
  workdays.py   주말·공휴일 판별
```

## 주요 기능과 설계

- **사진 소스 폴백 체인**: Welplan → welstory-meal.cloud → 웰스토리. 플레이스홀더 이미지는 걸러내고 사진 없이 전송
- **메뉴명 기준 매칭**: 소스마다 코너명과 순서가 날마다 달라서, 코너가 아니라 메뉴명으로 사진을 짝지음
- **사진 대기**: 실제 배식 사진은 10:30 전후에 올라오므로 최대 N분 대기 후 전송 (대개 11:00 전후)
- **끼니 구분**: 조식 사진이 점심 글에 실리던 문제를 `mealTimeId`로 중식만 남겨 해결
- **휴일 자동 스킵**: 음력 공휴일·대체공휴일을 `holidays` 패키지로 계산, 근로자의날 포함
- **여러 방 전송**: 웹훅을 콤마로 이어 붙이면 여러 방에 전송, 한 방이 실패해도 나머지는 전송하고 종료 코드로 실패 보고
- **테스트**: 모듈별 pytest 8개 파일, GitHub Actions CI

## 트러블슈팅

**GitHub Actions cron 지연**
- GitHub 자체 cron은 지연이 심해 점심 전에 도착하지 못했습니다. 외부 cron(cron-job.org)이 평일 10:39에 `workflow_dispatch`로 트리거하도록 바꿨습니다.

**웰스토리 API 자동 로그인 불가 — 조사 후 경로 폐기**
- ID/PW 로그인은 앞단 WAF(Imperva)가 봇으로 판단해 JS 챌린지 HTML을 돌려줬습니다.
- 브라우저에서 얻은 토큰은 JWT `exp = iat + 600`, 즉 **10분짜리**라 하루 한 번 도는 cron에 쓸 수 없었습니다.
- 유효 시간 안에 `Bearer`로 실어도 빈 응답 → 브라우저에서만 통하는 추가 조건이 있음을 확인했습니다.
- 결론: 조사 결과를 문서로 남기고, 계정이 필요 없는 소스(Welplan + meal.cloud)로 사진을 채우도록 설계를 바꿨습니다. 장수명 토큰 경로를 찾으면 설정값만 채우면 되도록 코드는 남겨 두었습니다.
