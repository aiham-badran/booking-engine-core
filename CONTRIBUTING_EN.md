# Contributing Guide

**Booking Engine Core**

Thank you for your interest in contributing to **Booking Engine Core** 🎉
This project is an **open-source domain core**, designed to be framework-agnostic, extensible, and business-logic focused.

Before contributing, please read this guide carefully to ensure alignment with the project's philosophy.

---

## 🎯 Project Philosophy

This repository is a **Core Engine**, not a full application.

### Core Principles

-   **Domain-first design**
-   **No framework dependencies**
-   **No infrastructure concerns**
-   **Explicit business rules**
-   **Extension over modification**
-   **Simplicity over feature richness**

If a change breaks any of these principles, it is unlikely to be accepted.

---

## ✅ What Contributions Are Welcome

### ✔ Allowed & Encouraged

-   Bug fixes
-   Improvements to existing domain logic
-   Refactoring that improves clarity without changing behavior
-   Test coverage improvements
-   Documentation improvements
-   Performance optimizations within the domain
-   Small, well-scoped enhancements aligned with the roadmap

### ⚠ Conditionally Accepted

-   New features **only if listed in the ROADMAP**
-   Enhancements that do not introduce:

    -   Framework coupling
    -   Infrastructure logic
    -   SaaS-specific behavior

---

## ❌ What Will NOT Be Accepted

The following are **explicitly out of scope**:

-   REST / GraphQL APIs
-   Web frameworks (FastAPI, Django, Flask, etc.)
-   Authentication / Authorization providers
-   Database implementations (SQL, NoSQL, ORM)
-   UI / Frontend code
-   SaaS billing, subscriptions, dashboards
-   Background workers or queues

These belong to **applications built on top of the core**, not inside it.

---

## 🧩 Architectural Boundaries

Contributions must respect the existing layers:

```
Domain (Entities, Value Objects)
Use Cases (Application logic)
Policies (Configuration & rules)
Extensions (Hooks)
Repositories (Interfaces or in-memory only)
```

🚫 Do not bypass domain rules
🚫 Do not add stateful services
🚫 Do not leak infrastructure concerns into domain logic

---

## 🧪 Testing Requirements

All contributions **must include tests**.

### Test Guidelines

-   Tests must be deterministic
-   Prefer domain-level tests
-   Avoid mocking internal domain behavior
-   New behavior → new tests
-   Bug fix → regression test required

Pull Requests without tests will not be merged.

---

## 🧱 Coding Standards

-   Python ≥ 3.10
-   Explicit and readable code
-   Clear naming (domain language preferred)
-   Avoid premature abstraction
-   Avoid hidden side effects
-   Stateless domain services only

Type hints are encouraged and may become mandatory in future versions.

---

## 🔌 Extensions & Hooks

When contributing to the extension system:

-   Hooks must be isolated
-   Errors must not break the core flow
-   No direct dependency between extensions
-   Hooks must not mutate core entities unexpectedly

---

## 🗺️ Roadmap Alignment

Before proposing a feature:

1. Check `ROADMAP.md`
2. If not listed → open a discussion issue first
3. Large changes require prior approval

Unplanned features may be rejected even if well implemented.

---

## 📦 Commit & PR Guidelines

### Commits

-   Clear, descriptive messages
-   One logical change per commit

Example:

```
Improve booking conflict detection logic
```

### Pull Requests

-   Describe **why** the change is needed
-   Reference related issues
-   Explain impact on existing behavior
-   Mention if behavior is unchanged

---

## 🤝 Community Expectations

-   Be respectful
-   Be clear and constructive
-   Prefer discussion before large changes
-   Quality > speed

This project values **engineering discipline** over fast feature growth.

---

## 🧠 Final Note

> This core is intentionally small.
> Its strength comes from clarity, not size.

If you are unsure whether a contribution fits, open an issue and discuss it first.

Thank you for helping make this core better 🚀
