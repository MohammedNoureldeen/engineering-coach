# Synthetic example: N+1 database reads

This invented Python repository API illustrates a read optimization. It is not tied to an ORM and does not contain a measured benchmark.

## Repository contract

- `list_orders()` performs one database call and returns a list of dictionaries with `id` and integer `user_id` fields.
- `get_user(user_id)` performs one database call and returns a dictionary containing `name`, or `None` when absent.
- `get_users(user_ids)` performs one database call and returns a dictionary keyed by user ID, containing only found users. Its result order is unspecified.
- This example assumes a bounded page of orders and a batch within the database parameter limit. These methods already enforce the same access scope. No cache is present.

## Before

```python
def order_summaries(repo):
    orders = repo.list_orders()
    result = []
    for order in orders:
        user = repo.get_user(order["user_id"])
        result.append({
            "id": order["id"],
            "user": (user or {}).get("name", "Deleted user"),
        })
    return result
```

## After

```python
def order_summaries(repo):
    orders = repo.list_orders()
    if not orders:
        return []
    user_ids = sorted({order["user_id"] for order in orders})
    users = repo.get_users(user_ids)
    return [
        {
            "id": order["id"],
            "user": users.get(order["user_id"], {}).get("name", "Deleted user"),
        }
        for order in orders
    ]
```

## Acceptance examples and constraints

Given orders `[{"id": 1, "user_id": 7}, {"id": 2, "user_id": 7}, {"id": 3, "user_id": 9}]` and only user 7 with name `Ada`, both versions return:

```json
[
  {"id": 1, "user": "Ada"},
  {"id": 2, "user": "Ada"},
  {"id": 3, "user": "Deleted user"}
]
```

Under the stated contract, the old code makes four database calls for these three orders; the new code makes two and asks for IDs `[7, 9]`. For N orders the old call count is `1 + N`; for a nonempty supported batch the new count is two. Both versions make one call for an empty order list. Mapping by ID preserves order independently of batch result order.

Deduplication and result building still process the inputs. Sorting U unique IDs adds `O(U log U)` work, and the batch map uses memory proportional to its result. Constant call count is not constant total computation or constant result size.

No latency, CPU, or memory measurements are supplied. A join could be an alternative if the real schema and access rules support it. Oversized batches may require chunking; with chunk size B, user reads become `ceil(U / B)`, plus the order read. A real system also needs to consider consistency if users change between queries. These are constraints and possible next decisions, not changes implemented here.

## Learning prompts

```text
$engineering-coach decisions examples/n-plus-one.md
$engineering-coach flow examples/n-plus-one.md
$engineering-coach practice examples/n-plus-one.md
```

In Claude Code, replace `$engineering-coach` with `/engineering-coach`.
