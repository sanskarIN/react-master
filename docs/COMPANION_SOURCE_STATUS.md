# Companion Source Status

The repository contains one numbered workspace for every React Full Mastery volume from `Part-001/` through `Part-150/`.

## Status meanings

Each part README should make clear whether the folder contains:

- surviving companion source;
- a reconstructed/documentation-only companion;
- a placeholder awaiting source recovery;
- a completed validated project.

## Historical archive limitation

The final master-publication build did not have every historical companion-project source archive available. The repository therefore preserves the complete numbered structure without inventing missing code.

When source is recovered:

1. place it only in the matching numbered folder;
2. document runtime/toolchain prerequisites;
3. remove secrets and generated build outputs;
4. add or repair tests;
5. run `python scripts/validate_all.py`;
6. commit recovery and validation as separate meaningful changes when practical.

## Reconstructed publication parts

The publication master had to reconstruct Parts 48, 61, and 95 because their original publication binaries were unavailable in the final archive. Companion code for those parts should likewise be treated as missing unless genuine historical source is recovered or a new replacement companion project is intentionally authored and clearly labeled.

## Integrity principle

Repository completeness means **accurate status and reproducible source**, not simply filling every folder with invented files.
