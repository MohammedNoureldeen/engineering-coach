# Synthetic example: audio noise gate

This invented Python feature suppresses quiet frames. It is a noise gate, not a general speech denoiser. The complete implementation is below; no streaming service, UI, benchmark, or listening test is implied.

## Feature contract

Input is a list of finite, normalized audio amplitudes in `[-1, 1]`. The gate uses RMS amplitude for each frame and persists its open/closed state across frames. It starts closed, opens at `RMS >= 0.20`, and closes at `RMS < 0.10`. The different thresholds introduce hysteresis. Empty frames return an empty list without changing state.

## Implementation

```python
import math


class NoiseGate:
    def __init__(self, open_threshold=0.20, close_threshold=0.10):
        if not (
            math.isfinite(open_threshold)
            and math.isfinite(close_threshold)
            and 0 <= close_threshold < open_threshold <= 1
        ):
            raise ValueError("Expected 0 <= close < open <= 1")
        self.open_threshold = open_threshold
        self.close_threshold = close_threshold
        self.is_open = False

    def process(self, frame):
        if not frame:
            return []
        rms = math.sqrt(sum(sample * sample for sample in frame) / len(frame))
        if self.is_open:
            if rms < self.close_threshold:
                self.is_open = False
        elif rms >= self.open_threshold:
            self.is_open = True
        return list(frame) if self.is_open else [0.0] * len(frame)
```

## Representative flow

Each value below is a separate single-sample frame processed by the same new gate:

| Input frame | Resulting state | Output |
| --- | --- | --- |
| `[0.05]` | closed | `[0.0]` |
| `[0.25]` | open | `[0.25]` |
| `[0.15]` | open | `[0.15]` |
| `[0.05]` | closed | `[0.0]` |

At exactly `[0.20]`, a closed gate opens. At exactly `[0.10]`, an already open gate stays open. At `[0.15]`, the output depends on the prior state. For multi-sample frames, RMS depends on all samples rather than only the peak or the first value.

## Limits to discuss

The gate suppresses entire frames without identifying speech. Quiet speech can be lost and loud noise can pass. There is no attack/release smoothing, hold timer, adaptive threshold, or spectral filtering. The caller supplies finite normalized samples; the method does not validate individual amplitudes. Abrupt transitions can affect audible quality, which would need actual listening and signal tests to assess. No claim of improved recognition accuracy is supported.

The state is stored on each instance, so reusing one instance across unrelated streams would couple their gating behavior. The code has no concurrency protection. These are observations about the implementation's boundaries, not reports of a production incident.

## Learning prompts

```text
$engineering-coach terms examples/noise-gate.md
$engineering-coach flow examples/noise-gate.md
$engineering-coach quiz examples/noise-gate.md اشرح بالعربية
```

In Claude Code, replace `$engineering-coach` with `/engineering-coach`.
