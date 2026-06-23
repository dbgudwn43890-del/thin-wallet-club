# Pre-Upload Review: 001_free_seoul_exhibitions

content_id: 001_free_seoul_exhibitions
review_status: conditional
reviewed_at: 2026-06-24
review_type: pre_upload_package_review

## Reviewed Files

- `data/candidates/001_free_seoul_exhibitions_candidates.yml`
- `data/verified/001_free_seoul_exhibitions_verified.yml`
- `data/verified/001_free_seoul_exhibitions_curated.yml`
- `data/rejected/001_free_seoul_exhibitions_rejected.yml`
- `drafts/briefs/001_free_seoul_exhibitions_brief.yml`
- `drafts/scripts/001_free_seoul_exhibitions_script.yml`
- `drafts/design_prompts/001_free_seoul_exhibitions_design_prompt.yml`
- `brand/voice_and_tone.md`
- `brand/forbidden_rules.md`
- `brand/design_system.md`
- `ops/quality_rules.md`
- `workflows/factcheck_checklist.md`
- `workflows/cardnews_checklist.md`
- `.claude/commands/review-before-upload.md`

## Fact Check Result

status: conditional_pass

Summary:

- Curator selected 5개와 script의 5개 전시 구성이 일치한다.
- selected 후보는 유영국, 권병준, 서서울미술관 개관 특별 미디어 소장품전, 포란, 더 하이브리드다.
- 전시명, 장소, 기간, 무료 여부, 출처, 확인일은 verified, curated, script, design prompt 사이에서 큰 충돌 없이 이어진다.
- script와 design prompt 모두 확인일 `2026.06.23`을 유지한다.
- `《포란》`은 종료 임박 후보로 표시되어 있고, 발행 지연 시 제외 또는 문구 수정이 필요하다는 리스크가 남아 있다.
- `《더 하이브리드》`는 무료 근거가 전시 상세 + 관람안내 조합이라는 점이 script와 design prompt에 남아 있다.
- 예약 필수 여부는 단정하지 않았고, `방문 전 예약/운영시간 확인` 문구가 포함되어 있다.

Notes:

- `《포란》`은 2026.07.05 종료로 제작/발행 지연에 민감하다.
- `《더 하이브리드》`는 무료 여부를 전시 상세 단독으로 닫지 않았으므로 최종 제작 전 사람 확인이 필요하다.
- 서울시립미술관 후보들의 전시 사전 예약 링크가 필수인지 선택인지 아직 확정하지 않았다.

## Tone Check Result

status: conditional_pass

Summary:

- script의 커버 headline은 `서울 무료 전시 5`로 정보 중심을 유지한다.
- script에는 `무료인데 꽤 괜찮아`, `얇은지갑클럽 저장용 리스트`, `감성 무료 전시`, `요즘 핫한`, `안 가면 손해`, `무조건 가야 함`, `MZ 취향`, `힙한`, `모르면 손해` 같은 금지 문구가 독자-facing 문구로 남아 있지 않다.
- design prompt에는 금지 문구가 `do_not_do`와 `caution_for_designer` 맥락에서만 등장한다.
- 브랜드명은 마지막 장 small_note와 design prompt의 하단 푸터 지시 중심으로 제한되어 있어 과다 노출로 보이지 않는다.
- 전반적으로 공공기관 홍보문보다 짧은 정보형 매거진 톤에 가깝다.

Notes:

- brief 파일에는 이전 단계의 hook/title 후보 일부가 남아 있지만, 현재 제작 기준은 script와 design prompt의 최신 톤 규칙을 따른다.
- 실제 카드 제작자는 brief의 오래된 후보 문구를 재사용하지 말아야 한다.

## Design Prompt Check Result

status: conditional_pass

Summary:

- design prompt는 공식 이미지 없이도 작동하는 타이포그래피 중심 설계다.
- 전시 포스터, 작품 이미지, 키비주얼을 직접 베끼거나 유사 재현하지 말라는 지시가 명확하다.
- 각 슬라이드는 headline, body_copy, small_note, design_intent, layout_direction, typography_direction, visual_motif, information_hierarchy를 포함한다.
- Slide 8에 출처, 확인일, 방문 전 예약/운영시간 확인 안내가 읽히도록 설계되어 있다.
- 카드별 visual motif는 추상적 구조, 선, 블록, 여백 중심이라 권리 리스크가 낮다.

Notes:

- 실제 디자인 제작 시 외부 이미지나 전시 포스터를 추가하면 별도 권리 확인이 필요하다.
- design prompt는 이미지 생성물이 아니며, outputs 파일을 생성하지 않았다.

## Risk Summary

- `《포란》` 일정 리스크: 발행일이 늦어지면 종료 임박 문구 수정 또는 후보 제외 필요.
- `《더 하이브리드》` 무료 근거 리스크: 전시 상세 + 관람안내 조합으로 무료 여부를 확인한 상태.
- 예약 여부 리스크: 전시 사전 예약 링크가 필수인지 선택인지 미확정.
- 기관 편중 리스크: selected 5개 중 4개가 서울시립미술관 후보이나, 앞선 사람 승인으로 허용됨.
- brief 잔여 문구 리스크: 최신 톤 보정 전 hook/title 후보가 brief에 남아 있으므로 제작자는 script/design prompt를 우선해야 함.

## Blocking Issues

None.

## Non-Blocking Issues

- `《포란》`은 실제 제작/발행일 기준으로 종료일까지 남은 일수를 다시 계산해야 한다.
- `《더 하이브리드》`는 무료 근거 표기를 최종 카드 제작 전 사람이 한 번 더 확인해야 한다.
- 예약 필수 여부는 단정하지 않았지만, 실제 카드에서 방문 전 확인 안내가 충분히 읽히는지 확인해야 한다.
- brief의 오래된 문구를 디자인 제작자가 재사용하지 않도록 script와 design prompt를 기준 파일로 지정해야 한다.
- 아직 실제 이미지, 캡션, 업로드 문구가 없으므로 최종 업로드 승인은 별도 단계에서 해야 한다.

## Human Review Required

- `《포란》`이 실제 발행 예정일 기준으로 여전히 사용 가능한지 확인.
- `《더 하이브리드》` 무료 여부를 전시 상세 + 관람안내 조합으로 표기해도 되는지 확인.
- 서울시립미술관 전시 사전 예약 링크가 필수 예약인지 선택 예약인지 확인.
- 카드 제작자가 brief의 이전 hook/title 후보가 아니라 최신 script와 design prompt를 기준으로 작업하는지 확인.
- 디자인 제작 시 전시 포스터, 작품 이미지, 키비주얼을 직접 복제하지 않았는지 확인.
- 최종 카드 이미지에서 출처, 확인일, 방문 전 예약/운영시간 확인 문구가 읽히는지 확인.
- 캡션과 업로드 문구는 아직 작성되지 않았으므로 별도 생성 및 검수 필요.

## Recommended Next Action

Proceed to controlled card production only after the human reviewer confirms the non-blocking issues above.

Recommended status:

- `conditional`: 제작 도구에 넘길 수는 있으나, 실제 업로드 전에는 일정/무료 근거/예약 여부/이미지 권리/최종 카드 가독성 확인이 필요하다.

Do not upload yet.
