# /curate-candidates

목적: 검증 완료 후보를 점수화하고 제작 여부를 결정한다.

현재 구조 세팅 단계에서는 실행하지 않는다.

## 담당

- Curator

## 입력

```
data/verified/{id}_{slug}.yml
```

## 평가 항목

각 항목은 0~5점이다.
기본 점수는 9개 항목 총 45점이며, 전시/행사 후보는 일정 판단 보조 필드로 `timing_fit`, `urgency_value`, `timing_label`, `timing_note`를 함께 기록한다.

- 타겟 적합도
- 지역 적합도
- 실질 절약 효과
- 감각성
- 시의성
- 저장 가능성
- 공유 가능성
- 출처 신뢰도
- 제작 난이도

## 전시/행사 timing 판단

종료일이 가깝다는 이유만으로 자동 제외하지 않는다.
`timing_fit`은 발행 가능성과 일정 안정성을, `urgency_value`는 저장/공유를 유도하는 긴급성을 평가한다.

| timing_label | 기준 | 판단 |
|--------------|------|------|
| `expired` | 이미 종료됨 | 제외 |
| `last_chance` | 종료까지 0~3일 | 메인 카드뉴스 후보 기본 제외. 스토리/긴급 알림/오늘의 추천 후보 가능 |
| `ending_soon` | 종료까지 4~7일 | 카드뉴스 후보 가능. "이번 주 안에 가야 함", "곧 종료" 표기 필수 |
| `ongoing_near` | 종료까지 8~21일 | 카드뉴스 후보 적합 |
| `ongoing_stable` | 종료까지 22일 이상 | 안정적 후보. 긴급성은 낮을 수 있음 |
| `upcoming_soon` | 시작 전이며 30일 이내 시작 | 카드뉴스 후보 가능. "곧 열림", "미리 저장", "오픈 예정" 표기 |
| `upcoming_later` | 시작까지 31일 이상 | 보류 후보 |

Curator 출력 권장 필드:

```yaml
timing_fit: 0~5
urgency_value: 0~5
timing_label: ongoing_stable | ending_soon | last_chance | upcoming_soon | upcoming_later | expired
timing_note: "일정 판단 근거"
```

## 결정 기준

- 32점 이상: 제작 가능
- 28~31점: 보류
- 27점 이하: 폐기 또는 재검토
- 출처 신뢰도 3점 미만: 점수와 무관하게 폐기

## 출력

제작 확정 시:

```
data/verified/{id}_{slug}.yml
status: selected
decision: produce
```

보류 또는 폐기 시 해당 사유를 데이터 파일에 기록한다.

전시/행사 후보는 제작/보류/폐기 사유에 일정 판단을 포함한다.

## 금지

- `selected` 전 `drafts/` 생성 금지
- 점수 없이 제작 확정 금지
