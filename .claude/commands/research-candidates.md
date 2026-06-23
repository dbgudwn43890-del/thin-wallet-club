# /research-candidates

목적: Scout가 실제 후보 데이터를 수집할 때 사용하는 명령 문서.

현재 구조 세팅 단계에서는 실행하지 않는다.

## 담당

- Trend Scout
- Policy Scout

## 입력

- `content/ideas.md`의 백로그 방향
- `sources/*.yml`
- `ops/source_rules.md`
- `schemas/candidate.schema.yml`

## 출력

```
data/candidates/{category}_candidates.yml
```

## 절차

1. 백로그 방향을 실제 후보로 전환할 필요가 있는지 확인한다.
2. 공식 출처 후보를 찾는다.
3. 후보별로 `schemas/candidate.schema.yml` 필드를 채운다.
4. 검증 전 정보는 확정 문장으로 쓰지 않는다.
5. `status: idea` 또는 `status: pre_selected`로 저장한다.

## 금지

- `drafts/`에 파일 생성 금지
- 원고, 캡션, 디자인 프롬프트 작성 금지
- 공식 출처가 없는 후보 저장 금지
