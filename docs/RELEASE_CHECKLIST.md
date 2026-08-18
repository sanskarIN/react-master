# Release Checklist

Use this checklist before tagging a stable companion-repository release.

## Repository integrity

- [ ] Part folders `Part-001/` through `Part-150/` are present.
- [ ] No accidental `Part-151/` core-series continuation is introduced.
- [ ] `python scripts/validate_all.py` completes as expected.
- [ ] Every real package project has documented install/build/test commands.
- [ ] Empty placeholder folders are clearly described rather than filled with fabricated source.

## Security and privacy

- [ ] No API keys, passwords, access tokens, signing keys, private URLs, or personal/private datasets are committed.
- [ ] Logs and fixtures contain no unnecessary personal data.
- [ ] Dependency and build changes have been reviewed for supply-chain impact.

## Licensing

- [ ] New original companion code is compatible with the MIT repository license.
- [ ] Third-party notices are included when required.
- [ ] Commercial manuscript, cover, certificates, and customer bundles remain outside the public repository.

## Documentation

- [ ] README reflects the current release.
- [ ] `CHANGELOG.md` records notable changes.
- [ ] Source-status notes are accurate.
- [ ] Version-sensitive instructions point readers to current official documentation where appropriate.
- [ ] X/Twitter is not used as stable publication metadata.
- [ ] No author avatar/photo is required for repository documentation.

## Release

- [ ] Choose the semantic version.
- [ ] Verify the final commit SHA.
- [ ] Tag/release only after validation passes.
- [ ] Record any known limitations in the release notes.
