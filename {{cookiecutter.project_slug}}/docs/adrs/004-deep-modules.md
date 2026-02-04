# ADR-004: Prefer Deep Modules

**Status**: Accepted
**Date**: {% now 'local', '%Y-%m-%d' %}
**Reference**: https://github.com/zakirullin/cognitive-load

## Context
Many small, shallow modules increase cognitive load through excessive file navigation and mental context switching.

## Decision
Create "deep" modules with simple public interfaces and substantial private implementation. Consolidate related functionality into cohesive units.

## Example
```python
# Avoid: Many shallow modules
# user_validator.py (30 lines)
# user_serializer.py (40 lines)
# user_repository.py (50 lines)
# user_service.py (20 lines just orchestrating)

# Prefer: One deep module
# user.py (140 lines)
class UserService:
    """Simple public interface"""
    def create_user(self, data: UserData) -> User: ...
    def get_user(self, id: str) -> User: ...

    # Private implementation
    def _validate(self, data): ...
    def _serialize(self, user): ...
    def _persist(self, user): ...
```

## Guidelines
- Target 100-500 lines per module for complex functionality
- Public API should be small relative to implementation
- Group by domain concept, not technical layer

## Consequences
- ✅ Less file navigation
- ✅ Complete context in one place
- ✅ Easier to understand domain concepts
- ⚠️ Larger files (mitigate with clear organization)
