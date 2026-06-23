# Status Rules

모든 콘텐츠 후보는 아래 상태값 중 하나를 가진다.
상태값은 실제 후보 데이터 파일(`data/candidates/*.yml`, `data/verified/*.yml`, `data/rejected/*.yml`)에 사용한다.
`content/ideas.md`는 실제 후보 데이터가 아니라 백로그 인덱스이므로 후보 상태의 원천으로 쓰지 않는다.

---

## 상태 정의

| status | 단계 | 담당 | 의미 |
|--------|------|------|------|
| `idea` | 0 | Trend/Policy Scout | 수집된 아이디어. 검증 전. |
| `pre_selected` | 1 | Curator | 브리프 만들 가치가 있다고 1차 판단됨. |
| `verifying` | 2 | Verifier | 공식 출처·일정·비용·조건 확인 중. |
| `verified` | 3 | Verifier | 핵심 정보 검증 완료. 제작 가능 상태. |
| `rejected` | — | Verifier / Curator | 폐기. 이유 반드시 기록. 되돌릴 수 없음. |
| `selected` | 4 | Curator | 이번 주 제작 대상으로 확정. |
| `briefed` | 5 | Editor | 브리프 작성 완료. |
| `scripted` | 6 | Editor | 8장 원고 작성 완료. |
| `designed` | 7 | Design Director | 디자인 프롬프트 완료. |
| `in_review` | 8 | Human | 사람 검수 중. |
| `approved` | 9 | Human | 검수 통과. 업로드 가능. |
| `revision_needed` | 8b | Human | 수정 요청. Editor/Design Director에게 반환. |
| `published` | 10 | Human | 인스타그램 발행 완료. |
| `archived` | — | System | 발행 후 30일 경과. 성과 기록 포함. |

---

## 파이프라인 흐름

```
idea
  └─→ pre_selected
        └─→ verifying
              ├─→ verified
              │     └─→ selected
              │           └─→ briefed
              │                 └─→ scripted
              │                       └─→ designed
              │                             └─→ in_review
              │                                   ├─→ approved → published → archived
              │                                   └─→ revision_needed → (scripted or designed)
              └─→ rejected
```

---

## 전환 규칙

| 전환 | 조건 |
|------|------|
| `idea` → `pre_selected` | Curator가 큐레이션 점수 계산 후 28점 이상 |
| `pre_selected` → `verifying` | Verifier에게 전달 |
| `verifying` → `verified` | 공식 출처 URL 확인 + 핵심 정보 6개 이상 확보 |
| `verifying` → `rejected` | 공식 출처 없음 / 마감 지남 / 조건 불명확 |
| `verified` → `selected` | Curator가 이번 주 제작 대상으로 확정 |
| `selected` → `briefed` | `drafts/briefs/` 파일 생성 완료 |
| `briefed` → `scripted` | `drafts/scripts/` 파일 생성 완료 |
| `scripted` → `designed` | `drafts/design_prompts/` 파일 생성 완료 |
| `designed` → `in_review` | `reviews/human_review_queue/` 에 제출 |
| `in_review` → `approved` | 사람 검수 통과 (`ops/human_review_rules.md` 기준) |
| `in_review` → `revision_needed` | 사람 검수 반려 |
| `approved` → `published` | 실제 인스타그램 업로드 완료 |
| `published` → `archived` | 발행 후 30일 경과 + 성과 데이터 기록 |

---

## 파일 위치

| status | 파일 위치 |
|--------|---------|
| idea ~ pre_selected | `data/candidates/{category}_candidates.yml` |
| verifying | `data/candidates/{category}_candidates.yml` |
| verified | `data/verified/{id}_{slug}.yml` |
| rejected | `data/rejected/{slug}.yml` |
| selected ~ designed | `drafts/` |
| in_review | `reviews/human_review_queue/` |
| approved | `reviews/approved/` |
| published | `outputs/published/` + `content/published_log.md` |
| archived | `data/archive/` |
