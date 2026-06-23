# Human Review Rules

에이전트가 생성한 콘텐츠는 반드시 사람이 검수한다.
사람 검수를 건너뛴 콘텐츠는 발행하지 않는다.

---

## 검수가 필요한 단계

| 단계 | 트리거 | 검수 위치 |
|------|--------|---------|
| 원고 완성 후 | `scripted` 상태 전환 시 | `reviews/human_review_queue/` |
| 디자인 프롬프트 완성 후 | `designed` 상태 전환 시 | `reviews/human_review_queue/` |
| 업로드 직전 | `approved` → `published` 전환 전 | 최종 확인 |

---

## 검수 항목

### A. 정보 정확성 검수

- [ ] 모든 TODO 항목이 해소되었는가?
- [ ] 공식 출처 URL이 현재 접근 가능한가?
- [ ] 확인일이 48시간 이내인가? (정책/브랜드), 24시간 이내인가? (행사)
- [ ] 마감일이 아직 지나지 않았는가?
- [ ] 대상 조건이 카드뉴스에 명시되어 있는가?
- [ ] 비용 정보가 정확한가?

### B. 브랜드 정합성 검수

- [ ] 얇은지갑클럽 톤인가? (`brand/voice_and_tone.md` 기준)
- [ ] 금지 표현이 없는가? (`brand/forbidden_rules.md` 기준)
- [ ] 공공기관처럼 보이는 표현이 없는가?
- [ ] 과장 표현이 없는가?
- [ ] 광고성 콘텐츠인데 표시가 없는가?

### C. 구조 검수

- [ ] 8장 슬라이드 순서가 자연스러운가?
- [ ] 첫 장이 저장하고 싶게 구성되어 있는가?
- [ ] 마지막 장에 CTA + 출처 + 확인일이 있는가?
- [ ] 한 장에 하나의 메시지만 있는가?
- [ ] 각 슬라이드 본문이 4줄 이내인가?

### D. 캡션 검수

- [ ] 첫 줄에 핵심 정보 or 훅이 있는가?
- [ ] 해시태그가 15개 이내인가?
- [ ] 출처와 확인일이 포함되어 있는가?
- [ ] 저장/팔로우 CTA가 있는가?

---

## 검수 결과 처리

### 통과 (approved)
`reviews/approved/{id}_{slug}_approved.md` 로 이동.
status를 `approved`로 업데이트.

### 반려 (revision_needed)
`reviews/revision_needed/{id}_{slug}_revision.md` 로 이동.
반려 사유를 명확하게 기록.
수정이 필요한 파일(script or design_prompt)에 코멘트 추가.
담당 에이전트(Editor or Design Director)에게 재작업 요청.

---

## 검수 SLA

| 상황 | 기준 |
|------|------|
| 일반 콘텐츠 | 제출 후 24시간 이내 |
| 마감 임박 콘텐츠 | 제출 후 6시간 이내 |
| 큐 적체 시 | 48시간 이상 대기 항목 우선 처리 |

---

## 검수 제출 형식

`reviews/human_review_queue/{id}_{slug}_review.md` 에 다음을 포함:

```
# Review: {콘텐츠명}

status: in_review
제출일: YYYY.MM.DD
담당 에이전트: Editor / Design Director

## 파일 목록
- 원고: drafts/scripts/{id}_{slug}_script.md
- 디자인 프롬프트: drafts/design_prompts/{id}_{slug}_design_prompt.md
- 캡션: drafts/captions/{id}_{slug}_caption.md

## 검수 포인트 (에이전트 자체 체크)
- TODO 미해소 항목:
- 확인일:
- 출처:
- 특이사항:
```
