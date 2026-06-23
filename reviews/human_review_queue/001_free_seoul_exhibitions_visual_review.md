# Visual Draft Review: 001_free_seoul_exhibitions

content_id: 001_free_seoul_exhibitions
review_status: conditional
reviewed_at: 2026-06-24
review_type: visual_draft_final_review

## Reviewed Files

- `outputs/reviewed/001_free_seoul_exhibitions/cards/slide_01.svg`
- `outputs/reviewed/001_free_seoul_exhibitions/cards/slide_02.svg`
- `outputs/reviewed/001_free_seoul_exhibitions/cards/slide_03.svg`
- `outputs/reviewed/001_free_seoul_exhibitions/cards/slide_04.svg`
- `outputs/reviewed/001_free_seoul_exhibitions/cards/slide_05.svg`
- `outputs/reviewed/001_free_seoul_exhibitions/cards/slide_06.svg`
- `outputs/reviewed/001_free_seoul_exhibitions/cards/slide_07.svg`
- `outputs/reviewed/001_free_seoul_exhibitions/cards/slide_08.svg`
- `outputs/reviewed/001_free_seoul_exhibitions/preview.html`
- `outputs/reviewed/001_free_seoul_exhibitions/production_notes.md`
- `drafts/scripts/001_free_seoul_exhibitions_script.yml`
- `drafts/design_prompts/001_free_seoul_exhibitions_design_prompt.yml`
- `reviews/human_review_queue/001_free_seoul_exhibitions_pre_upload_review.md`
- `brand/voice_and_tone.md`
- `brand/forbidden_rules.md`
- `brand/design_system.md`
- `workflows/cardnews_checklist.md`
- `workflows/factcheck_checklist.md`

## Visual Check Result

status: conditional_pass

Summary:

- SVG 8개 모두 `width="1080"`, `height="1350"`, `viewBox="0 0 1080 1350"` 기준을 따른다.
- 전체 흐름은 커버 → 리스트 맥락 → 전시 5개 → CTA/출처로 자연스럽다.
- 타이포그래피, 여백, 그리드, 추상 도형 중심으로 구성되어 디자인 프롬프트 방향과 맞는다.
- 카드별 headline/body/note 위계가 분리되어 있고, 본문 양도 모바일에서 과밀해 보일 가능성이 낮다.
- 공공기관 홍보물의 원색/안내문 박스/과한 아이콘 느낌은 보이지 않는다.
- slide_08은 출처, 확인일, 방문 전 확인 안내, 포란 일정 재확인 메모를 포함한다.

Notes:

- 실제 모바일 화면에서 slide_08 하단 푸터와 안내 박스 텍스트가 충분히 읽히는지 사람 확인이 필요하다.
- slide_06은 `곧 종료` 라벨과 headline이 함께 있어 긴급성은 잘 드러나지만, 실제 디자인 리뷰에서 반복감이 과한지 확인하면 좋다.

## Copy Check Result

status: pass

Summary:

- 커버 headline은 `서울 무료 전시 5`로 유지되어 있다.
- SVG 카드 문구는 최신 script 기준과 일치한다. 일부 headline은 시각적 줄바꿈을 위해 나뉘었지만 의미와 문구는 유지된다.
- 폐기된 문구와 금지 문구가 독자-facing 영역에 남아 있지 않다.
- `무료인데 꽤 괜찮아`, `얇은지갑클럽 저장용 리스트`, `감성 무료 전시`, `요즘 핫한`, `안 가면 손해`, `무조건 가야 함`, `MZ 취향`, `힙한`, `모르면 손해`는 outputs 안에서 발견되지 않았다.
- 브랜드명은 slide_08 하단에만 작게 들어가 과다 노출로 보이지 않는다.

## Fact Check Result

status: conditional_pass

Summary:

- selected 5개 전시가 정확히 반영되어 있다.
- slide_03 유영국, slide_04 권병준, slide_05 서서울 미디어, slide_06 포란, slide_07 더 하이브리드 순서가 script와 일치한다.
- 기간, 무료 여부, 지역 정보는 script의 small_note와 일치한다.
- slide_03~slide_07에 출처가 포함되어 있고, slide_08에 공식 출처 기준, 확인일, 방문 전 예약/운영시간 확인이 포함되어 있다.
- `《포란》`은 `곧 종료`, `7월 5일까지`, `발행일 기준 일정 재확인`으로 리스크가 충분히 드러난다.
- `《더 하이브리드》` 무료 근거 리스크는 production notes와 기존 review notes에 남아 있다.
- 예약 필수 여부는 단정하지 않고 `방문 전 예약/운영시간 확인`으로 처리되어 있다.

Notes:

