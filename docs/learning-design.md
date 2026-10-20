# Why this teaching approach

Engineering Coach serves developers who use AI to meet delivery deadlines and want to understand what they ship. The goal is observable reasoning: explain a change, predict a new case, diagnose a defect, and extend an idea independently. A fluent summary alone does not demonstrate those abilities.

## Evidence informing the design

The [Institute of Education Sciences practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/1) recommends alternating worked examples with problem solving, connecting concrete and abstract representations, retrieval through quizzing, and deep explanatory questions. Its evidence ratings vary by recommendation, and much of its scope is educational rather than workplace software development. We use these as general design principles, not proof that this skill improves engineering performance.

The 2026 study [How AI Impacts Skill Formation](https://arxiv.org/abs/2601.20245), by Judy Hanwen Shen and Alex Tamkin, investigated learning an unfamiliar Python asynchronous library with and without AI assistance. It found lower immediate mastery in the AI-assisted condition on average. Its qualitative analysis associated comprehension-oriented interactions with stronger learning outcomes. These interaction patterns were not randomized teaching interventions, so they do not establish a causal ranking of coaching methods. The small sample and immediate assessment also limit claims about long-term professional development. See the [authors' explanation and limitations](https://www.anthropic.com/research/AI-assistance-coding-skills).

## Our design choices

- **Explain from evidence.** A concrete input traced through actual code gives the learner something to reason about. Teaching must also admit missing history, uncertain rationale, and unmeasured benefits.
- **Add a small recall opportunity.** Explanation modes offer one unanswered check after explaining. Users can opt out or ask directly for an answer.
- **Transfer to a changed constraint.** Quiz and practice modes change a boundary, workload, or failure case, then wait for an attempt. Feedback addresses the mechanism rather than only marking the answer.
- **Use progressively specific hints.** Provide enough support to continue without immediately completing the reasoning for the learner.
- **Adapt without tracking.** Use the conversation to adjust depth and revisit misconceptions. No profiles, automatic schedules, or claims of mastery from one correct response.

This exact combination is a product design informed by the evidence, not a scientifically validated intervention. Behavioral checks assess whether the assistant follows the design; proving learning gains would require learner studies, including delayed recall and transfer assessments.

## Keeping the instructions useful

The main skill holds routing, evidence rules, and shared teaching behavior. Mode guides supply focused guidance and load only when selected. The public examples are synthetic so they can be shared and evaluated safely. Source links and host installation guidance were reviewed on **2026-10-20**; platform behavior can change.
