# CSV Column Dictionary

| Column | Meaning | Expected format |
|---|---|---|
| `batch` | Student batch | Text, e.g. `CSE-A` |
| `day` | Weekday | Monday through Friday in this sample |
| `start_time` | Class start | 24-hour `HH:MM` |
| `end_time` | Class end | 24-hour `HH:MM` |
| `course` | Course name | Text from CSV only |
| `faculty` | Faculty name | Text from CSV only |
| `room` | Room or lab | Text from CSV only |

Each row represents one class. Match batch and day without inventing aliases. Preserve stored course, faculty, room, and times. The CSV is the source of truth for this assignment.
