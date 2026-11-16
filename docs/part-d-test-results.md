# Part D – MCP Server Test Results

## Environment
- Python: 3.11.18
- MCP SDK: 1.30.0
- Transport: stdio
- Testing tool: MCP Inspector

## Server Connection
The Nimbus Campus Helpdesk MCP server connected successfully to MCP Inspector.
The server responded to protocol initialization and listing requests.

## Test 1: get_timetable
Input:
- batch: CSE-A
- day: Monday

Expected: Three timetable entries.

Actual: Three entries returned:
1. Python Programming – 09:00 to 10:00 – Prof. Sharma – Lab-01
2. Mathematics – 10:00 to 11:00 – Prof. Mehta – Room-201
3. Computer Fundamentals – 11:15 to 12:15 – Prof. Patel – Room-202

Result: PASS

## Test 2: get_fee_status
Input:
- student_id: STU1001

Expected: A mock fee-status record.

Actual:
- Status: Paid
- Amount due: 0
- Currency: INR

Result: PASS

## Test 3: Hostel Rules Resource
Resource URI:
hostel://rules

Expected: Return the fictional hostel rules document.

Actual: The resource was successfully read in MCP Inspector.

Result: PASS

## Failure Case
An initial fee-status request used an invalid or unmatched student ID.

Actual: The server returned an error explaining that the ID was unknown and listed the valid mock IDs.

Result: PASS – Invalid input was handled without crashing the server.

## Conclusion
All three required MCP components were tested successfully through MCP Inspector. The server uses fictional assignment data only.
