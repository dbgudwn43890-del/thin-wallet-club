# /create-design-prompt

목적: 완성 원고를 Claude Design용 디자인 프롬프트로 전환한다.

현재 구조 세팅 단계에서는 실행하지 않는다.

## 담당

- Design Director

## 입력

```
drafts/scripts/{id}_{slug}_script.md
drafts/captions/{id}_{slug}_caption.md
```

참조:

- `.claude/skills/magazine-design/SKILL.md`
- `schemas/design_prompt.schema.yml`
- `brand/design_system.md`

## 출력

```
drafts/design_prompts/{id}_{slug}_design_prompt.md
reviews/human_review_queue/{id}_{slug}_review.md
```

## 완료 조건

- 1080x1350px, 8장 명시
- 브랜드 컨텍스트 포함
- 슬라이드별 텍스트 전체 포함
- 강조 요소와 금지 요소 명시
- 출처, 확인일, 브랜드명 위치 명시
- 정보 중심 커버 원칙 명시
- 금지 카피/금지 톤 명시

## 금지

- 원고와 다른 문구를 새로 만들기 금지
- 사람 검수 큐 없이 업로드 단계로 넘기기 금지
- 디자인 프롬프트에서 금지 문구 새로 생성 금지
- 브랜드명/내부 기획어 과다 노출 지시 금지
