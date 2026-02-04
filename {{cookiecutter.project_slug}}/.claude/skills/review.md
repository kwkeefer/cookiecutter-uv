{%- if cookiecutter.use_claude_agents == 'yes' -%}
---
description: Review code changes for quality, security, and adherence to project standards
---

# Code Review

Review the current changes following project standards.

## Process

1. **Run checks first**:
   ```bash
   make lint && make typecheck && make test
   ```

2. **Review against standards**:
   - Check CLAUDE.md for project conventions
   - Verify utils/ doesn't import from other app modules
   - Ensure type hints on all functions
   - Confirm tests mirror source structure with proper markers

3. **Check test coverage**:
   ```bash
   make test-cov
   ```

## Output Format

Categorize findings:

### 🔴 Critical (must fix)
- Security vulnerabilities
- Broken functionality
- Missing error handling for external inputs

### 🟡 Should Fix
- Missing type hints
- Tests without markers
- Module boundary violations

### 🟢 Consider
- Code clarity improvements
- Additional test cases
- Documentation updates

## Review Checklist

- [ ] All functions have type hints
- [ ] Tests use `@pytest.mark.unit` or `@pytest.mark.integration`
- [ ] No hardcoded secrets or credentials
- [ ] Error handling uses custom exceptions
- [ ] New modules follow project structure
{%- endif %}
