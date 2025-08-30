# ADR-004: Makefile as Primary Developer Interface

**Status**: Accepted  
**Date**: {% now 'local', '%Y-%m-%d' %}  

## Context
Developers need a consistent interface for common tasks regardless of their familiarity with Python tooling.

## Decision
Provide a Makefile with all common development tasks.

## Consequences
- ✅ Universal interface across different environments
- ✅ Self-documenting with help target
- ✅ Composable commands
- ⚠️ Requires make to be installed (usually available)