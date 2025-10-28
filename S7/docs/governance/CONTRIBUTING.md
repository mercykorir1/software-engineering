# Contributing Guidelines

## Branch naming
Use short, consistent names:
- `feature/<ticket>-short-description`
- `fix/<ticket>-short-description`
- `docs/<ticket>-short-description`

Examples:
- `feature/12-add-login-button`
- `fix/34-fix-crash`
- `docs/56-update-readme`

## Commit style
- Use imperative tense: `Add X`, `Fix Y`
- Reference issue number: `Fix #45: correct validation`
- Keep commits small and focused.

## Pull request policy
All changes to `main` must come through a Pull Request (PR):
- Linked issue required
- CI must be green
- 1 review approval (CODEOWNERS)
- No secrets or credentials in code

## Code style
Follow project linter rules. Run locally before pushing:
```bash
npm run lint
npm test
