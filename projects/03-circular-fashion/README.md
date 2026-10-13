# Circular Fashion — 순환 패션 업사이클 플랫폼

> 버려질 패션 소재가 새로운 제품으로 순환하도록 연결하고, 그 과정을 검증 가능한 이력으로 남기는 서비스
> SSAFY 15기 프로젝트 · 6인 팀

- **저장소**: [gbw11/circular-fashion](https://github.com/gbw11/circular-fashion) (팀 GitLab 결과물을 모은 포트폴리오용 스냅샷)
- **담당**: 인프라(DevOps) → User/Wallet 인증 → 소재(Material) 관리 도메인

## 개요

폐원단·데드스톡을 업사이클 브랜드에 직접 연결하는 **P2P 마켓플레이스**와, 소재가 제품이 되기까지를 블록체인에 기록하는 **트레이서빌리티**를 하나의 흐름으로 묶었습니다.

```
소재 등록 → 거래 → 결제 → 배송·수령 → 가공 의뢰 → 생산 → 제품화 → QR로 이력 조회
```

| 역할 | 지갑 | 하는 일 |
|---|---|---|
| SUPPLIER | ✅ | 폐소재 등록·판매, 발생 정보 서명 |
| BRAND | ✅ | 소재 구매, 가공 의뢰, 생산, 제품 등록 |
| PROCESSOR | ✅ | 소재 가공, 결과 수량 기록·서명 |
| CONSUMER | ❌ | 제품 구매, QR로 이력 조회 |

블록체인은 "진짜 폐소재인지"는 판별하지 못하지만, **"누가 무엇을 언제 기록·확인했는지"** 를 한쪽이 임의로 바꾸기 어렵게 합니다.

## 기술 스택

| 분야 | 기술 |
|---|---|
| Backend | Spring Boot, MySQL, QueryDSL, Spring Security |
| Frontend | React, TypeScript, Vite |
| Blockchain | Solidity (Hardhat), 이더리움 계열 테스트넷 |
| AI | Python |
| Infra | AWS EC2, Docker Compose, Nginx, Jenkins Multibranch |

## 담당 역할

### 인프라 / DevOps
- AWS EC2 + Docker Compose 배포 환경 구축 (Nginx 리버스 프록시, HTTPS, 도메인)
- **Jenkins Multibranch Pipeline**으로 파트별 브랜치(`*/develop`, `*/master`) CI/CD 자동화, **헬스체크 실패 시 자동 롤백**
- 운영과 완전히 격리된 **상시 통합 테스트 환경(`/test/`)** — 각 파트가 `develop`에 병합할 때마다 자동 배포되어 머지 전 통합 상태 확인
- **마이그레이션 preflight 도구**: 스키마 변경 누락으로 배포가 죽던 문제를, 배포 전 자동 검증 + 안전한 경우 자동 적용으로 해결
- 환경변수·시크릿 관리, CORS·인증 관련 운영 장애 대응

### User / Wallet 인증
- 지갑 서명 기반 로그인

### Material / Product 도메인
- 소재 등록·조회·수정, 보유 수량(Balance/Available) 관리
- 소재 발생 증빙(Evidence), 소재 이력(Lineage) 조회
- 생산 배치(ProductionBatch) 투입/산출 관리, 소재 소비(Consume) 처리
- 잔여 소재(Scrap) 생성, **업사이클 비율** 계산
- 제품 모델/개별 제품(ProductModel/ProductItem) 관리

## 설계 문서

기능마다 **설계(spec) → 구현 계획(plan)** 순서로 문서를 먼저 쓰고 구현했습니다.
(공통 응답·예외 설계, Spring Boot 패키지 구조, 보안·JPA 기반, 지갑 서명 로그인, 파일 업로드 정책, 역할-권한 매트릭스 등)
