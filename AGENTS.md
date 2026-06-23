# Agent Team

얇은지갑클럽 카드뉴스 생산 파이프라인을 담당하는 에이전트 팀.
리서치 → 검증 → 기획 → 원고 → 디자인 → 업로드 → 성과분석 순서로 역할이 분리된다.

---

## 1. Trend Scout

**파일:** `.claude/agents/trend-scout.md`

서울/수도권의 무료/저가 문화행사, 전시, 팝업, 브랜드 프로그램, 공간, 음악, 취향 트렌드를 찾는다.
"싸기만 한 정보"가 아니라 "저렴하지만 취향 있어 보이는 경험"을 기준으로 선별한다.

---

## 2. Policy Scout

**파일:** `.claude/agents/policy-scout.md`

청년정책, 지원금, 주거, 교통, 문화패스, 교육비, 대학생 혜택을 찾는다.
온통청년, 정부24, 보조금24, 서울청년몽땅정보통 등 공식 출처만 사용한다.

---

## 3. Verifier

**파일:** `.claude/agents/verifier.md`

모든 후보의 공식 출처, 신청 가능 여부, 마감일, 대상 조건, 지역 조건, 비용을 검증한다.
공식 출처 없거나 마감 불명확한 후보는 폐기한다.

---

## 4. Curator

**파일:** `.claude/agents/curator.md`

콘텐츠 후보를 9개 항목으로 점수화하고 카드뉴스 제작 여부를 결정한다.
32점 이상 제작, 출처 신뢰도 3점 미만 무조건 폐기.

---

## 5. Editor

**파일:** `.claude/agents/editor.md`

카드뉴스 제목, 8장 슬라이드 구성, 본문 카피, 캡션, CTA를 작성한다.
얇은지갑클럽 에디터 톤을 유지한다.

---

## 6. Design Director

**파일:** `.claude/agents/design-director.md`

Claude Design용 프롬프트를 만들고 디자인 시스템과의 일관성을 검수한다.
1080x1350 매거진형 카드뉴스 8장 기준.

---

## 7. Growth Analyst

**파일:** `.claude/agents/growth-analyst.md`

업로드 후 저장률, 공유율, 댓글, 팔로우 전환을 분석하고 다음 콘텐츠 방향을 제안한다.

---

## Pipeline

```
Trend Scout / Policy Scout
        ↓
    Verifier
        ↓
    Curator (점수화 → 제작 결정)
        ↓
    Editor (원고)
        ↓
Design Director (디자인 프롬프트)
        ↓
    업로드
        ↓
Growth Analyst (성과 분석)
```
