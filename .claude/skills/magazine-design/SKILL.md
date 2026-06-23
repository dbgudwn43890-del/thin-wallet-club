# Magazine Design Skill

## Purpose

완성된 원고(`drafts/scripts/{id}_{slug}_script.md`)를 받아
Claude Design에 입력할 디자인 프롬프트(`drafts/design_prompts/{id}_{slug}_design_prompt.md`)를 생성한다.

얇은지갑클럽의 매거진형 디자인 시스템을 반영한다.
공공기관 카드뉴스처럼 보이지 않아야 한다.

현재 구조 세팅 단계에서는 실제 디자인 프롬프트를 생성하지 않는다.
이 문서는 정식 운영 시 반복 디자인 지시 절차를 정의한다.

---

## 입력 조건

- 입력 파일: `drafts/scripts/{id}_{slug}_script.md`
- 필수 상태: `status: scripted`
- 필수 조건: todo_count = 0, quality_check 통과
- 브랜드 참조: `brand/design_system.md`
- 스키마 참조: `schemas/design_prompt.schema.yml`

---

## 출력

- 출력 파일: `drafts/design_prompts/{id}_{slug}_design_prompt.md`
- 상태 업데이트: `status: designed`
- 검수 대기: `reviews/human_review_queue/{id}_{slug}_review.md` 생성

이 스킬은 원고 내용을 새로 쓰거나 사실 정보를 추가하지 않는다.

---

## 실행 절차

### Step 1. 원고 파일 검토
script 파일을 읽고 아래를 확인한다.
- 슬라이드가 정확히 8장인가?
- 각 슬라이드에 heading / body / footer가 있는가?
- TODO 항목이 0개인가?
- Slide 8에 CTA + 출처 + 브랜드명이 있는가?
- 커버 문구가 명확한 정보 중심인가?
- 금지 문구나 내부 기획어가 없는가?

조건 미충족 시 → Editor에게 반환.

### Step 2. 브랜드 컨텍스트 작성
Claude Design이 이해할 수 있도록 브랜드를 설명한다.

```
브랜드명: 얇은지갑클럽
설명: 서울/수도권 20대를 위한 감각 있는 생활 정보 매거진
포맷: 인스타그램 캐러셀 1080x1350px 8장
무드: editorial, magazine, minimal, warm
```

### Step 3. 무드 키워드 선택
원고 내용과 카테고리에 맞는 무드를 고른다.

기본 필수: editorial, magazine, minimal, warm
카테고리별 추가:
- 문화/전시: + urban, curated, soft contrast
- 정책/혜택: + clean, structured
- 브랜드: + premium, curated
- 에세이: + warm, editorial

### Step 4. 강조 요소 추출
원고에서 시각적으로 강조할 요소를 추출한다.
- 마감일 (날짜 형식 강조)
- 혜택 금액 (숫자 크게)
- 장소/기관명
- 대상 조건 (박스 or 굵게)

### Step 5. 슬라이드별 프롬프트 작성
원고의 각 슬라이드 텍스트를 그대로 복사하여 포함한다.
슬라이드별 시각 방향을 추가한다.
새로운 headline/body copy를 임의로 만들지 않는다.
감도는 문구를 더 꾸미는 방식이 아니라 여백, 타이포그래피, 정보 위계로 만든다.

```
Slide 1 (Cover/Hook):
  레이아웃: 잡지 표지. 상단 라벨, 중앙 대형 타이포, 하단 브랜드명
  무드: 명확하고 간결하게
  텍스트: [원고 그대로]

Slide 2~7 (정보 카드):
  레이아웃: 넉넉한 여백, 제목 → 본문 위계
  푸터: 확인일: YYYY.MM.DD | 출처: [출처명] (작게, 고정)
  텍스트: [원고 그대로]

Slide 8 (CTA):
  레이아웃: 여백 많게, CTA 중앙, 출처/브랜드명 하단
  텍스트: [원고 그대로]
```

### Step 6. 금지 요소 명시
Claude Design이 피해야 할 요소를 명확히 적는다.

```
금지:
- 공공기관 원색 (파랑/빨강 계열 강한 색상)
- 밈 스티커, 과한 이모지
- 복잡한 배경 패턴
- 무지개 그라데이션
- 한 슬라이드 내 5줄 초과 텍스트
- 폰트 3종 초과
- 금지 카피 새로 생성: 무료인데 꽤 괜찮아, 얇은지갑클럽 저장용 리스트, 감성 무료 전시, 요즘 핫한, 안 가면 손해, 무조건 가야 함, MZ 취향, 힙한, 모르면 손해
- 브랜드명/내부 운영어 과다 노출
```

### Step 7. 고정 표기 명시
모든 정보 카드(Slide 2~7) 하단에 반드시 포함할 요소:
```
확인일: YYYY.MM.DD
출처: [출처명]
```

Slide 8에 추가:
```
얇은지갑클럽
```

### Step 8. 검수 큐 제출
`reviews/human_review_queue/{id}_{slug}_review.md` 파일을 생성한다.

```markdown
# Review: {콘텐츠명}

status: in_review
제출일: YYYY-MM-DD
제출 에이전트: Design Director

## 파일 목록
- 원고: drafts/scripts/{id}_{slug}_script.md
- 디자인 프롬프트: drafts/design_prompts/{id}_{slug}_design_prompt.md
- 캡션: drafts/captions/{id}_{slug}_caption.md

## 에이전트 체크 결과
- TODO 미해소: 없음
- 확인일: YYYY-MM-DD
- 출처: [출처명]
- 특이사항: [있으면 기재]
```

---

## 품질 기준

프롬프트 제출 전 확인:
- [ ] 브랜드 컨텍스트 포함
- [ ] 무드 키워드 최소 3개
- [ ] 슬라이드 8장 텍스트 전체 포함
- [ ] 강조 요소 명시됨
- [ ] 금지 요소 명시됨
- [ ] 고정 표기 (출처/확인일/브랜드명) 위치 명시됨
- [ ] 검수 큐 파일 생성 완료
- [ ] 금지 카피를 새로 만들지 않음
- [ ] 커버가 명확한 정보 중심으로 유지됨
