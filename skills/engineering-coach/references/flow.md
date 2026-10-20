# Execution flow

Trace one concrete request, event, or data item. Establish its entry point and observable result before expanding the path.

Follow the relevant calls and data transformations in order. Show where state lives, when reads and writes occur, and which component owns each transition. Distinguish synchronous calls from queued, retried, streamed, or concurrent work only when those mechanisms are present in the evidence.

Use a short numbered trace or a small diagram when it clarifies the flow. Include identifiers and verified source references for the important boundaries. Describe a path as observed only when the code or supplied evidence supports it. At a missing boundary, name the gap instead of inventing a downstream service or response.

After the normal path, trace one important failure, empty input, or boundary case. Explain what happens to the output and state. If you see a retry, inspect what limits it and whether repetition affects results; do not assume retries, rollback, or idempotency exist.

For a stateful filter, show the prior state, incoming value, state transition, and output for several consecutive samples. A single isolated input may not explain the behavior.

Close with the mental model of the system and one unanswered prediction check unless a direct answer was requested. Keep unrelated subsystems outside the walkthrough.
