# Part D – JSON-RPC Communication Evidence

## Testing Environment
- MCP Inspector: 2.13.0
- Python MCP SDK: 1.30.0
- Transport: stdio
- Protocol version: 2025-11-25
- Server name: nimbus-campus-helpdesk

## 1. Initialize Request

The client sent an initialize request using JSON-RPC 2.0.

Method: initialize
Request ID: 0

Client information:
- Name: mcp-inspector
- Version: 2.13.0

Client capabilities included:
- sampling
- elicitation
- roots
- tasks
- extensions

## 2. Initialize Response

The server successfully responded.

Server information:
- Name: nimbus-campus-helpdesk
- Version: 1.30.0
- Protocol version: 2025-11-25

Server capabilities:
- experimental
- prompts
- resources
- tools

This demonstrates successful protocol initialization and capability negotiation.

## 3. Initialized Notification

The client sent:
notifications/initialized

This notification confirmed that the initialization phase was complete.

## 4. Tools List Request

Method: tools/list
Request ID: 2

The server returned two registered tools.

### Tool 1: get_timetable

Description:
Return classes listed in the mock timetable for an exact batch and weekday. Never infer missing classes.

Input schema:
- batch: string (required)
- day: string (required)

### Tool 2: get_fee_status

Description:
Return a fictional fee-status record for a mock student ID (STU1001-STU1003); do not use real student data.

Input schema:
- student_id: string (required)

## 5. Resources List Request

Method: resources/list
Request ID: 1

Returned resource:
- Name: hostel_rules
- URI: hostel://rules
- MIME type: text/plain

## 6. Prompts and Resource Templates

prompts/list returned an empty list.
resources/templates/list returned an empty list.

These are not required components for this assignment.

## 7. Capability Negotiation Explanation

The client advertised capabilities it could support. The server responded with the capabilities it provides.

The server advertised tools, resources and prompts. The client and server successfully completed the initialization handshake using protocol version 2025-11-25.

## Evidence Source

MCP Inspector exported protocol messages on 16 November 2026.
The exported JSON contains the actual initialize request and response, initialized notification, tools/list response and resource discovery response.

Note: The tools/call request and response will be documented separately after capturing the corresponding Inspector call.

## 8. Tool Call Request and Response

The MCP Inspector exported the following actual JSON-RPC tool call.

Method: tools/call
Request ID: 6
Tool name: get_timetable

Request arguments:
{
  "batch": "CSE-A",
  "day": "Monday"
}

Response:
- batch: CSE-A
- day: Monday
- count: 3
- isError: false

Returned classes:
1. Python Programming – 09:00 to 10:00 – Prof. Sharma – Lab-01
2. Mathematics – 10:00 to 11:00 – Prof. Mehta – Room-201
3. Computer Fundamentals – 11:15 to 12:15 – Prof. Patel – Room-202

Execution duration: 52 ms.

The tool call completed successfully and returned the expected mock timetable records.

## 9. Failure Case

An invalid student ID was tested with get_fee_status.

The server returned an error stating that the mock student ID was unknown and suggested valid IDs STU1001, STU1002, and STU1003.

This demonstrates input validation and error handling.
