# BA refinement template

Copy this file per feature/epic. Keep IDs stable across Jira/ADO/wiki links.

---

## Header

| Field | Value |
|-------|-------|
| Feature ID | FEAT-____ |
| Title | |
| Author | |
| Status | Discovery / Refining / Ready |
| Stakeholders | |
| Last updated | |

---

## 1. Problem statement

**Who** is affected?  
**What** pain or opportunity?  
**Why now** (trigger, metric, risk)?

**Desired outcome (1 sentence):**

---

## 2. Scope

### In scope
| ID | Item | Notes |
|----|------|-------|
| IN-01 | | |

### Exclusions
| ID | Exclusion | Reason |
|----|-----------|--------|
| OUT-01 | | |

**Good enough for refinement:** Every Must-have requirement maps to an IN item or new IN row.

---

## 3. Actors & workflow

| Actor | Description |
|-------|-------------|
| | |

**Primary flow (happy path):**

```text
1.
2.
3.
```

**Alternate / exception flows:**

- 

---

## 4. Business rules

| ID | When (condition) | Then ( outcome ) | Else | Source |
|----|------------------|--------------------|------|--------|
| RULE-01 | | | | Policy / Legal / SME |

**Good enough for refinement:** Rules are testable — no "handle appropriately."

---

## 5. Constraints & dependencies

| ID | Type | Description | Impact if unresolved |
|----|------|-------------|---------------------|
| CON-01 | Legal / Tech / Data / Vendor | | |
| DEP-01 | Upstream system / team | | |

---

## 6. Assumptions

| ID | Assumption | Validate by | Owner |
|----|------------|-------------|-------|
| ASM-01 | | | |

---

## 7. Open questions

| ID | Question | Blocks | Owner | Due |
|----|----------|--------|-------|-----|
| Q-01 | | | | |

**Good enough for refinement:** No open **Blocker** questions without a dated decision or spike.

---

## 8. Acceptance signals

| ID | Signal | How verified |
|----|--------|--------------|
| AC-01 | Observable behavior or metric | Demo / analytics / audit |

---

## 9. Traceability (starter)

| Rule / scope ID | Story / ticket | Test note |
|-----------------|----------------|-----------|
| RULE-01 | | |

---

## 10. MVP / PoC planning (optional — before full build)

Use when the squad needs a **validated slice** before committing to full delivery. Detail in `mvp-poc-slice-template.md`.

| Field | Value |
|-------|-------|
| Slice type | PoC / MVP / Spike |
| Hypothesis (1 sentence) | |
| Smallest testable slice | |
| Target window | e.g. 2 weeks |

### Scope for slice only

| ID | In slice | Deferred to full feature |
|----|----------|--------------------------|
| SLICE-01 | | |

### Success signals — PoC vs production

| ID | Signal | PoC threshold | Production threshold |
|----|--------|---------------|----------------------|
| SIG-01 | | | |

**Good enough for refinement:** PoC/MVP slice has **explicit OUT** rows; hypothesis is falsifiable; production commitments (if any) named in SIG column.

---

## Domain extensions (customize in Exercise 2)

### Compliance / privacy
| ID | Requirement |
|----|-------------|
| | |

### Pricing / commercial
| ID | Requirement |
|----|-------------|
| | |

---

## Refinement checklist

- [ ] Problem & outcome agreed with requestor
- [ ] Exclusions reviewed by impacted teams
- [ ] Rules have sources or flagged as draft
- [ ] Acceptance signals demo-able
- [ ] Open blockers owned and dated

---

## Anti-patterns (delete before sharing if not needed)

- Do not put database schema here unless constraint-driven
- Do not write UI pixel specs — link design when ready
- Do not close open questions by guessing — mark ASM-## instead
