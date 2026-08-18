# Master Publication QA Record

This repository accompanies the completed **React Full Mastery — Complete 150-Part Master Edition**.

## Core-series audit

- Parts 001–150 accounted for exactly once in the final master inventory.
- The current authoritative late-series branch was retained for Parts 116–150.
- The numbered core series closes at Part 150; no Part 151 continuation is required.
- Parts 48, 61, and 95 were reconstructed for the publication master because their historical source binaries were unavailable in the final archive. They are identified as reconstructed sources in the publication audit rather than presented as surviving originals.

## Master publication checks

- Master DOCX created and archive-integrity checked.
- Master PDF created at approximately 3,187 pages.
- PDF is searchable, openable, unencrypted, and uses embedded fonts.
- Master DOCX contains explicit bookmarks for Parts 001–150.
- Embedded media was namespaced during merge to prevent cross-document relationship collisions.
- Accessibility cleanup removed high- and medium-severity audit findings in the master DOCX; remaining low-level advisories relate to visible raw URL text.
- Final publication package uses SHA-256 manifests.

## Content/privacy publication constraints

- No Ram Sandesh author avatar or portrait is required or intentionally used.
- X/Twitter is intentionally omitted from stable publication metadata and repository documentation.
- Commercial book files are kept outside the MIT-licensed companion repository.

## Companion-code limitation

Not every historical companion-project archive survived into the final build. Empty numbered folders are therefore intentional placeholders. Missing code must not be fabricated merely to make the repository look complete.

## Validation command

```bash
python scripts/validate_all.py
```

The validator should skip empty scaffold directories and validate actual package projects only when source is present.
