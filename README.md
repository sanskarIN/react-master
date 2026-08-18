# React Full Mastery — 150-Part Companion Repository

Official companion repository for **React Full Mastery: Complete 150-Part Master Edition** by **Ram Sandesh**.

**Repository:** https://github.com/sanskarIN/react-master

## What this repository contains

- `Part-001/` through `Part-150/` — one companion workspace per numbered volume.
- Architecture references, labs, capstone scaffolds, and validation tooling that are intentionally released as open source.
- Documentation for contribution, security, publishing status, release governance, and source recovery.
- A validator at `scripts/validate_all.py` that discovers actual JavaScript/TypeScript package projects and runs supported lint/test/build commands.

## What this repository does not contain

The commercial book manuscript, complete PDF/DOCX/EPUB editions, retail customer bundles, cover artwork, certificates, and commercial marketing assets are **not** published here. Historical companion source archives were not all available during the final master-publication build, so missing project code is never fabricated.

## Licensing

- Original companion source code intentionally published here: **MIT License** (`LICENSE`).
- Book/manuscript/editorial/cover/commercial publication content: **All Rights Reserved** (`BOOK-LICENSE.md`).

## Validation

```bash
python scripts/validate_all.py
```

Empty scaffold folders are skipped. Buildable projects are validated only when their source is actually present.

## Publication status

The numbered core learning series closes at **Part 150**. Future repository work should focus on companion-code completion, errata, documentation improvements, examples, tests, maintenance, and versioned releases rather than inventing Part 151.

## Author and contact

**Author:** Ram Sandesh  
**GitHub:** https://github.com/sanskarIN  
**Project/content contact:** sanskarin@outlook.in

No author avatar/photo is required for this project, and no X/Twitter profile link is included in the repository documentation.
