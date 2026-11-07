# MVP / PoC slice template (BA-owned)

Use when the squad needs a **time-boxed validation** before full delivery — not a replacement for the full refinement template.

Copy per initiative. Link to parent feature: `FEAT-____` in `ba-refinement-template.md`.

---

## Header

| Field | Value |
|-------|-------|
| Slice ID | POC-____ |
| Parent feature | FEAT-____ |
| Type | PoC / MVP / Spike |
| Owner (BA) | |
| Tech partner | |
| Target window | e.g. 2 weeks |
| Status | Draft / Approved / Running / Done |

---

## 1. Hypothesis

**We believe** …  
**For** … (segment / actor)  
**Will achieve** … (observable outcome)  
**We will know we are right when** … (signal)

| ID | Hypothesis element | Testable? |
|----|-------------------|-----------|
| H-01 | | Y / N |

**Good enough:** One sentence a stakeholder can repeat without reading the full spec.

---

## 2. Smallest testable slice

What is the **minimum** we can build or simulate to learn something — not the full feature?

| ID | In slice | Out of slice (defer) |
|----|----------|----------------------|
| SLICE-01 | | |
| SLICE-02 | | |

**Constraints for slice size:**

- [ ] Fits agreed calendar box (e.g. ≤ 2 weeks)
- [ ] No production commitments unless listed in §6
- [ ] Fake / manual steps documented if used

---

## 3. MVP vs PoC intent

| Dimension | PoC (learn) | MVP (deliver minimum value) |
|-----------|-------------|----------------------------|
| Primary goal | Validate assumption | Ship usable value |
| Audience | Internal + friendly pilots | Paying / production users |
| Quality bar | Good enough to observe signal | Good enough to support & measure |
| Success | Learn / kill / pivot | Retain / convert / operate |

**This initiative is:** ☐ PoC  ☐ MVP  ☐ Hybrid (explain below)

**Hybrid note:**

---

## 4. Scope for the slice

### In scope (slice only)

| ID | Item | Why in slice |
|----|------|--------------|
| IN-P-01 | | |

### Explicit exclusions

| ID | Exclusion | Risk if ignored |
|----|-----------|-----------------|
| OUT-P-01 | | |

---

## 5. Rules & constraints (slice-level)

| ID | Rule / constraint | Source |
|----|-------------------|--------|
| RULE-P-01 | | |
| CON-P-01 | Legal / security / data | |

---

## 6. Success signals — PoC vs production

| ID | Signal | PoC threshold | Production threshold | How measured |
|----|--------|---------------|----------------------|--------------|
| SIG-P-01 | | | | |
| SIG-P-02 | | | | |

**Good enough for PoC:** At least one **quantitative** and one **qualitative** signal with owner and date.

---

## 7. Dependencies & enablers

| ID | Need | Owner | Ready by |
|----|------|-------|----------|
| DEP-P-01 | Test accounts / data | | |
| DEP-P-02 | Legal / privacy sign-off | | |

---

## 8. Open questions (slice blockers only)

| ID | Question | Blocks | Owner | Due |
|----|----------|--------|-------|-----|
| Q-P-01 | | | | |

---

## 9. Handoff to delivery

| Artifact | Link / location |
|----------|-----------------|
| Full structured spec | `ba-refinement-template.md` copy |
| PoC/MVP slice | This file |
| Backlog items | |
| Demo / readout date | |

---

## Slice checklist (before kickoff)

- [ ] Hypothesis is falsifiable
- [ ] Slice IN/OUT reviewed with engineering
- [ ] PoC vs MVP intent agreed with sponsor
- [ ] Success signals have owners and dates
- [ ] Production commitments (if any) explicit in §6
- [ ] Parent spec RULE/OUT IDs referenced below

## Traceability to parent spec

| Parent ID | How slice uses it |
|-----------|-------------------|
| RULE-01 | |
| OUT-02 | |

---

## Anti-patterns

- PoC scope creep disguised as "just one more story"
- MVP without support / ops plan when real users are in scope
- Success signals that only measure "we shipped code"
