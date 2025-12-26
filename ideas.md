# Ideas (Out of V1 Scope)

- Advanced rule engine
- Extensions marketplace
- SaaS management layer

# Ideas & Improvements (Post-V1)

This file contains approved improvement ideas that are intentionally
excluded from V1 to preserve simplicity and architectural clarity.

---

## 1. Stronger Type Hints Across Core Modules

### Description

Add explicit type hints to all public classes and methods across the core modules.

### Why

- Improves readability and maintainability
- Enables static analysis tools (mypy, pyright)
- Reduces misuse of core APIs by developers

### When

- After V1 stabilization
- Before inviting external contributors

---

## 2. Context as a Strong Value Object

### Description

Enhance the Context entity with:

- **repr** for debugging
- **eq** for identity comparison

### Why

- Improves debugging and logging
- Makes Context comparisons explicit and safe
- No impact on business logic

### When

- Early V2
- Before adding more Context-dependent logic

---

## 3. Duplicate Context Registration Protection

### Description

Prevent registering two Contexts with the same identifier in ContextRegistry.

### Why

- Avoids silent overwrites
- Makes system behavior explicit
- Improves error visibility for developers

### When

- V2
- When Context creation becomes dynamic or user-driven

---

## 4. Domain-Specific Context Exceptions

### Description

Introduce custom exceptions such as:

- ContextNotFoundError
- ContextAlreadyExistsError

### Why

- Clearer error semantics
- Easier error handling for integrators
- Improves API expressiveness

### When

- V2
- Before public API exposure

---

## 5. Explicit Context Configuration Object

### Description

Add a dedicated configuration object attached to each Context
to store non-core metadata and behavior flags.

### Why

- Keeps Context entity clean
- Enables future per-context customization
- Prevents bloating the Context class

### When

- After Core Request Flow is stable
- Before adding advanced features (SaaS, analytics)
