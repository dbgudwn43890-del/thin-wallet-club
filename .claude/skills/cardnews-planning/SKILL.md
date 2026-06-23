# Cardnews Planning Skill

## Purpose

검증된 콘텐츠 후보(`data/verified/{id}_{slug}.yml`)를 받아
8장 카드뉴스 브리프(`drafts/briefs/{id}_{slug}.md`)를 생성한다.

브리프는 원고 작성의 설계도다. 브리프가 정확할수록 원고 품질이 올라간다.

현재 구조 세팅 단계에서는 실제 브리프를 생성하지 않는다.
이 문서는 정식 운영 시 반복 기획 절차를 정의한다.

---

## 입력 조건

- 입력 파일: `data/verified/{id}_{slug}.yml`
- 필수 상태: `status: selected`
- 필수 조건: `result: pass or caution`, `todo_remaining: []`
- 스키마 참조: `schemas/brief.schema.yml`

---

## 출력

- 출력 파일: `drafts/briefs/{id}_{slug}.md`
- 상태 업데이트: `status: briefed`

이 스킬은 최종 원고, 캡션, 디자인 프롬프트를 작성하지 않는다.

---

## 실행 절차

### Step 1. 입력 파일 확인
verified 데이터 파일을 읽고 아래 항목이 모두 채워져 있는지 확인한다.
- source_name, source_url, verified_at
- target (대상 조건)
- period (기간/마감일)
- cost (비용)
- verified_info.how_to_apply
- verified_info.cautions
- todo_remaining이 빈 배열인지 확인

채워지지 않은 항목이 있으면 Verifier에게 반환한다.

### Step 2. 제목 후보 5개 생성
- 15자 이내
- 구체적 숫자(개수, 금액, 기간) 포함 권장
- 대상 명시 시 저장률 상승
- `brand/voice_and_tone.md` 기준 적용
- `brand/forbidden_rules.md` 금지 표현 배제

좋은 예시:
- "무료인데 괜찮은 문화생활 5"
- "청년 혜택, 조건부터 보기"
- "대학생 인증 혜택 7"

나쁜 예시:
- "대박 혜택 공개합니다"
- "청년 여러분께서는 꼭 확인하세요"

### Step 3. 핵심 약속 정의
이 카드뉴스를 다 보고 나서 독자가 얻는 것을 1문장으로.

예시: "독자가 저렴하게 즐길 수 있는 선택지와 이용 조건을 알게 된다."

### Step 4. 8장 슬라이드 구성 설계

| 장 | 역할 | 설계 질문 |
|----|------|---------|
| 1 | Hook | 첫 장만 보고 저장하고 싶어지는가? |
| 2 | Context | "이게 뭔데?"에 2줄로 답할 수 있는가? |
| 3 | Why now | 마감일/시의성이 드러나는가? |
| 4 | Target | 나도 해당되는지 즉시 알 수 있는가? |
| 5 | Benefit | 구체적 금액/가치가 있는가? |
| 6 | How-to | 신청/방문 방법이 단계별로 있는가? |
| 7 | Caution | 가장 많이 놓치는 조건이 있는가? |
| 8 | CTA | 저장 유도 + 출처 + 확인일 + 브랜드명 |

### Step 5. 팩트 목록 작성
confirmed와 todo를 명확히 분리한다.
confirmed 항목만 원고에서 확정 문장으로 쓸 수 있다.
todo 항목은 원고에서 반드시 `TODO:` 로 표시한다.

### Step 6. 리스크 정리
- 대상 조건이 복잡한가?
- 마감이 너무 임박한가?
- 비용이 조건에 따라 달라지는가?
- 오해 가능한 표현이 생길 수 있는가?

### Step 7. 캡션 방향 메모
- 첫 줄 훅 방향
- 강조할 조건
- 해시태그 방향

### Step 8. 디자인 방향 메모
- 무드 키워드
- 강조 요소 (마감일, 금액, 장소 등)
- 특이사항

---

## 품질 기준

브리프 제출 전 확인:
- [ ] 제목 후보 5개 있음
- [ ] 8장 구성 완전히 설계됨
- [ ] 핵심 약속 1문장 있음
- [ ] confirmed/todo 분리 완료
- [ ] 리스크 항목 검토됨
