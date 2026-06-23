# Naming Rules

파일명 규칙. 일관된 네이밍이 없으면 파이프라인이 탐색 불가 상태가 된다.

---

## Content ID

모든 콘텐츠는 3자리 제로패딩 번호를 가진다.

```
001, 002, 003 ... 099, 100, 101 ...
```

번호는 아이디어 단계에서 부여하지 않는다.
Curator가 `selected` 상태로 확정할 때 발행 예정 순서에 맞춰 부여한다.
`content/ideas.md`는 백로그 인덱스이므로 번호 부여의 원천으로 사용하지 않는다.

---

## Slug 규칙

- 영어 소문자만 사용
- 단어 구분: underscore (`_`)
- 날짜보다 콘텐츠 번호 우선
- 최대 40자 이내
- 카테고리를 반영할 것

```
좋은 예시: culture_example
나쁜 예: FreeSeoullExhibitions, 서울전시무료, 2026-06-23
```

---

## 파일 네이밍 규칙

| 단계 | 위치 | 형식 |
|------|------|------|
| 후보 데이터 (카테고리별) | `data/candidates/` | `{category}_candidates.yml` |
| 검증 완료 데이터 | `data/verified/` | `{id}_{slug}.yml` |
| 폐기 데이터 | `data/rejected/` | `{id_or_date}_{slug}.yml` |
| 브리프 | `drafts/briefs/` | `{id}_{slug}.md` |
| 원고 | `drafts/scripts/` | `{id}_{slug}_script.md` |
| 디자인 프롬프트 | `drafts/design_prompts/` | `{id}_{slug}_design_prompt.md` |
| 캡션 | `drafts/captions/` | `{id}_{slug}_caption.md` |
| 검수 대기 | `reviews/human_review_queue/` | `{id}_{slug}_review.md` |
| 검수 통과 | `reviews/approved/` | `{id}_{slug}_approved.md` |
| 수정 요청 | `reviews/revision_needed/` | `{id}_{slug}_revision.md` |
| 성과 데이터 | `data/performance/` | `{id}_{slug}_performance.yml` |
| 아카이브 | `data/archive/` | `{id}_{slug}_archive.yml` |

---

## 카테고리 슬러그

| 카테고리 | 슬러그 접두사 |
|---------|------------|
| 문화생활/전시/공연 | `culture_` / `exhibition_` |
| 청년정책/지원금 | `policy_` / `benefit_` |
| 브랜드 프로그램 | `brand_` |
| 대학생 혜택 | `student_` |
| 에세이/조언 | `essay_` |

---

## 예시

```
# 아래는 형식 예시이며 실제 후보가 아니다.

# ID 001: culture example (예시)

data/verified/001_culture_example.yml
drafts/briefs/001_culture_example.md
drafts/scripts/001_culture_example_script.md
drafts/design_prompts/001_culture_example_design_prompt.md
drafts/captions/001_culture_example_caption.md
reviews/human_review_queue/001_culture_example_review.md
reviews/approved/001_culture_example_approved.md
data/performance/001_culture_example_performance.yml
data/archive/001_culture_example_archive.yml

# ID 002: policy example (예시)

data/verified/002_policy_example.yml
drafts/briefs/002_policy_example.md
...
```
