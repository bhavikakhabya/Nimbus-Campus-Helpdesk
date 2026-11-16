# Part B — Description rewrites and trigger comparison

Test the three descriptions below one at a time. Save the exact description, the prompts you used, and actual platform behaviour. Do not state that a description improved triggering unless the tests support it.

## Version 1 — Balanced (default in SKILL.md)

`Use when a student asks to look up, filter, explain, or check classes in the supplied campus timetable CSV, including a batch's daily schedule, a course's time or room, or whether a class exists. For missing batch/day details, ask a concise clarification instead of guessing.`

## Version 2 — Too broad (deliberate experiment)

`Use for student questions about campus life, classes, college, study, schedules, or university information.`

Expected risk: unrelated college or study questions may activate it. Verify with the two negative prompts and additional unrelated prompts.

## Version 3 — Too narrow (deliberate experiment)

`Use only when the user explicitly asks: “Show the timetable for [batch] on [weekday]” and provides both values in that exact format.`

Expected risk: valid variants such as asking for a course room or using different wording may fail to activate it. Verify with the course-room prompt and ambiguous prompt.

## Results table

| Version | Prompt | Triggered? | Correct? | Observation |
|---|---|---|---|---|
| V1 | TODO | TODO | TODO | TODO |
| V2 | TODO | TODO | TODO | TODO |
| V3 | TODO | TODO | TODO | TODO |

A description is too broad when it activates on unrelated tasks; too narrow when it misses legitimate paraphrases or closely related timetable questions. Use measured results, not assumptions.
