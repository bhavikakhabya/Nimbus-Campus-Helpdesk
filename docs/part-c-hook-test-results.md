# Part C – Hook Test Results

## Objective
To verify that the protect-data.sh hook blocks writes to the protected data directory and safely handles invalid input.

## Test 1: Protected file
Input:
{"tool_input":{"file_path":"data/timetable.csv"}}

Expected: Block the operation.

Actual: The script displayed:
"Block: data/ is protected; edit it manually after reviewing the change."

Exit code: 2

Result: PASS

## Test 2: Normal file
Input:
{"tool_input":{"file_path":"README.md"}}

Expected: Allow the operation.

Actual: The script completed without a blocking message.

Exit code: 0

Result: PASS

## Test 3: Invalid JSON
Input:
invalid json

Expected: Refuse the operation because the input cannot be validated.

Actual: The script displayed:
"Block: unable to validate tool input; refusing protected write."

Exit code: 2

Result: PASS

## Conclusion
All three manual tests passed. The hook blocks protected data files, allows normal files, and refuses invalid JSON input.

Note: These are manual script tests. The hook has not been verified inside a live Claude Code session.
