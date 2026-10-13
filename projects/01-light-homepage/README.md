# LIGHT — 김해교회 청년교회 홈페이지

> **L**ive **I**n **G**od, **H**elp **T**he other
> 청년부(20~39세)를 위한 공개 홈페이지와 회원 전용 포털

- **기간**: 2026.08.20 ~ 진행 중
- **인원**: 2명 (프론트엔드·인프라 / 백엔드·모바일)
- **저장소**: [gbw11/light-homepage](https://github.com/gbw11/light-homepage)
- **배포**: https://light-homepage-xi.vercel.app

## 개요

| 영역 | 대상 | 구현 |
|---|---|---|
| 공개 | 비로그인 방문자 | Next.js SSG (SEO · 카카오톡 공유 미리보기) |
| 회원 | 로그인한 청년 | 주보 · 사진첩 · 월례회 · 내부 공지 · 출석부 |
| 운영 | 임원 · 전도사 | 글 작성 · 업로드 · 회원 승인/관리 |

```
사용자 ──▶ Vercel (Next.js) ──/api/**─▶ Render (Spring Boot) ──▶ Neon (PostgreSQL)
                                                              └─▶ Cloudflare R2 (파일)
```

**무료 티어만으로 전체 인프라 비용 $0** — R2 사용량이 95%에 도달하면 업로드를 막는 과금 방지 장치를 설계했습니다.

## 기술 스택

| 분야 | 기술 |
|---|---|
| Frontend | Next.js 16 (App Router, Turbopack), React 19, TypeScript, Tailwind CSS v4, TanStack Query, react-hook-form + zod, Tiptap |
| Backend | Spring Boot 3, Java 21, PostgreSQL 16, JWT |
| Mobile | Flutter |
| Infra | Vercel, Render, Neon, Cloudflare R2, Jenkins, GitHub Actions |

## 담당 역할

전체 커밋 약 640건 중 **약 540건** — `frontend/`, `infra/`, `.github/`, `docs/`의 대부분을 작성했습니다.

### 프론트엔드
- 공개 사이트 · 회원 포털 · 운영 화면 전체 구현 (모바일 우선, 화면 설계 21개)
- **회원 열람 게이트**: 사진첩·월례회·내부 공지를 401/403에 따라 분기하고, 권한 검사는 서버가 하도록 경계 유지
- **인증 계약 v1.3 전환**: 명단 대조 가입 → 수단 선택(이메일·카카오) 2단계 가입, 비밀번호 리셋 코드 발급, 계정 삭제
- **PWA를 의존성 없이 구현**: 회원 사진·주보가 캐시에 남지 않아야 한다는 보안 요구사항 때문에, 라이브러리 대신 직접 감사할 수 있는 서비스워커(캐시 화이트리스트)로 구현
- 말씀(설교) 화면: 유튜브 채널 RSS로 목록 자동 갱신, RSS가 간헐적으로 막혀도 예전 스냅샷으로 떨어지지 않게 처리
- 한글 slug 이중 인코딩 버그, 모바일 터치 타겟 44px 미달 등 실사용 이슈 수정

### 인프라 · CI/CD
- **Jenkins + GitHub Actions** 이중 CI: PR 검증(Actions) / 전체 검증·배포(Jenkins)
- **브랜치 정책을 CI가 검사**: `feat/* → *_develop → develop → main` 규약에서 PR의 base가 어긋나면 CI가 실패
- 시크릿 스캔 워크플로, 백엔드 브랜치의 불필요한 Vercel 배포 시도 차단
- **모바일(Flutter) CI/릴리스**: `mobile-v*` 태그로 서명된 APK·AAB 빌드, `apksigner`로 v2 서명 검증, Flutter 이미지 레이어 최적화

### 문서화 · 협업
- 기획(PLAN) · 기능 명세 63개 · 비기능 명세 · **API 명세(FE·BE 계약서)** 작성
- 비호환 API 변경은 `[CONTRACT]` PR + 상대 승인 규칙으로 운영
- 일일 인계(handover) 문서와 의사결정 기록(DECISIONS.md)으로 결정의 근거를 남김

## 트러블슈팅

**프로덕션이 13커밋 동안 동결된 사고**
- 문제: 실제 인물 사진을 제거한 수정이 "배포됨"으로 기록됐지만, Vercel의 Production Branch가 `main`(마일스톤 릴리스 전용, 의도적으로 뒤처진 브랜치)으로 설정돼 있어 반영되지 않았습니다.
- 원인: 문서에는 `develop`이라고 적혀 있었지만 실제 설정은 달랐습니다.
- 해결: 배포 대상은 모두 `develop`을 가리키도록 바꾸고, "문서에 적힌 것은 설정의 증거가 아니다 — 설정 화면을 눈으로 확인한다"는 체크 규칙을 README에 명시했습니다.

**Jenkins에서 워터마크 테스트가 계속 실패**
- 원인: Jenkins 이미지에 한글 폰트가 없어 렌더링 결과가 달라졌습니다. 이미지에 한글 폰트를 추가해 해결했습니다.
