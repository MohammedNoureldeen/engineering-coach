"""Execute the synthetic Python examples against their public contracts."""

import math
from pathlib import Path
import re
import unittest


EXAMPLES = Path(__file__).resolve().parents[1] / "examples"


def implementations(filename):
    text = (EXAMPLES / filename).read_text(encoding="utf-8")
    modules = []
    for snippet in re.findall(r"```python\n(.*?)\n```", text, re.DOTALL):
        namespace = {}
        exec(compile(snippet, filename, "exec"), namespace)
        modules.append(namespace)
    return modules


class Repository:
    def __init__(self, orders):
        self.orders = orders
        self.users = {7: {"name": "Ada"}, 9: {"name": "Lin"}}
        self.calls = []

    def list_orders(self):
        self.calls.append(("orders",))
        return list(self.orders)

    def get_user(self, user_id):
        self.calls.append(("user", user_id))
        return self.users.get(user_id)

    def get_users(self, user_ids):
        self.calls.append(("users", tuple(user_ids)))
        return {key: self.users[key] for key in reversed(user_ids) if key in self.users}


class ExampleContracts(unittest.TestCase):
    def test_expiry_before_and_after(self):
        before, after = implementations("bug-fix.md")
        self.assertEqual([before["token_is_valid"](n, 100) for n in (99, 100, 101)], [True, True, False])
        self.assertEqual([after["token_is_valid"](n, 100) for n in (99, 100, 101)], [True, False, False])

    def test_batch_preserves_order_and_missing_users(self):
        before, after = implementations("n-plus-one.md")
        orders = [{"id": 1, "user_id": 9}, {"id": 2, "user_id": 7}, {"id": 3, "user_id": 9}, {"id": 4, "user_id": 11}]
        expected = [{"id": 1, "user": "Lin"}, {"id": 2, "user": "Ada"}, {"id": 3, "user": "Lin"}, {"id": 4, "user": "Deleted user"}]
        old_repo, new_repo = Repository(orders), Repository(orders)
        self.assertEqual(before["order_summaries"](old_repo), expected)
        self.assertEqual(after["order_summaries"](new_repo), expected)
        self.assertEqual(len(old_repo.calls), 5)
        self.assertEqual(new_repo.calls, [("orders",), ("users", (7, 9, 11))])

    def test_empty_order_list_skips_user_reads(self):
        for module in implementations("n-plus-one.md"):
            repo = Repository([])
            self.assertEqual(module["order_summaries"](repo), [])
            self.assertEqual(repo.calls, [("orders",)])

    def test_gate_sequence_and_empty_frame(self):
        gate = implementations("noise-gate.md")[0]["NoiseGate"]()
        self.assertEqual([gate.process([n]) for n in (0.05, 0.25, 0.15, 0.05)], [[0.0], [0.25], [0.15], [0.0]])
        gate.process([0.25])
        self.assertEqual(gate.process([]), [])
        self.assertTrue(gate.is_open)

    def test_gate_thresholds_and_prior_state(self):
        factory = implementations("noise-gate.md")[0]["NoiseGate"]
        gate = factory()
        self.assertEqual(gate.process([0.15]), [0.0])
        self.assertEqual(gate.process([0.20]), [0.20])
        self.assertEqual(gate.process([0.10]), [0.10])
        self.assertEqual(gate.process([0.15]), [0.15])
        self.assertEqual(gate.process([0.09]), [0.0])

    def test_gate_uses_all_samples_and_keeps_input(self):
        gate = implementations("noise-gate.md")[0]["NoiseGate"]()
        frame = [0.0, 0.4]
        self.assertEqual(gate.process(frame), frame)
        self.assertEqual(frame, [0.0, 0.4])

    def test_invalid_thresholds(self):
        factory = implementations("noise-gate.md")[0]["NoiseGate"]
        for opening, closing in ((0.1, 0.1), (0.1, 0.2), (1.1, 0.1), (0.2, -0.1), (math.nan, 0.1), (0.2, math.inf)):
            with self.subTest(opening=opening, closing=closing):
                with self.assertRaises(ValueError):
                    factory(opening, closing)


if __name__ == "__main__":
    unittest.main(verbosity=2)
