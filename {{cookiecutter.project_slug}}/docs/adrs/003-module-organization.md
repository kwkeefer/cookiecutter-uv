# ADR-003: Module Organization

**Status**: Accepted
**Date**: {% now 'local', '%Y-%m-%d' %}

## Context
Need a simple, scalable structure for organizing code.

## Decision
Start with a minimal structure:
- `core/` - Business logic and main functionality
- `utils/` - Shared helpers (optional, add when needed)

Add specialized modules (`api/`, `db/`, etc.) as the project grows.

## Consequences
- ✅ Simple starting point
- ✅ No empty placeholder directories
- ✅ Easy to extend when needed
- ✅ `utils/` stays dependency-free (no app imports)
