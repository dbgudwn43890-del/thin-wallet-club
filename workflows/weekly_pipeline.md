# Weekly Pipeline

얇은지갑클럽 주간 콘텐츠 생산 루틴.
목표: 주 4개 업로드 (월/수/금/일).

---

## 주간 업로드 스케줄

| 요일 | 카테고리 | 담당 에이전트 |
|------|---------|-------------|
| 월 | 청년 혜택/지원금 | Policy Scout → Verifier → Editor |
| 수 | 무료·저가 문화생활 | Trend Scout → Verifier → Editor |
| 금 | 브랜드 프로그램/팝업/기회 | Trend Scout → Verifier → Editor |
| 일 | 취향 입문 or 에세이 | Editor (직접 기획) |

대학생 콘텐츠: 격주 1회, 월요일 or 수요일 슬롯.

---

## 월요일 (D-7): 리서치 주간

- [ ] Policy Scout 실행 → policy_sources.yml 기반 후보 수집
- [ ] Trend Scout 실행 → culture_sources.yml, brand_sources.yml 기반 후보 수집
- [ ] 후보 `content/ideas.md`에 추가
- [ ] 각 후보 점수화 필드 채우기

## 화요일 (D-6): 검증

- [ ] Verifier 실행 → 전 주 수집 후보 전체 검증
- [ ] 공식 출처 URL 확인
- [ ] 마감일 지난 건 폐기
- [ ] 검증 결과를 `content/ideas.md`에 업데이트

## 수요일 (D-5): 큐레이션 + 기획

- [ ] Curator 실행 → 점수화, 제작 결정
- [ ] 이번 주 4개 콘텐츠 확정
- [ ] 각 콘텐츠 브리프 생성 → `drafts/briefs/`에 저장
- [ ] 캘린더 업데이트 → `content/calendar.md`

## 목요일 (D-4): 원고 작성

- [ ] Editor 실행 → 4개 콘텐츠 8장 원고 작성
- [ ] 원고 → `drafts/scripts/`에 저장
- [ ] 캡션 → `drafts/captions/`에 저장
- [ ] 팩트체크 체크리스트 실행 → `workflows/factcheck_checklist.md`

## 금요일 (D-3): 디자인

- [ ] Design Director 실행 → 4개 디자인 프롬프트 생성
- [ ] 프롬프트 → `drafts/design_prompts/`에 저장
- [ ] Claude Design에서 카드뉴스 제작
- [ ] 초안 → `outputs/reviewed/`에 저장

## 토요일 (D-2): 검수

- [ ] 카드뉴스 검수 체크리스트 실행 → `workflows/cardnews_checklist.md`
- [ ] 정보/브랜드/디자인 검수 전부 통과해야 업로드
- [ ] 캡션 최종 교정
- [ ] 해시태그 세트 확인

## 일요일/월요일: 업로드

- [ ] 스케줄 예약 or 실시간 업로드
- [ ] 업로드 후 `content/published_log.md`에 기록
- [ ] 완료 파일 → `outputs/published/`로 이동

## 업로드 후 (D+3): 성과 분석

- [ ] Growth Analyst 실행 → 저장률, 공유율, 댓글, 팔로우 분석
- [ ] 분석 결과 → `content/published_log.md`에 추가
- [ ] 다음 주 콘텐츠 방향에 반영

---

## 비상 대응

### 후보가 부족한 경우
→ sources/*.yml 추가 출처 확인
→ 에세이형 콘텐츠로 대체 (정보 검증 없이 제작 가능)

### 마감일이 급할 경우
→ 검증 → 원고 → 디자인 → 업로드를 1일 안에 진행
→ 이 경우 Verifier 검증 2회로 강화

### 콘텐츠 오류 발견 시 (업로드 후)
→ 즉시 스토리 또는 캡션 수정 공지
→ 잘못된 정보는 삭제 후 재업로드
→ `forbidden_rules.md` 위반 시 계정 관리자에게 보고
