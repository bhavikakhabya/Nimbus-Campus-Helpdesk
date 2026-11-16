# Part D — MCP Protocol Trace (capture your real session)

Paste the actual JSON-RPC messages/logs captured from MCP Inspector or another MCP client. SDK/protocol versions differ; do not represent the illustrative outline below as a captured trace.

## Required exchanges

1. `initialize` request and response: record the protocol version and capabilities offered by each side.
2. `notifications/initialized` notification, if present in the protocol revision/client trace.
3. `tools/list` request and response: include the exact tool names, descriptions, and input schemas returned.
4. `tools/call` request and response for `get_timetable` using `CSE-A` and `Monday`.
5. One failure case, such as invalid day `Funday` or unknown mock ID `STU9999`.

## Explain in your own words

Capability negotiation is the client and server declaring which protocol version and optional features they support so the session can use compatible operations. Describe the exact version and capabilities from your trace, and do not assume a capability that was not advertised.

## Tool descriptions as attack surface

Tool descriptions are shown to the model as part of the context used to decide whether and how to call tools. Misleading or hostile descriptions can steer tool selection or encourage unsafe arguments, so inspect descriptions, schemas, server code, and outputs as untrusted inputs.

**Evidence file(s):** TODO (save screenshots/logs in `screenshots/`).
