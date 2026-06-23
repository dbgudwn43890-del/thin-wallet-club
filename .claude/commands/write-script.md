# /write-script

목적: 승인된 브리프를 바탕으로 8장 카드뉴스 원고와 캡션을 작성한다.

현재 구조 세팅 단계에서는 실행하지 않는다.

## 담당

- Editor

## 입력

```
drafts/briefs/{id}_{slug}.md
```

참조:

- `schemas/script.schema.yml`
- `brand/voice_and_tone.md`
- `brand/forbidden_rules.md`

## 출력

```
drafts/scripts/{id}_{slug}_script.md
drafts/captions/{id}_{slug}_caption.md
```

## 완료 조건

- 슬라이드 정확히 8장
- 각 슬라이드 제목 15자 이내
- 각 슬라이드 본문 4줄 이내
- TODO 0개
- 출처와 확인일 표기
- 금지 표현 없음

## 금지

- 브리프 없이 원고 작성 금지
- 검증 데이터에 없는 정보 추가 금지
