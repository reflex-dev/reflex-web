# Reflex Web - Development Guide

## Running the App

```bash
# Install dependencies
uv sync

# Run development server
reflex run

# Open browser at http://localhost:3000
```

## Testing

```bash
# Run unit tests
pytest

# Run integration tests (requires Playwright)
pytest tests/test_*.py

# Run pre-commit checks
pre-commit run --all-files

# Run linting
ruff check .

# Run formatting
ruff format .
```

## PR Submission Guidelines

### Before Submitting

1. **Run tests**: Ensure all tests pass locally
2. **Run linting**: `ruff check .` should pass with no errors
3. **Run formatting**: `ruff format .` to auto-format code
4. **Test locally**: Run `reflex run` and verify your changes work

### Commit Message Format

```
Brief description of change (50 chars or less)

Longer explanation if needed. Describe what changed and why.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

### PR Title and Description

- **Title**: Clear, concise description (e.g., "Fix mobile navigation menu", "Add dark mode support to docs")
- **Description**: Include:
  - Summary of changes
  - Why the change was needed
  - Test plan or steps to verify
  - Any relevant issue numbers

### Example PR Description

```markdown
## Summary
- Fixed rendering issue on the Base Vars documentation page
- Updated component styling for better mobile responsiveness

## Test Plan
- [x] Verified page renders correctly on desktop
- [x] Tested on mobile devices (iOS Safari, Chrome Android)
- [x] All unit tests pass
- [x] Linting passes

🤖 Generated with [Claude Code](https://claude.com/claude-code)
```

### CI Requirements

Your PR must pass:
- Unit tests
- Integration tests
- Linting checks (Ruff)
- Spell checking (Codespell)

### Getting PR Approved

- PRs are reviewed by the Reflex team
- Address any review comments
- Keep PRs focused on a single change when possible
- Add screenshots for UI changes
