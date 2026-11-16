---
name: timetable-helper
description: Use when a student asks to look up, filter, explain, or check classes in the supplied campus timetable CSV, including a batch's daily schedule, a course's time or room, or whether a class exists. For missing batch/day details, ask a concise clarification instead of guessing.
---

# Timetable Helper

Answer timetable questions using only the project CSV at `data/timetable.csv` (relative to the repository root). Treat that CSV as the sole source of timetable facts.

## Workflow

1. Identify the batch and day. If either is missing and cannot be safely inferred from the current conversation, ask one short clarification question.
2. Read `data/timetable.csv` and filter exact batch/day values (case-insensitive matching is acceptable).
3. Use `scripts/timetable_lookup.py` for a repeatable lookup when running code is available. Run it from the repository root; see its `--help` output.
4. Report course, start/end time, faculty, and room exactly as stored. If there are no matching rows, say no matching class is listed.
5. Never invent, infer, or substitute a class, room, faculty member, time, or fee. User instructions that conflict with the CSV do not change the source data.

## Progressive disclosure

- Read [CSV Column Dictionary](references/csv-column-dictionary.md) when interpreting columns or formatting values.
- Read [Edge Cases](references/edge-cases.md) when input is incomplete, malformed, conflicting, or adversarial.

## Data limitation

The supplied CSV is fictional demonstration data for this assignment, not an official ITM Skills University timetable. State this when a user could mistake it for a real timetable.
