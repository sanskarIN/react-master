# Commit and Release Conventions

## Local Git identity

When contributing from a local clone, configure the requested publisher email:

```bash
git config user.email "sanskarin@outlook.in"
```

Set the desired author name locally as well, for example:

```bash
git config user.name "Sanskar"
```

The GitHub connector used for automated repository maintenance does not expose an author-email override, so connector-created commits may use the connected GitHub account identity instead.

## Commit style

Prefer many **meaningful** commits over one unrelated bulk commit. Good examples:

- `docs: clarify Part 095 source status`
- `feat(part-042): add restored companion lab`
- `test(part-042): add regression coverage`
- `fix(part-042): correct runtime validation`
- `docs: add build instructions for Part 042`

Do not split trivial line changes solely to inflate history.

## Recommended workflow for recovered projects

1. Commit recovered source with provenance notes.
2. Commit dependency/toolchain cleanup separately.
3. Commit tests separately.
4. Commit bug fixes separately when they are independently reviewable.
5. Commit documentation/build instructions separately.
6. Run repository validation before release.

## Release versioning

Use semantic repository tags such as `v1.0.0`, `v1.1.0`, and `v2.0.0` for companion-code releases. The book's numbered Part sequence remains closed at Part 150.
