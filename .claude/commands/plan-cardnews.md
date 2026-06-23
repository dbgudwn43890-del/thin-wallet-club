# /plan-cardnews

목적: 제작 확정 후보를 8장 카드뉴스 브리프로 설계한다.

현재 구조 세팅 단계에서는 실행하지 않는다.

## 담당

- Editor

## 입력

```
data/verified/{id}_{slug}.yml
status: selected
```

참조:

- `.claude/skills/cardnews-planning/SKILL.md`
- `schemas/brief.schema.yml`
- `brand/voice_and_tone.md`
- `brand/forbidden_rules.md`

## 출력

```
drafts/briefs/{id}_{slug}.md
```

## 완료 조건

- 제목 후보 5개
- 8장 슬라이드 구성
- 핵심 약속 1문장
- 확인된 팩트와 TODO 분리
- 리스크와 캡션/디자인 방향 메모

## 금지

- 검증되지 않은 정보 확정 표현 금지
- TODO가 있는 브리프를 원고 단계로 전달 금지
