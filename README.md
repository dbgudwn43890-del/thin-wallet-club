# 얇은지갑클럽 운영 시스템

서울/수도권 20대를 위한 감각 있는 생활 정보 매거진, 얇은지갑클럽의 콘텐츠 생산 시스템.

현재 프로젝트 상태: **구조 세팅 단계**

지금은 첫 콘텐츠 제작을 시작하지 않는다. 이 저장소는 장기 운영 가능한 콘텐츠 생산 시스템의 역할, 규칙, 스키마, 검수 절차를 정리하는 단계다.

---

## 핵심 원칙

- 에이전트는 역할을 정의한다.
- 스킬은 반복 작업 절차를 정의한다.
- 스키마는 출력 형식을 정의한다.
- `ops/`는 운영 규칙을 정의한다.
- `docs/`는 시스템 이해와 인수인계를 돕는다.
- `data/`는 실제 후보, 검증, 성과 데이터를 저장한다.
- `reviews/`는 사람 검수 대기열과 승인/수정 상태를 관리한다.
- `drafts/`는 제작이 확정된 콘텐츠만 들어간다.
- `outputs/`는 완성본만 들어간다.

---

## 폴더 역할

| 폴더 | 역할 |
|------|------|
| `.claude/agents/` | Trend Scout, Policy Scout, Verifier 등 에이전트 역할 정의 |
| `.claude/skills/` | fact-verification, cardnews-planning, magazine-design 반복 절차 |
| `.claude/commands/` | 리서치, 검증, 큐레이션, 제작, 검수 실행 명령 문서 |
| `brand/` | 브랜드 전략, 톤, 디자인 시스템, 금지 표현 |
| `ops/` | 운영 원칙, 상태, 네이밍, 출처, 검수, 품질, 변경 기록 규칙 |
| `schemas/` | 후보, 검증, 브리프, 원고, 디자인 프롬프트, 성과 데이터 형식 |
| `docs/` | 시스템 개요, 에이전트 인계, 콘텐츠 라이프사이클 |
| `sources/` | Scout가 참조할 출처 목록 |
| `templates/` | 카테고리별 카드뉴스 구조 템플릿 |
| `content/` | 아이디어 백로그 인덱스, 캘린더, 발행 로그 |
| `data/candidates/` | 실제 후보 데이터 |
| `data/verified/` | 검증 통과 데이터 |
| `data/rejected/` | 폐기 후보와 사유 |
| `data/performance/` | 발행 후 성과 데이터 |
| `data/archive/` | 종료된 콘텐츠 묶음 기록 |
| `drafts/` | 제작 확정 후 브리프, 원고, 캡션, 디자인 프롬프트 |
| `reviews/` | 사람 검수 큐, 승인, 수정 요청 기록 |
| `outputs/` | 발행 가능하거나 발행 완료된 최종 산출물 |
| `workflows/` | 주간 운영 흐름과 체크리스트 |

---

## 콘텐츠 제작 전 필수 선행 조건

콘텐츠 제작은 아래 조건을 모두 만족한 뒤에만 시작한다.

1. 후보 데이터가 `schemas/candidate.schema.yml` 형식으로 `data/candidates/`에 저장되어 있다.
2. Verifier가 공식 출처를 확인하고 `schemas/verification.schema.yml` 형식으로 `data/verified/`에 저장했다.
3. Curator가 9개 항목 점수화를 완료했다.
4. 출처 신뢰도 점수가 3점 이상이다.
5. 제작 기준 점수를 충족하고 `status: selected`로 확정됐다.
6. 사람 검수 흐름과 파일 저장 위치가 정해져 있다.

이 조건 전에는 `drafts/`에 브리프, 원고, 캡션, 디자인 프롬프트를 만들지 않는다.

---

## 현재 하지 않는 일

- 첫 콘텐츠 제작
- 무료 전시 후보 수집
- 실제 정책/행사/브랜드 정보 조사
- 외부 URL 검증
- 카드뉴스 원고 작성
- 캡션 작성
- 디자인 프롬프트 작성
- `drafts/` 안에 실제 제작물 생성
- `data/` 안에 실제 후보 데이터 생성

---

## 운영 문서

| 문서 | 설명 |
|------|------|
| `docs/system_overview.md` | 전체 시스템 구조 |
| `docs/agent_handoff_protocol.md` | 에이전트 간 입력/출력/저장 위치 |
| `docs/content_lifecycle.md` | 아이디어부터 아카이브까지 흐름 |
| `ops/operating_principles.md` | 운영 판단 기준 |
| `ops/status_rules.md` | 상태값과 전환 조건 |
| `ops/naming_rules.md` | 파일명과 ID 규칙 |
| `ops/source_rules.md` | 공식 출처 기준 |
| `ops/human_review_rules.md` | 사람 검수 기준 |
| `ops/quality_rules.md` | 단계별 품질 기준 |
| `ops/change_log_rules.md` | 발행 후 수정/삭제 기록 |

---

## Structure Validation

구조 검증은 Git 기준 커밋 전 현재 폴더 구조가 1차 운영 구조를 유지하는지 확인하기 위한 안전장치다.
콘텐츠 제작 전에는 통합 검증이 통과해야 한다.

실행 명령:

```bash
pip install -r requirements.txt
python scripts/validate_structure.py
python scripts/validate_empty_production_dirs.py
python scripts/validate_schemas.py
python scripts/validate_all.py
```

전체 검증만 실행할 때:

```bash
python scripts/validate_all.py
```

검증 기준:

- `validate_structure.py`: 필수 폴더와 문서가 있는지 확인한다.
- `validate_empty_production_dirs.py`: 제작 전 단계에서 `data/`, `reviews/`, `drafts/`, `outputs/`에 실제 콘텐츠 파일이 없는지 확인한다.
- `validate_schemas.py`: `schemas/`의 YAML 파일이 정상 파싱되는지 확인한다. 이 검증에는 PyYAML이 필요하다.
- `validate_all.py`: 위 세 검증을 순서대로 실행한다.

지금은 아직 콘텐츠 제작 전 단계다.
실제 콘텐츠 제작을 시작하면 `validate_empty_production_dirs.py`의 기준은 운영 단계에 맞게 변경해야 할 수 있다.

---

## 첫 콘텐츠 제작은 아직 시작하지 않는다

현재 저장소의 목적은 콘텐츠를 빠르게 만드는 것이 아니라, 반복 가능한 생산 시스템을 안정적으로 세우는 것이다.
첫 콘텐츠는 구조, 규칙, 스키마, 검수 절차가 모두 합의된 뒤 별도 작업으로 시작한다.
