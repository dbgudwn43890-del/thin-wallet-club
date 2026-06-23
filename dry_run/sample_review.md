# MOCK REVIEW SAMPLE

This is not a real human review request.
This file exists only to test the manual pipeline dry run format.

---

review_id: DRY_REVIEW_001
linked_candidate_id: SAMPLE_YOUTH_BENEFIT
review_reason: Mock caution result needs human decision before curation simulation.

---

## Checklist

- [ ] Confirm this is mock data only.
- [ ] Confirm no real URL, institution, policy, event, or brand is included.
- [ ] Confirm no cardnews script was created.
- [ ] Confirm no caption was created.
- [ ] Confirm no design prompt was created.
- [ ] Confirm production folders remain empty except `.gitkeep`.
- [ ] Confirm caution/fail/pass branches are understandable.

## Reviewer Decision Options

- `approve_for_dry_run_curation`: Continue dry run only.
- `request_mock_revision`: Revise the sample data format.
- `reject_sample`: Remove this sample from dry run.

## Notes

- This review sample must not be moved into `reviews/human_review_queue/`.
- Any real human review file should follow `ops/human_review_rules.md`.
- Dry run learnings may be summarized in `docs/manual_pipeline_dry_run.md`.
