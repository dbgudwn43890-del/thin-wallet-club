# Content Lifecycle

콘텐츠 하나가 아이디어에서 아카이브까지 이동하는 전체 경로.

현재 프로젝트는 구조 세팅 단계다.
아래 라이프사이클은 정식 운영 시 사용할 절차이며, 지금 단계에서는 실제 후보 수집과 제작을 시작하지 않는다.

---

## 전체 라이프사이클

```
Week N-1 (리서치 주간)
  Scout 수집 → Verifier 검증 → Curator 선별

Week N (제작 주간)
  Editor 브리프 → Editor 원고 → Design Director 디자인 프롬프트

Week N (검수/발행)
  Human Review → 업로드

Week N+1 (성과)
  Growth Analyst D+3 분석

Month N+1 (아카이브)
  D+30 아카이브 처리
```

---

## 단계별 상세

### Phase 1: 리서치 (D-7 ~ D-5)

**담당:** Trend Scout / Policy Scout
**커맨드:** `/research-candidates`
**출력:** `data/candidates/{category}_candidates.yml`

수집 기준:
- `sources/*.yml` 에 등록된 출처 우선
- 비용: 무료 우선, 최대 3만 원 이하
- 지역: 서울/수도권
- 시의성: 이미 종료된 후보 제외. 종료 임박/시작 예정 후보는 `ops/quality_rules.md`의 전시/행사 일정 판단 기준 적용

수집 목표: 주당 8~12개 (실제 제작 수의 2~3배)

---

### Phase 2: 검증 (D-6 ~ D-5)

**담당:** Verifier
**커맨드:** `/verify-candidate`
**스킬:** `fact-verification`
**입력:** `data/candidates/`
**출력:** `data/verified/` or `data/rejected/`

필수 확인 항목:
- 공식 출처 URL 접근 가능 여부
- 핵심 정보 6개 (대상/지역/기간/비용/방법/주의사항)
- 마감일 유효 여부
- TODO 0개 달성 여부

---

### Phase 3: 큐레이션 (D-5)

**담당:** Curator
**커맨드:** `/curate-candidates`
**입력:** `data/verified/` (result: pass or caution)
**출력:** selected 항목 목록 + content_id 부여

점수 기준 (9개 항목, 각 0~5점, 총 45점):
- 36점 이상: 제작
- 28~35점: 보류
- 27점 이하 or 출처 신뢰도 2점 이하: 폐기

전시/행사 후보는 기본 점수와 별도로 timing 판단을 기록한다.

- `expired`: 제외
- `last_chance`: 종료까지 0~3일, 메인 카드뉴스 후보 기본 제외
- `ending_soon`: 종료까지 4~7일, 카드뉴스 후보 가능하나 "곧 종료" 표기 필수
- `ongoing_near`: 종료까지 8~21일, 카드뉴스 후보 적합
- `ongoing_stable`: 종료까지 22일 이상, 안정적 후보
- `upcoming_soon`: 시작 전이고 30일 이내 시작, "곧 열림"/"미리 저장" 후보 가능
- `upcoming_later`: 시작까지 31일 이상, 보류

주간 선별 목표: 4개 (월/수/금/일 슬롯)

---

### Phase 4: 브리프 (D-4)

**담당:** Editor
**커맨드:** `/plan-cardnews`
**스킬:** `cardnews-planning`
**입력:** `data/verified/{id}_{slug}.yml`
**출력:** `drafts/briefs/{id}_{slug}.md`

---

### Phase 5: 원고 + 캡션 (D-4 ~ D-3)

**담당:** Editor
**커맨드:** `/write-script`
**입력:** `drafts/briefs/{id}_{slug}.md`
**출력:**
- `drafts/scripts/{id}_{slug}_script.md`
- `drafts/captions/{id}_{slug}_caption.md`

완료 조건: TODO 0개, 금지 표현 0개, 8장 완성

---

### Phase 6: 디자인 프롬프트 (D-3)

**담당:** Design Director
**커맨드:** `/create-design-prompt`
**스킬:** `magazine-design`
**입력:** `drafts/scripts/{id}_{slug}_script.md`
**출력:** `drafts/design_prompts/{id}_{slug}_design_prompt.md`

→ Claude Design에 프롬프트 입력
→ 디자인 초안 생성

---

### Phase 7: 사람 검수 (D-2)

**담당:** Human
**커맨드:** `/review-before-upload`
**입력:** `reviews/human_review_queue/{id}_{slug}_review.md`
**출력:** `reviews/approved/` or `reviews/revision_needed/`

SLA: 24시간 이내
반려 시: scripted or designed 단계로 반환

---

### Phase 8: 업로드 (D-1 ~ D-0)

**담당:** Human
**출력:**
- `outputs/published/`
- `content/published_log.md` 기록

설정: 캐러셀, 위치 태그(서울), 예약 업로드(오전 7시 or 오후 7시)
업로드 직후: 첫 댓글 고정

---

### Phase 9: 성과 분석 (D+3)

**담당:** Growth Analyst
**출력:** `data/performance/{id}_{slug}_performance.yml`

측정 지표: 저장률 우선 > 공유율 > 댓글 > 팔로우 전환
성과 등급: A(저장률 10%↑) / B(5~10%) / C(5%↓)
다음 콘텐츠 방향: 5개 제안 → 실제 후보가 아닌 백로그 방향으로만 `content/ideas.md`에 추가

---

### Phase 10: 아카이브 (D+30)

**담당:** System
**출력:** `data/archive/{id}_{slug}_archive.yml`

아카이브 포함:
- 검증 데이터
- 원고
- 성과 데이터
- 변경 이력 (있는 경우)

---

## 비상 대응

| 상황 | 대응 |
|------|------|
| 후보 부족 | 에세이형으로 대체 (Phase 2~3 생략) |
| 검증 실패 과다 | 그 주 발행 수 축소 (4→2개) |
| 검수 반려 반복 | 에이전트 지시문 점검 |
| 종료 D-0~D-3 정보 | 메인 카드뉴스 제외, 스토리/긴급 알림 후보로 분리 |
| 종료 D-4~D-7 정보 | 카드뉴스 후보 가능, "곧 종료" 표기 필수 |
| 업로드 후 오류 | `ops/change_log_rules.md` 절차 |
