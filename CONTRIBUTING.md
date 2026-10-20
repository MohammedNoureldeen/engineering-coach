# Contributing

Improvements should help a developer reason about real code, correct a demonstrated teaching failure, or make installation clearer. Please keep the main skill concise and put mode-specific detail in its corresponding guide.

## Propose a change

1. Describe the user request and the observable problem. Include a minimal synthetic example or an artifact you have permission to share.
2. Change the canonical English skill instructions once. Update both READMEs if installation, modes, or user-visible behavior changes.
3. Run `python scripts/check_package.py` and `python evals/check_examples.py` using Python 3.10 or newer. These check the package, UTF-8 text, local documentation links, and the executable example contracts using the standard library.
4. If you have Codex's skill creator available, also run its `quick_validate.py` against `skills/engineering-coach`. The creator's validation utility needs PyYAML; the skill itself does not.
5. Try the relevant cases from [evals/cases.json](evals/cases.json) in a fresh session with the revised skill. Include your actual output, what you checked, the assistant version, and any limitations in the PR description. Use [the validation record](docs/validation.md) as an example of honest reporting.

Behavioral evaluation is a manual judgment against the stated criteria, not an exact-wording snapshot test. Check that evidence supports claims, hints do not reveal solutions too early, and direct requests still get direct answers. For read-only cases, compare the fixture before and after the session.

Do not contribute private chat transcripts, credentials, project-specific source, or learner records. Use the [examples](examples/bug-fix.md) as a model for reusable synthetic fixtures. Keep evaluation logs outside the tracked project unless deliberately reduced to a shareable, reviewed example.

## Language and compatibility

Arabic contributions and translation corrections are welcome. Keep code identifiers and invocation syntax unchanged, and use natural Arabic explanations with English technical terms where useful. Both READMEs should cover the same capabilities and limitations.

Keep `SKILL.md` portable. Add host-specific details to installation documentation or Codex's `agents/openai.yaml` rather than making the teaching depend on a particular connector. Report Claude Code runtime testing separately; documented compatibility is not a runtime test.

By contributing, you agree to license your contribution under this repository's [MIT License](LICENSE).

يمكنك المساهمة بالعربية أو الإنجليزية. استخدم أمثلة مصطنعة، وحدّث دليلَي الاستخدام عند تغيير السلوك، واذكر ما اختبرته فعليًا وحدود التحقق.