- `《포란》`은 실제 caption 작성 또는 업로드 전 발행일 기준으로 다시 판단해야 한다.
- `《더 하이브리드》`는 무료 근거를 최종 승인 전에 사람이 다시 확인해야 한다.

## Rights Check Result

status: pass

Summary:

- SVG 카드 안에 외부 이미지, 전시 포스터, 작품 이미지, 공식 키비주얼을 사용하지 않았다.
- `<image>` 태그나 외부 이미지 URL을 사용하지 않았다.
- 그래픽은 추상 도형, 선, 프레임, 색면, 텍스트 중심이다.
- 특정 작품을 직접 재현한다고 볼 만한 구체 이미지가 없다.
- production notes에도 외부 이미지 미사용과 권리 확인 원칙이 명시되어 있다.

## Blocking Issues

None.

## Non-Blocking Issues

- slide_08 하단의 출처/브랜드/방문 전 확인 문구는 실제 모바일 크기에서 가독성 확인이 필요하다.
- slide_06의 `곧 종료` 라벨과 headline 반복이 실제 카드에서 과하게 느껴지는지 사람 확인이 필요하다.
- `《포란》` 일정 유효성은 caption 작성 전 다시 확인해야 한다.
- `《더 하이브리드》` 무료 근거는 최종 업로드 전 다시 확인해야 한다.
- caption과 업로드 문구는 아직 작성되지 않았으므로 별도 단계에서 검수해야 한다.

## Slide By Slide Notes

### Slide 01

- 문구: script 기준과 일치. 커버 headline `서울 무료 전시 5` 유지.
- 시각: 큰 타이포그래피와 숫자 중심이라 정보형 커버로 적합.
- 확인 필요: 실제 피드 썸네일에서 `서울/무료/전시/5` 위계가 충분히 읽히는지 확인.

### Slide 02

- 문구: script 기준과 일치.
- 시각: 번호형 리스트와 지역 축약 표기로 리스트 맥락이 보인다.
- 확인 필요: `why save` 라벨이 독자-facing 문구로 과하게 도드라지지 않는지 확인.

### Slide 03

- 문구: script 기준과 일치.
- 시각: 색면 블록이 작품 복제가 아니라 추상 모티프로 작동한다.
- 확인 필요: 출처 텍스트 크기가 모바일에서 읽히는지 확인.

### Slide 04

- 문구: headline이 `소리로` / `보는 전시`로 줄바꿈되었지만 script와 의미가 일치한다.
- 시각: 얇은 선 모티프가 소리/공간감을 과하지 않게 암시한다.
- 확인 필요: 본문과 선 모티프가 겹치지 않는지 실제 미리보기에서 확인.

### Slide 05

- 문구: script 기준과 일치.
- 시각: 프레임 구조가 미디어/새 공간 느낌을 준다.
- 확인 필요: 긴 headline 줄바꿈이 모바일에서 안정적인지 확인.

### Slide 06

- 문구: script 기준과 일치하며 종료 임박 리스크가 드러난다.
- 시각: `곧 종료` 라벨과 날짜 강조가 적절하다.
- 확인 필요: 발행일 기준 일정 유효성 재확인. 라벨/headline 반복감 확인.

### Slide 07

- 문구: script 기준과 일치.
- 시각: 레이어 블록이 공예/혼성 감각을 추상적으로 표현한다.
- 확인 필요: 무료 근거 분리 리스크를 최종 리뷰에서 다시 확인.

### Slide 08

- 문구: script 기준 CTA와 리뷰 요구사항을 반영한다.
- 시각: CTA, 공식 출처 기준, 확인일, 포란 일정 재확인, 방문 전 확인 안내가 들어 있다.
- 확인 필요: 하단 푸터와 안내 박스 텍스트가 실제 모바일 크기에서 충분히 읽히는지 확인.

## Human Review Required

- `preview.html`을 실제 화면에서 열어 8장 흐름과 모바일 가독성을 확인.
- slide_08의 출처/확인일/방문 전 확인 문구가 묻히지 않는지 확인.
- `《포란》`이 caption 작성 시점에도 사용 가능한지 발행 예정일 기준으로 재확인.
- `《더 하이브리드》` 무료 근거를 전시 상세 + 관람안내 조합으로 표기해도 되는지 최종 확인.
- slide_06의 `곧 종료` 반복 표현이 과하지 않은지 확인.
- 외부 이미지나 전시 포스터를 추가하지 않는 제작 방침을 유지할지 확인.

## Recommended Next Action

Proceed to caption drafting only after a human reviewer visually checks `preview.html`.

Recommended status:

- `conditional`: 카드 자체의 차단 이슈는 없으나, 실제 모바일 가독성, `《포란》` 일정, `《더 하이브리드》` 무료 근거 확인이 남아 있다.

Do not publish yet.
