# Agent Handoff Protocol

에이전트 간 작업 인계 절차.
각 에이전트는 "무엇을 받아서, 무엇을 만들고, 어디에 저장하고, 누구에게 넘기는지"를 정확히 안다.

---

## 핵심 원칙

1. 에이전트는 본인 담당 파일만 쓴다.
2. 다음 에이전트가 필요한 파일이 없으면 이전 단계로 에스컬레이션한다.
3. TODO가 남아있는 파일은 다음 단계로 넘기지 않는다.
4. 상태 업데이트는 해당 데이터 파일에 반영한다.
5. `content/ideas.md`는 백로그 인덱스이며 실제 후보 데이터나 검증 상태의 원천으로 쓰지 않는다.

---

## 1. Trend Scout / Policy Scout → Verifier

**Scout 출력:**
```
data/candidates/{category}_candidates.yml
  - 후보 항목 추가
  - status: idea
  - source.verified_at: TODO
```

**Verifier 입력 조건:**
- `data/candidates/` 에 신규 항목 존재
- status가 `idea` or `pre_selected`

**에스컬레이션:**
- 출처 URL이 아예 없는 경우 → Scout에게 반환

---

## 2. Verifier → Curator

**Verifier 출력:**
```
data/verified/{id}_{slug}.yml     (pass/caution)
data/rejected/{slug}.yml          (fail)
  - result: pass / caution / fail
  - verified_at: YYYY-MM-DD
  - verified_info: 핵심 정보 6개
  - usable_sentences: []
  - todo_remaining: [] (pass는 반드시 0개)
```

**Curator 입력 조건:**
- `data/verified/` 에 result가 `pass` or `caution`인 항목
- todo_remaining이 0개

**에스컬레이션:**
- 검증 중 마감 지남 → 즉시 rejected 처리
- 출처 접근 불가 → Scout에게 대체 출처 요청

---

## 3. Curator → Editor

**Curator 출력:**
```
data/verified/{id}_{slug}.yml 업데이트:
  - status: selected
  - content_id: 부여 (001, 002 ...)
  - scores.total: /45
  - decision: produce / hold / reject
```

**Editor 입력 조건:**
- `data/verified/` 에 status가 `selected`인 항목
- scores.source_trust가 3점 이상
- result가 `pass` or `caution`

**에스컬레이션:**
- scores.total이 28점 미만 → hold 처리, 다음 주 재검토

---

## 4. Editor (브리프) → Editor (원고)

**브리프 출력:**
```
drafts/briefs/{id}_{slug}.md
  - 8장 슬라이드 구성 설계 완료
  - 제목 후보 5개
  - 팩트 목록 (확인된 것 / TODO)
  - status: briefed
```

**원고 입력 조건:**
- 브리프의 TODO 항목이 0개
- 슬라이드 구성 8장 완전 설계됨

**에스컬레이션:**
- 브리프에 TODO가 남은 경우 → Verifier에게 추가 확인 요청

---

## 5. Editor (원고) → Design Director

**원고 출력:**
```
drafts/scripts/{id}_{slug}_script.md
drafts/captions/{id}_{slug}_caption.md
  - 8장 슬라이드 원고 완성
  - TODO 0개
  - 금지 표현 0개
  - 출처/확인일 표기 완료
  - status: scripted
```

**Design Director 입력 조건:**
- script 파일의 todo_count가 0
- quality_check 체크리스트 통과

**에스컬레이션:**
- 원고에서 검증 불가 정보 발견 시 → Verifier에게 재검증 요청

---

## 6. Design Director → Human Review

**Design Director 출력:**
```
drafts/design_prompts/{id}_{slug}_design_prompt.md
reviews/human_review_queue/{id}_{slug}_review.md
  - 8장 슬라이드 텍스트 완전 포함
  - 강조/금지 요소 명시
  - status: designed → in_review
```

**Human Review 입력 조건:**
- `reviews/human_review_queue/` 에 review 파일 존재
- design_prompt 파일 존재

---

## 7. Human Review → 업로드 or 반려

**통과 (approved):**
```
reviews/approved/{id}_{slug}_approved.md 생성
  - 통과 일자 기록
  - status: approved
```
→ 업로드 진행 → `outputs/published/` + `content/published_log.md`

**반려 (revision_needed):**
```
reviews/revision_needed/{id}_{slug}_revision.md 생성
  - 반려 사유 상세 기록
  - 수정 요청 파일 명시
  - status: revision_needed
```
→ Editor or Design Director에게 반환 → scripted or designed 단계로 복귀

---

## 8. 업로드 → Growth Analyst

**업로드 후:**
```
content/published_log.md 업데이트
outputs/published/ 파일 저장
  - status: published
```

**Growth Analyst (D+3):**
```
data/performance/{id}_{slug}_performance.yml 생성
  - metrics_d3 완성
  - analysis 작성
  - next_recommendations 5개
  - performance_grade: A/B/C
```

**Archive (D+30):**
```
data/archive/{id}_{slug}_archive.yml 생성
  - status: archived
```
