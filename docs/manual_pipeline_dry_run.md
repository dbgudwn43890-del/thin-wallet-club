# Manual Pipeline Dry Run

이 문서는 실제 콘텐츠 제작 전에 candidate -> verification -> curation 흐름을 샘플 데이터로 점검하는 절차를 정의한다.

## Purpose

dry run의 목적은 실제 후보를 수집하지 않고도 운영 구조가 작동하는지 확인하는 것이다.

- candidate 데이터 형식이 읽기 쉬운지 확인한다.
- verification 결과가 pass, caution, fail로 분기되는지 확인한다.
- curation 단계에서 어떤 정보를 받아야 하는지 확인한다.
- 사람 검수 큐의 최소 형식을 확인한다.
- production 폴더를 오염시키지 않고 운영 흐름을 리허설한다.

## Difference From Real Content Production

dry run은 실제 콘텐츠 제작이 아니다.

- 실제 전시명, 정책명, 브랜드명을 사용하지 않는다.
- 실제 URL을 사용하지 않는다.
- 외부 검색을 하지 않는다.
- 카드뉴스 원고를 쓰지 않는다.
- 캡션을 쓰지 않는다.
- 디자인 프롬프트를 만들지 않는다.
- `data/`, `reviews/`, `drafts/`, `outputs/`에 실제 파일을 만들지 않는다.

샘플 데이터는 모두 `dry_run/` 아래에 둔다.

## Files Created During Dry Run

```text
dry_run/
├── README.md
├── sample_candidate.yml
├── sample_verification.yml
└── sample_review.md
```

각 파일의 역할:

- `dry_run/sample_candidate.yml`: candidate 단계 샘플
- `dry_run/sample_verification.yml`: verification 단계 샘플
- `dry_run/sample_review.md`: 사람 검수 대기 형식 샘플

## Candidate Stage

참조 파일:

```text
dry_run/sample_candidate.yml
```

확인할 것:

- 각 후보가 mock 데이터임을 명확히 표시하는가?
- `SAMPLE_FREE_CULTURE_EVENT`, `SAMPLE_YOUTH_BENEFIT`, `SAMPLE_BRAND_PROGRAM`처럼 실제 정보와 혼동되지 않는 이름을 쓰는가?
- `schemas/candidate.schema.yml`의 주요 필드를 포함하는가?
- status가 `idea` 또는 `pre_selected`로 남아 있는가?
- 실제 URL 대신 `https://example.com/sample-source`만 사용하는가?

## Verification Stage

참조 파일:

```text
dry_run/sample_verification.yml
```

확인할 것:

- 검증이 실제 외부 확인이 아니라 mock verification임을 명확히 표시하는가?
- pass, caution, fail 결과가 모두 하나씩 있는가?
- fail 항목에는 폐기 사유가 있는가?
- caution 항목에는 사람 검토가 필요한 이유가 있는가?
- pass 항목에는 `todo_remaining: []`가 유지되는가?

## Curation Stage

dry run에서는 실제 점수화를 확정하지 않는다.
Curator는 아래 질문에 답하는 방식으로만 흐름을 점검한다.

- pass 항목은 점수화 입력으로 충분한 정보를 가지고 있는가?
- caution 항목은 어떤 주의 문구나 사람 판단이 필요한가?
- fail 항목은 `rejected` 흐름으로 보내기에 충분한 사유가 있는가?
- `schemas/candidate.schema.yml`과 `schemas/verification.schema.yml` 사이에 누락되는 정보가 있는가?

dry run 단계에서는 `drafts/`로 넘어가지 않는다.

## Human Review Stage

참조 파일:

```text
dry_run/sample_review.md
```

확인할 것:

- review_id가 있는가?
- linked_candidate_id가 있는가?
- review_reason이 명확한가?
- checklist가 실제 검수 전에 필요한 질문을 담고 있는가?
- reviewer_decision_options가 승인, 수정 요청, 폐기 흐름을 표현하는가?
- notes가 production 폴더로 이동 금지 원칙을 명확히 하는가?

## Folder Rules

dry run 중 production 폴더는 계속 비어 있어야 한다.
아래 폴더에는 `.gitkeep`과 `.DS_Store` 외 파일을 두지 않는다.

- `data/candidates`
- `data/verified`
- `data/rejected`
- `data/archive`
- `data/performance`
- `reviews/human_review_queue`
- `reviews/approved`
- `reviews/revision_needed`
- `drafts/briefs`
- `drafts/scripts`
- `drafts/design_prompts`
- `drafts/captions`
- `outputs/reviewed`
- `outputs/published`

`scripts/validate_empty_production_dirs.py`는 이 원칙을 검증한다.

## Cleanup Or Archive Criteria

dry run 후 아래 기준 중 하나에 해당하면 샘플 파일을 수정하거나 삭제한다.

- 샘플이 실제 콘텐츠처럼 오해될 수 있다.
- 실제 기관명, 정책명, 행사명, 브랜드명이 들어갔다.
- 실제 URL이 들어갔다.
- production 폴더로 복사되었다.
- 스키마 변경 후 샘플 구조가 낡았다.

샘플은 production archive 대상이 아니다.
필요하면 `dry_run/` 안에서만 유지한다.

## Pre-Real-Content Checklist

실제 콘텐츠 파이프라인을 시작하기 전 아래를 확인한다.

- [ ] `python scripts/validate_all.py`가 통과한다.
- [ ] dry run 샘플이 실제 정보와 혼동되지 않는다.
- [ ] candidate -> verification -> curation 입력/출력 경계가 이해된다.
- [ ] caution과 fail 처리 기준이 충분히 명확하다.
- [ ] 사람 검수 대기 형식이 운영자에게 충분히 읽기 쉽다.
- [ ] production 폴더는 `.gitkeep` 외 비어 있다.
- [ ] 첫 실제 후보 수집을 시작해도 되는지 사람이 승인했다.
