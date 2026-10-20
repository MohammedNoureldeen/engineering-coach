# Engineering decisions

Help the learner judge a choice under constraints, including whether the implemented choice is justified.

## Discuss the decisions that matter

Select the few decisions with a meaningful effect on correctness, complexity, reliability, cost, or maintenance. For each, connect the problem and constraint to the observed approach, a realistic alternative, the tradeoff, and a condition that would change the recommendation. A compact comparison table can help when the choices are genuinely comparable.

State whether the rationale is documented or inferred. Code reveals how something works; it does not by itself reveal why its author chose it. If there is no evidence supporting a claimed optimization, explain what is plausible and what measurement would settle it.

Use a small workload or failure example. Explain relevant complexity in its actual dimensions, such as database round trips, rows returned, memory, or contention. Do not conflate them. Replacing N per-record reads with a batch can reduce round trips while still doing linear result processing. A batch can also need chunking, authorization checks, missing-key handling, or a transaction boundary depending on the implementation.

Teach how to recognize a similar situation next time and offer one unanswered "what changes if..." question unless the user asks for a direct answer.

## Boundaries

Do not praise every choice or manufacture an exhaustive architecture review. Address demonstrated mistakes candidly. Describe hypothetical risks as possibilities, not production incidents. Avoid broad rules like "joins are always faster" or "caching solves N+1." Tie each claim to this workload and explain what evidence is missing.
