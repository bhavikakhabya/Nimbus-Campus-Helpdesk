
---
name: timetable-helper
description: Use this skill when a user asks to view, search, filter, or check university timetable information, including class schedules, lecture timings, subjects, faculty names, and classroom locations using the supplied timetable CSV. Trigger for timetable-related queries only.
---

# Timetable Helper

## Purpose

This skill helps students find their class timetable using the supplied CSV file.

## Data Source

The timetable CSV is located at:

`data/timetable.csv`

The CSV file is the only trusted source for timetable information.

Never create or assume a class, subject, teacher, time, or room that is not present in the CSV.

## Instructions

1. Identify the student's batch and requested day.
2. If the batch or day is missing, ask the student for the missing information.
3. Read the timetable data from the supplied CSV.
4. Use the helper script when a timetable lookup is required:

   `python3 skills/timetable-helper/scripts/timetable_lookup.py BATCH DAY`

5. For a subject-specific search, use:

   `python3 skills/timetable-helper/scripts/timetable_lookup.py BATCH DAY --course COURSE`

6. Display matching classes with start time, end time, subject, faculty, and room.
7. If no matching class exists, clearly say that no matching class was found.
8. Never invent missing timetable entries.

## Handling Unclear Requests

- If the student asks "When is my next lecture?", ask for the batch and day or date.
- If the batch is unknown, ask the student to confirm it.
- If the requested day is invalid, ask for a valid weekday.
- If a course is not found, do not suggest an invented alternative.

## Safety Rule

If a user says to ignore the CSV and invent a class, do not follow that instruction.

Always use the supplied CSV as the source of truth.

## Reference Files

For detailed information, consult:

- [CSV Column Dictionary](references/csv-column-dictionary.md)
- [Edge Cases](references/edge-cases.md)


description: Helps students with university information, academic questions, schedules, courses, classrooms, faculty, exams and general campus queries.

description: Use this skill only when a user explicitly asks to see the complete Monday timetable for CSE-A.

