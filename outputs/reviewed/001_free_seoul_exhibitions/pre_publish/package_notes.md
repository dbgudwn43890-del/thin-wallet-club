# Pre-Publish Package Notes

content_id: `001_free_seoul_exhibitions`
status: `pre_publish_review_package`
created_at: `2026-06-24`

## Package Purpose

이 패키지는 실제 업로드 전 사람이 마지막으로 확인할 수 있도록 만든 pre-publish 검토용 묶음입니다.

업로드 완료 처리, published 이동, published log 기록, approved 리뷰 이동을 의미하지 않습니다.

## Included Files

- `images/slide_01.png`
- `images/slide_02.png`
- `images/slide_03.png`
- `images/slide_04.png`
- `images/slide_05.png`
- `images/slide_06.png`
- `images/slide_07.png`
- `images/slide_08.png`
- `final_caption_candidate.md`
- `upload_checklist.md`
- `package_notes.md`

## Source Files

- `outputs/reviewed/001_free_seoul_exhibitions/cards/slide_01.svg` ~ `slide_08.svg`
- `outputs/reviewed/001_free_seoul_exhibitions/preview.html`
- `outputs/reviewed/001_free_seoul_exhibitions/production_notes.md`
- `drafts/captions/001_free_seoul_exhibitions_caption.md`
- `reviews/human_review_queue/001_free_seoul_exhibitions_final_approval_review.md`
- `ops/upload_rules.md`
- `workflows/cardnews_checklist.md`
- `workflows/factcheck_checklist.md`

## Conversion Method

- SVG 원본 8장을 Chrome headless screenshot 방식으로 1080x1350 PNG로 변환했습니다.
- 원본 SVG는 수정하지 않았습니다.
- 외부 이미지, 작품 이미지, 전시 포스터, 공식 키비주얼을 추가하지 않았습니다.

## Not Published Yet

- `outputs/published/`를 생성하거나 수정하지 않았습니다.
- `content/published_log.md`를 수정하지 않았습니다.
- `reviews/approved/`로 이동하지 않았습니다.
- 실제 업로드 완료처럼 기록하지 않았습니다.

## Human Checks Still Required

- `《포란》`이 실제 업로드일 기준 종료 전인지 확인.
- `《더 하이브리드》` 무료 근거 재확인.
- 서울시립미술관 예약 필수 여부 확인.
- PNG 8장 순서와 이미지 품질 확인.
- slide_08 하단 정보 모바일 가독성 확인.
- 최종 캡션과 해시태그 확인.

## Recommended Next Step

사람이 `upload_checklist.md`를 완료한 뒤 실제 업로드 여부를 결정합니다.

승인 후에만 published output 생성, 업로드 기록, published log 정리를 진행합니다.
