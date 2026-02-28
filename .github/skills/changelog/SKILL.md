---
name: changelog
description: Add or update the missing CHANGELOG.md entry for the current OpenTelemetry Python Contrib pull request.
---

# OpenTelemetry Python Contrib — Changelog Skill

Use this skill when a pull request in `open-telemetry/opentelemetry-python-contrib` is missing a changelog entry or the user asks to fix git conflicts with `./CHANGELOG.md`.

Your job is to **only edit the root `./CHANGELOG.md` file** and add or update the changelog entry for the current PR.

## Primary goal

Given the current pull request diff, title, commit message, and/or PR description:

- determine whether the PR needs a changelog entry
- determine the correct changelog section
- add a concise entry in the correct format
- avoid touching any file other than `./CHANGELOG.md`

## Scope rules

- Only modify `./CHANGELOG.md`
- Do not edit any other file
- Do not run tests
- Do not run lint
- Do not search CI jobs
- Do not investigate unrelated failures
- Do not make code changes
- Do not reformat unrelated parts of the changelog
- Do not reorder unrelated entries unless required to resolve a merge conflict

## What to inspect

Use the PR title, description, and code diff to infer:

- which package(s) changed
- whether the change is user-visible
- whether the change belongs in:
  - `### Added`
  - `### Fixed`
  - `### Breaking changes`

If the change is breaking and the repository uses a dedicated breaking-change section, place it there. Otherwise, place it in the most accurate normal section and clearly mention the breaking behavior in the text.

## When to add an entry

Add a changelog entry when the PR introduces a user-visible change, including:

- new instrumentation behavior
- new package support
- bug fixes
- behavior changes
- deprecations
- removals
- compatibility updates that matter to users
- meaningful documentation-visible behavior changes

Do **not** add an entry for purely internal changes unless the repository convention clearly requires it, such as:

- refactors with no user-visible impact
- test-only changes
- CI-only changes
- tooling-only changes
- formatting-only changes

If uncertain, prefer adding an entry only when there is a clear user-facing impact.

## Placement rules

- Add the new entry under the appropriate section in the **current unreleased version** at the top of `CHANGELOG.md`
- Do not create a new release section unless explicitly required
- Do not place the entry under an older released version
- Preserve existing formatting and spacing
- Keep entries grouped with similar package changes when possible

## Entry style rules

- Each entry must start with `- `
- Keep wording concise and user-facing
- Mention the affected package name(s) when relevant, using backticks
- Use present-tense or imperative changelog style consistently with the existing file
- Do not include implementation details unless needed for clarity
- One logical change per bullet
- If a PR affects multiple user-visible packages in the same way, they may be grouped into one entry

## Required format

Format entries exactly like this:

- `- <entry text>`
- `  ([#<PR_NUMBER>](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/<PR_NUMBER>))`

Example:

- Add Python 3.14 support
  ([#1234](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/1234))

Package-specific example:

- `opentelemetry-instrumentation-requests`: Fix duplicate span creation on retried requests
  ([#1234](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/1234))

## Update rules

If an entry for the current PR already exists:

- update it instead of adding a duplicate
- improve clarity if the existing wording is inaccurate or incomplete
- keep the PR link correct
- do not duplicate the same PR number in multiple equivalent entries unless the PR truly needs multiple separate bullets

## Conflict resolution rules

If `CHANGELOG.md` has merge conflict markers:

- resolve conflicts only inside `CHANGELOG.md`
- preserve all valid existing entries
- keep the current PR entry exactly once
- remove conflict markers
- maintain correct section placement and formatting

## Output expectations

After editing:

- the only modified file should be `./CHANGELOG.md`
- the changelog should remain valid markdown
- the new or updated entry should match the repository’s existing style

## Decision heuristic

When generating the text:
1. Identify the user-visible outcome
2. Name the affected package if helpful
3. Describe the change in one concise line
4. Append the PR reference on the next line

Prefer this style:

- `package`: user-visible change

Avoid:
- vague wording
- internal implementation details
- repeating the PR title verbatim if it is too technical or unclear

## Examples

### Added
- `opentelemetry-instrumentation-botocore`: Add support for instrumenting `aiobotocore`
  ([#4049](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4049))

### Fixed
- `opentelemetry-instrumentation-flask`: Fix exemplars generation for HTTP server duration metrics
  ([#3912](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/3912))

### Changed
- `opentelemetry-instrumentation-logging`: Move the SDK `LoggingHandler` into the instrumentation package
  ([#4210](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/4210))

### Removed
- `opentelemetry-instrumentation-xyz`: Remove deprecated legacy hook support
  ([#1234](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/1234))
