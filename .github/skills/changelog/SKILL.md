---
name: changelog
description: A skill for generating changelog entries for OpenTelemetry Python Contrib packages.
---

# OpenTelemetry Python Contrib — Changelog Skill

This skill generates changelog entries for OpenTelemetry Python Contrib packages based on commit messages and pull request descriptions. It follows the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format and categorizes changes into sections: Added, Fixed or Breaking changes. Just Add/Update/Remove the entry from the ./CHANGELOG.md file at the root of the repository.

# Important

- Do not run any test or lint
- Do not run any task other than just update the CHANGELOG.md file accordingly to the request
- Do not search for failures in jobs

## Usage

- You can also include multiple changes in a single entry
- Each change should be listed on a new line with a leading dash
- Include the PR number and link to the PR for reference
- Fix any git conflicts in the changelog file if they arise during merges

A changelog entry format should look like this:

```
- Add Python 3.14 support
  ([#<PR_NUMBER>](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/<PR_NUMBER>))
```



