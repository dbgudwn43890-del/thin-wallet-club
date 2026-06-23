# System Overview

얇은지갑클럽 콘텐츠 생산 시스템 전체 개요.

---

## 목적

서울/수도권 20대를 위한 정보형 인스타그램 매거진을 반복 가능한 방식으로 운영한다.
매주 4개의 카드뉴스를 안정적으로 생산하고, 정확성과 감각을 동시에 유지한다.

현재 프로젝트는 구조 세팅 단계다.
실제 후보 수집, 외부 URL 검증, 원고 작성, 캡션 작성, 디자인 프롬프트 작성은 아직 시작하지 않는다.

---

## 시스템 계층

```
[브랜드 계층]          brand/
  브랜드 기준, 톤, 디자인 시스템, 금지 규칙

[운영 계층]            ops/
  작동 원칙, 상태 규칙, 출처 규칙, 검수 규칙, 품질 기준

[에이전트 계층]        .claude/agents/
  7개 에이전트 — 역할 정의

[스킬 계층]            .claude/skills/
  3개 스킬 — 작업 절차 정의

[커맨드 계층]          .claude/commands/
  7개 커맨드 — 실행 트리거

[데이터 계층]          data/ + schemas/
  후보 데이터, 검증 데이터, 성과 데이터 + 스키마

[제작 계층]            drafts/ + reviews/
  브리프, 원고, 디자인 프롬프트, 캡션, 검수 큐

[출판 계층]            outputs/ + content/
  발행 완료 파일, 캘린더, 발행 로그
```

---

## 에이전트 팀

| 에이전트 | 역할 | 사용 스킬/커맨드 |
|---------|------|----------------|
| Trend Scout | 문화행사, 팝업, 트렌드 수집 | `/research-candidates` |
| Policy Scout | 청년정책, 지원금 수집 | `/research-candidates` |
| Verifier | 출처·정보 검증 | `fact-verification`, `/verify-candidate` |
| Curator | 점수화, 제작 결정 | `/curate-candidates` |
| Editor | 브리프, 원고, 캡션 | `cardnews-planning`, `/plan-cardnews`, `/write-script` |
| Design Director | 디자인 프롬프트 | `magazine-design`, `/create-design-prompt` |
| Growth Analyst | 성과 분석, 다음 방향 제안 | (발행 후 D+3) |

---

## 데이터 흐름

```
외부 출처 (sources/*.yml)
      ↓
  Scout 수집
      ↓
data/candidates/{category}_candidates.yml
      ↓
  Verifier 검증
      ↓
data/verified/{id}_{slug}.yml
      ↓
  Curator 선별
      ↓
  Editor 브리프
drafts/briefs/{id}_{slug}.md
      ↓
  Editor 원고
drafts/scripts/{id}_{slug}_script.md
drafts/captions/{id}_{slug}_caption.md
      ↓
  Design Director
drafts/design_prompts/{id}_{slug}_design_prompt.md
      ↓
  Human Review
reviews/human_review_queue/ → reviews/approved/
      ↓
  업로드
outputs/published/
content/published_log.md
      ↓
  Growth Analyst (D+3)
data/performance/{id}_{slug}_performance.yml
      ↓
  Archive (D+30)
data/archive/{id}_{slug}_archive.yml
```

---

## 폴더 역할 요약

| 폴더 | 역할 |
|------|------|
| `brand/` | 브랜드 기준 (변경 시 에이전트 전체 영향) |
| `ops/` | 운영 규칙 (상태, 네이밍, 검수, 품질, 출처, 변경) |
| `schemas/` | 데이터 구조 정의 (에이전트 출력 형식 기준) |
| `docs/` | 시스템 이해용 문서 |
| `sources/` | 출처 목록 yml (Scout가 참조) |
| `templates/` | 카테고리별 카드뉴스 포맷 |
| `content/` | 캘린더, 아이디어 백로그 인덱스, 발행 로그. 실제 후보 데이터 저장 금지 |
| `data/` | 후보/검증/성과/아카이브 데이터 |
| `drafts/` | 제작 중 파일 |
| `reviews/` | 사람 검수 큐 |
| `outputs/` | 발행 완료 파일 |
| `.claude/agents/` | 에이전트 역할 정의 |
| `.claude/skills/` | 에이전트 작업 절차 |
| `.claude/commands/` | 실행 트리거 |
| `workflows/` | 주간 파이프라인, 체크리스트 |

---

## 핵심 규칙 파일 위치

| 규칙 | 파일 |
|------|------|
| 운영 철학 | `ops/operating_principles.md` |
| 상태 관리 | `ops/status_rules.md` |
| 파일 네이밍 | `ops/naming_rules.md` |
| 출처 기준 | `ops/source_rules.md` |
| 검수 기준 | `ops/human_review_rules.md` |
| 품질 기준 | `ops/quality_rules.md` |
| 변경 처리 | `ops/change_log_rules.md` |
| 브랜드 기준 | `brand/voice_and_tone.md` |
| 디자인 기준 | `brand/design_system.md` |
| 금지 규칙 | `brand/forbidden_rules.md` |

---

## Structure Lock

현재 구조는 1차 운영 구조로 잠금 대상이다.
새 폴더, 새 에이전트, 새 스키마, 새 워크플로우 추가는 명확한 운영 필요가 있을 때만 한다.

콘텐츠 제작은 구조 검증 통과 후 시작한다.
Git 기준 커밋 전에는 아래 명령을 실행한다.

```bash
python scripts/validate_all.py
```

`validate_all.py`가 실패하면 기준 구조가 깨졌거나, 제작 전 비어 있어야 할 폴더에 실제 산출물이 들어간 상태다.
실패 원인을 먼저 해결한 뒤 커밋한다.
