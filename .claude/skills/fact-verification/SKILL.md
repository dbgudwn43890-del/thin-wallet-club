# Fact Verification Skill

## Purpose

후보 데이터(`data/candidates/`)를 받아
검증 결과(`data/verified/` or `data/rejected/`)를 출력한다.

공식 출처를 직접 확인하고, 핵심 정보 6개를 채우고, TODO를 0으로 만든다.
이 스킬이 통과시킨 정보만 원고에 확정 문장으로 쓸 수 있다.

현재 구조 세팅 단계에서는 실제 외부 URL 검증을 실행하지 않는다.
이 문서는 정식 운영 시 반복 검증 절차를 정의한다.

---

## 입력 조건

- 입력 파일: `data/candidates/{category}_candidates.yml`
- 필수 상태: `status: idea or pre_selected`
- 스키마 참조: `schemas/verification.schema.yml`
- 출처 기준: `ops/source_rules.md`

---

## 출력

- 통과/주의: `data/verified/{id}_{slug}.yml` (result: pass or caution)
- 폐기: `data/rejected/{slug}.yml` (result: fail)
- 상태 업데이트: `status: verified` or `status: rejected`

이 스킬은 원고, 캡션, 디자인 프롬프트를 작성하지 않는다.

---

## 실행 절차

### Step 1. 출처 등급 확인
`ops/source_rules.md` 기준으로 출처 등급을 확인한다.

- Tier 1: 정부/기관/브랜드 공식 홈페이지 → 검증 진행
- Tier 2: 주요 언론, 공식 블로그 → Tier 1 교차 확인 필수
- Tier 3: 개인 블로그, SNS → 단독 출처로 불가, Tier 1 찾아야 함
- 출처 없음 → 즉시 fail 처리

### Step 2. URL 접근 확인
공식 URL에 직접 접속하여 정보를 확인한다.
접속 불가 시 다른 공식 경로로 재확인 시도.
재확인 불가 시 → fail 처리.

### Step 3. 핵심 정보 6개 채우기

| 항목 | 확인 질문 |
|------|---------|
| 대상 | 나이/거주/소득/재학 조건이 명확한가? |
| 지역 | 서울/수도권 대상인가? |
| 기간 | 시작일~종료일 or 마감일이 명확한가? |
| 비용 | 무료인가? 얼마인가? |
| 신청/이용 방법 | 어디서 어떻게 하는가? |
| 주의사항 | 탈락 조건, 제한 사항이 있는가? |

6개 중 4개 미만이 확인되면 → caution 처리.
대상/기간/비용 중 하나라도 확인 불가 → fail 처리.

### Step 4. 마감 유효성 확인
오늘 날짜 기준으로 마감일이 지났는가?
발행 리드타임(최소 3일)을 고려했을 때 업로드 전에 마감되는가?
→ 조건 해당 시 fail 처리.

### Step 5. 비용 기준 확인
무료 또는 3만 원 이하인가?
유료 전환 가능성이 있는가?
→ 3만 원 초과 시 caution 처리 + Curator 판단에 맡긴다.

### Step 6. 검증 가능 문장 추출
카드뉴스 원고에 그대로 쓸 수 있는 확정 문장을 뽑는다.
확인되지 않은 내용은 절대 확정 문장으로 작성하지 않는다.

### Step 7. 결과 파일 저장
스키마 `schemas/verification.schema.yml` 형식으로 파일을 저장한다.

---

## 폐기 사유 코드

| 코드 | 사유 |
|------|------|
| NO_SOURCE | 공식 출처 없음 |
| EXPIRED | 마감 지남 |
| WRONG_COST | 무료/금액 정보 불일치 |
| WRONG_REGION | 서울/수도권 대상 아님 |
| UNCLEAR_TARGET | 대상 조건 불명확 |
| AD_UNLABELED | 광고성 정보인데 미표시 |
| COST_EXCEEDED | 비용 기준 초과 (Curator 결정 없이) |

---

## 품질 기준

검증 결과 제출 전 확인:
- [ ] 공식 URL 직접 확인 완료
- [ ] verified_at이 오늘 날짜
- [ ] 핵심 정보 6개 중 6개 확인 (pass) or 4~5개 (caution)
- [ ] todo_remaining이 pass 기준 0개
- [ ] usable_sentences가 1개 이상
