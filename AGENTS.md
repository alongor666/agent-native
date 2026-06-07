# Repository Guidelines

## Project Structure & Module Organization

This repository maintains the Agent-Native Specification (ANS), a document-first specification project. `SPEC.md` is the normative source of truth. `CHECKLIST.md` and `ASSESSMENT.md` are derived validation and self-assessment artifacts and must stay aligned with `SPEC.md`. `ans.json` is the machine-readable contract consumed by agents. `GOVERNANCE.md` defines versioning, release, and maintenance rules; `CHANGELOG.md`, `changelog.json`, and `compatibility.json` record human- and machine-readable release history. `STATUS.md` stores current state, decisions, and open work. Tooling lives in `tools/`, currently `tools/ans-lint.py`.

## Build, Test, and Development Commands

- `python3 tools/ans-lint.py`: validates `ans.json` against `SPEC.md`, `CHECKLIST.md`, `ASSESSMENT.md`, changelog, and compatibility data. Exit `0` means the repository is consistent.
- `python3 tools/ans-lint.py --json`: emits only the machine-readable JSON report, useful for agent workflows and CI-style checks.
- `git show v0.1.0:SPEC.md`: inspects an immutable tagged specification snapshot.

There is no package install, build step, or runtime server for this repository.

## Coding Style & Naming Conventions

Keep documentation concise, normative, and structured. Use RFC 2119 keywords (`MUST`, `SHOULD`, `MAY`) only when changing conformance requirements. Preserve stable clause identifiers such as `A1.3` in derived artifacts. JSON files use UTF-8, two-space indentation, explicit fields, and stable ordering where practical. Python tooling should remain zero-dependency, Python 3 compatible, and readable over clever.

## Testing Guidelines

Run `python3 tools/ans-lint.py` after any change to `SPEC.md`, `CHECKLIST.md`, `ASSESSMENT.md`, `ans.json`, `changelog.json`, or `compatibility.json`. For normative changes, manually confirm that all derived files were updated and that `STATUS.md` records the decision.

## Commit & Pull Request Guidelines

Existing commits use short type prefixes, for example `init:` and `release:` followed by a clear Chinese summary. Keep commits scoped to one logical change. Pull requests should describe the normative or non-normative impact, list changed artifacts, include the `ans-lint` result, and link relevant decisions in `STATUS.md`. Do not publish releases without following `GOVERNANCE.md`.

## Agent-Specific Instructions

New agent sessions should read `STATUS.md`, then `SPEC.md`, then `CHECKLIST.md` before editing. Treat `SPEC.md` as the single source of truth, avoid creating duplicate guidance files, and prefer machine-readable updates when adding durable project facts.
