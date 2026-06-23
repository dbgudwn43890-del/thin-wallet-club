# /review-before-upload

목적: 업로드 전 사람이 원고, 캡션, 디자인 프롬프트를 최종 검수한다.

현재 구조 세팅 단계에서는 실행하지 않는다.

## 담당

- Human reviewer

## 입력

```
reviews/human_review_queue/{id}_{slug}_review.md
drafts/scripts/{id}_{slug}_script.md
drafts/captions/{id}_{slug}_caption.md
drafts/design_prompts/{id}_{slug}_design_prompt.md
```

참조:

- `ops/human_review_rules.md`
- `ops/quality_rules.md`
- `ops/upload_rules.md`

## 출력

통과:

```
reviews/approved/{id}_{slug}_approved.md
```

수정 필요:

```
reviews/revision_needed/{id}_{slug}_revision.md
```

## 검수 기준

- 정보 정확성
- 브랜드 톤
- 금지 표현
- 8장 구조
- 출처와 확인일
- 캡션과 CTA

## 금지

- 사람 검수 없이 업로드 금지
- TODO가 남은 콘텐츠 승인 금지
- 출처 또는 확인일이 빠진 콘텐츠 승인 금지
