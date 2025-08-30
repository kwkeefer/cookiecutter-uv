# ADR-006: Module Organization

**Status**: Proposed  
**Date**: {% now 'local', '%Y-%m-%d' %}  

## Context
Need clear boundaries between different aspects of the application.

## Decision
Organize code into four main modules:
- `core/` - Business logic and domain models
- `api/` - External interfaces (REST, GraphQL, etc.)
- `db/` - Database models and queries
- `utils/` - Shared utilities and helpers

## Consequences
- ✅ Clear separation of concerns
- ✅ Easy to understand project structure
- ✅ Prevents circular dependencies
- ⚠️ May need adjustment based on project needs