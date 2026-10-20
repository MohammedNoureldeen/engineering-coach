# Synthetic example: expiry boundary

This invented Python example is for learning. It is not from a private project.

## Contract and reported problem

The application compares integer Unix timestamps in seconds. A token is valid only while `now < expires_at`. A caller reported that a token was accepted at the exact expiration second.

## Before

```python
def token_is_valid(now: int, expires_at: int) -> bool:
    return now <= expires_at
```

## After

```python
def token_is_valid(now: int, expires_at: int) -> bool:
    return now < expires_at
```

## Acceptance examples

For `expires_at = 100`, `now = 99` is valid, `now = 100` is expired, and `now = 101` is expired. The old predicate differs at equality. These examples specify expected behavior; they do not by themselves prove tests ran.

Both inputs are already in the same unit and use an authoritative application clock. Clock skew, cryptographic signature validation, and token revocation are outside this small example. Do not infer that the real-world security of a token system follows from this predicate alone.

## Learning prompts

```text
$engineering-coach changes examples/bug-fix.md
$engineering-coach quiz examples/bug-fix.md
$engineering-coach practice examples/bug-fix.md
```

In Claude Code, replace `$engineering-coach` with `/engineering-coach`.
