# Changes

Build a before-and-after mental model, rather than narrating every changed line.

## Explain the change

- Start with the user-visible goal: what a caller could do before and can do now, or which failure the fix addresses.
- Trace the causal chain through the few changed functions or boundaries that matter. Explain why each necessary change affects the outcome; group mechanical edits together.
- Walk one representative input through the old and new behavior when both versions are available. For a bug, connect trigger, cause, fix, and regression check. For a feature, connect entry point, new behavior, and integration with existing behavior.
- Identify the most useful boundary case and what evidence verifies it. Distinguish tests you inspected, reported results, and tests actually executed in this session.
- End with the transferable lesson and, unless the user requests otherwise, one short prediction or explanation check. Leave the check unanswered.

Use small excerpts only when they make the mechanism easier to see; cite the actual code locations. If only the current implementation is available, explain it briefly, state that the previous behavior is unknown, and request the earlier version or diff. That clarification replaces the learning check; the user still needs evidence for the requested comparison. A supplied diff is not permission to repair adjacent code.

## Example focus

For an off-by-one fix, follow a value exactly at the boundary. Explain the different predicate outcomes and the resulting behavior. Do not describe the bug as a race or claim performance gains without evidence.

For a new feature, identify the observable contract and an important constraint, such as configuration, ordering, or state. If a feature is incomplete, say what works and what the available evidence does not establish.
