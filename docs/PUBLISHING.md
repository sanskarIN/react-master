# Publishing Guide

This repository is the open-source companion for **React Full Mastery: Complete 150-Part Master Edition** by **Ram Sandesh**.

Official repository: https://github.com/sanskarIN/react-master

## Distribution model

Use wide ebook distribution unless you intentionally choose an exclusivity program. Keep the commercial manuscript separate from this public repository.

Recommended channels:

- Amazon KDP — EPUB for Kindle; use platform preview tools before release.
- Google Play Books — EPUB and/or PDF.
- Kobo Writing Life — validated EPUB.
- Apple Books — validated EPUB.
- Gumroad / Buy Me a Coffee / Payhip — direct-sale buyer bundle containing the customer-facing PDF, EPUB, preview, README, and checksums.
- GitHub — companion code, labs, documentation, architecture references, and validation tools only.

## Physical edition

The complete master is about 3,187 pages, so physical publication should use the prepared multi-volume print split rather than one oversized paperback/hardcover.

## Public repository policy

Publish here:

- original companion code you own;
- labs and safe sample datasets;
- build/run instructions;
- architecture examples;
- tests, validation scripts, contribution guidance, and security policy.

Do not publish here:

- complete paid PDF/DOCX/EPUB manuscripts;
- customer-only bundles;
- cover/marketing assets unless intentionally released;
- secrets, signing material, tokens, passwords, or private datasets;
- third-party copyrighted content without redistribution rights.

## Metadata

- Title: React Full Mastery
- Edition: Complete 150-Part Master Edition
- Author: Ram Sandesh
- Contact: sanskarin@outlook.in
- Companion repository: https://github.com/sanskarIN/react-master

No author avatar/photo is required, and X/Twitter is intentionally omitted from stable publication metadata.

## Licensing

Original companion code intentionally released here uses the **MIT License**. The commercial manuscript, editorial text, covers, certificates, and commercial publication assets remain **All Rights Reserved** under `BOOK-LICENSE.md`.

## Release checklist

- Validate lint/test/build for every project that actually has source.
- Confirm no private credentials are committed.
- Confirm the complete commercial manuscript is absent.
- Verify README links and contact metadata.
- Record changes in `CHANGELOG.md`.
- Tag stable releases using semantic versions such as `v1.0.0`.
- Keep checksums for externally distributed publication packages.
