# /verify-candidate

목적: 후보 데이터의 공식 출처, 대상, 기간, 비용, 신청 가능 여부를 검증한다.

현재 구조 세팅 단계에서는 실행하지 않는다.

## 담당

- Verifier

## 입력

```
data/candidates/{category}_candidates.yml
```

참조:

- `schemas/verification.schema.yml`
- `ops/source_rules.md`
- `ops/quality_rules.md`
- `.claude/skills/fact-verification/SKILL.md`

## 출력

통과 또는 주의:

```
data/verified/{id}_{slug}.yml
```

폐기:

```
data/rejected/{date_or_slug}.yml
```

## 완료 조건

- 공식 출처 확인
- 확인일 기록
- 대상, 지역, 기간, 비용, 신청/이용 방법, 주의사항 확인
- `pass` 결과의 `todo_remaining`은 빈 배열

## 금지

- 공식 출처 없는 후보 통과 금지
- 마감이 지난 후보 통과 금지
- 검증 전 정보를 원고로 넘기기 금지
