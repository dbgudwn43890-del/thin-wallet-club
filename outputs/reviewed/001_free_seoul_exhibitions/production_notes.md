# Visual Draft Production Notes

content_id: `001_free_seoul_exhibitions`
status: `review_visual_draft`
created_at: `2026-06-24`

## 제작 기준

- 1080x1350 비율의 인스타그램 카드뉴스 리뷰용 시각 초안.
- 최종 업로드본이 아니라 사람 검토용 visual draft.
- 최신 script와 design prompt를 기준으로 제작.
- brief에 남아 있는 이전 후보 문구는 사용하지 않음.
- 카드 문구는 원고의 headline, body_copy, small_note 범위 안에서 사용.
- captions, 업로드 문구, published outputs는 생성하지 않음.

## 사용한 입력 파일

- `drafts/scripts/001_free_seoul_exhibitions_script.yml`
- `drafts/design_prompts/001_free_seoul_exhibitions_design_prompt.yml`
- `reviews/human_review_queue/001_free_seoul_exhibitions_pre_upload_review.md`
- `brand/design_system.md`
- `brand/voice_and_tone.md`
- `brand/forbidden_rules.md`

## 이미지/저작권 처리 방식

- 외부 이미지, 전시 포스터, 작품 이미지, 공식 키비주얼을 사용하지 않음.
- 모든 카드는 SVG 기반의 추상 도형, 선, 정보 블록, 타이포그래피로 구성.
- 각 전시의 분위기는 색면, 선, 프레임, 레이어 같은 일반적 시각 모티프로만 표현.
- 실제 디자인 제작 단계에서 사진이나 포스터를 추가하려면 별도 권리 확인이 필요.

## 카드별 제작 메모

1. `slide_01.svg`: 정보형 커버. `서울 무료 전시 5`와 숫자 5를 중심으로 구성.
2. `slide_02.svg`: 무료, 서울, 분위기 다양성을 번호형 리스트로 정리.
3. `slide_03.svg`: 유영국 전시는 작품 이미지 없이 단순 색면 블록으로 암시.
4. `slide_04.svg`: 권병준 전시는 소리와 공간감을 얇은 선의 간격으로 표현.
5. `slide_05.svg`: 서서울미술관은 미디어/스크린을 연상시키는 프레임 구조 사용.
6. `slide_06.svg`: 포란은 종료 임박 정보를 작은 라벨과 날짜 중심으로 표현.
7. `slide_07.svg`: 더 하이브리드는 공예와 혼성적 감각을 레이어 블록으로 표현.
8. `slide_08.svg`: 공식 출처 기준, 확인일, 방문 전 예약/운영시간 확인, 포란 일정 재확인 안내 포함.

## 아직 최종 업로드본이 아님

- 이 산출물은 리뷰용 SVG 초안이다.
- 실제 업로드용 PNG/JPG/PDF/ZIP 파일을 생성하지 않았다.
- 캡션과 업로드 문구도 생성하지 않았다.
- `reviews/approved/`로 이동하지 않았다.

## 사람이 확인해야 할 항목

- `《포란》`이 실제 발행 예정일 기준으로 여전히 사용 가능한지 확인.
- `《더 하이브리드》` 무료 근거를 전시 상세 + 관람안내 조합으로 표기해도 되는지 확인.
- 서울시립미술관 전시 사전 예약 링크가 필수인지 선택인지 확인.
- slide 08의 출처, 확인일, 방문 전 확인 문구가 모바일에서 충분히 읽히는지 확인.
- 브랜드명이 과하게 노출되지 않는지 확인.
- 공공기관 홍보물처럼 보이지 않는지 확인.
- 금지 문구와 과장된 추천 문구가 카드 문구로 들어가지 않았는지 확인.

## 다음 단계 권장사항

- 사람이 `preview.html`로 8장 흐름을 먼저 확인한다.
- 필요하면 SVG의 간격, 글자 크기, 하단 정보 가독성만 보정한다.
- 일정/무료 근거/예약 여부 확인 후 최종 리뷰 상태를 결정한다.
- 승인 전까지 published output을 만들지 않는다.
