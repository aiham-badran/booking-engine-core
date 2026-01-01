# 🗺️ Roadmap – Booking Engine Core

This roadmap describes the planned evolution of **Booking Engine Core** as an open-source, framework-agnostic backend engine.

The roadmap intentionally focuses on **core domain quality, extensibility, and developer experience**, while keeping SaaS, UI, and infrastructure concerns out of scope.

---

## ✅ Version 1.0 – Core Engine (Released)

**Status:** ✅ Stable
**Tag:** `v1.0.0-core`

### Scope

The first stable release delivers a complete, extensible booking core engine.

### Features

-   Booking domain model with explicit lifecycle
-   Core use cases:

    -   Create booking
    -   Cancel booking
    -   Reschedule booking

-   Booking rules:

    -   Availability validation
    -   Conflict detection

-   Configurable booking policies
-   Context-aware hooks (before / after use cases)
-   Optional authorization checks
-   In-memory repositories
-   Full domain-level test coverage

### Explicitly Out of Scope

-   API layer
-   Persistence / database adapters
-   Authentication providers
-   UI or dashboards
-   SaaS or billing logic

---

## 🟢 Version 1.1 – Stabilization & Developer Experience

**Goal:** Improve safety, clarity, and usability without changing core behavior.

### Planned Improvements

-   Stronger type hints for all public APIs
-   Clearer public method boundaries
-   Improved naming consistency across modules
-   Documentation polish and examples
-   Minor internal refactors (no breaking changes)

---

## 🟡 Version 2.0 – Domain Maturity

**Goal:** Strengthen domain modeling and error semantics.

### Planned Improvements

-   Context as a strong value object:

    -   `__repr__`
    -   `__eq__`

-   Domain-specific exceptions:

    -   ContextNotFoundError
    -   ContextAlreadyExistsError
    -   BookingRuleViolationError

-   Protection against duplicate context registration
-   Booking status migration from string → enum (backward compatible)

---

## 🟡 Version 2.1 – Configurability & Safety

**Goal:** Improve configurability while keeping the core clean.

### Planned Improvements

-   Explicit ContextConfiguration object
-   PolicyResolver abstraction
-   Optional policy caching per context
-   Repository interface extensions:

    -   `list_by_context_and_service`

---

## 🟡 Version 2.2 – Extensions & Hooks Enhancements

**Goal:** Improve extension robustness without increasing complexity.

### Planned Improvements

-   Error isolation between hooks
-   Optional hook execution priorities
-   Improved extensions documentation
-   Safer hook execution model

---

## 🟡 Version 2.3 – Authorization & Access Control

**Goal:** Enable richer authorization without coupling to auth providers.

### Planned Improvements

-   RoleRepository abstraction
-   Permission groups
-   Policy-based authorization per use case
-   Hook-based permission extensions

---

## 🟡 Version 2.4 – Testing & Reliability

**Goal:** Increase confidence under edge cases.

### Planned Improvements

-   Property-based testing
-   Performance-related edge case tests
-   Stress scenarios for booking conflicts

---

## 🔵 Future Considerations (Not Scheduled)

These ideas are acknowledged but not scheduled to preserve focus:

-   Application layer / dependency injection
-   Async hooks execution
-   Observability (metrics, tracing)
-   SDKs (Python / JavaScript)
-   SaaS management features

---

## 🚫 Non-Goals

The following will **never** be part of the core:

-   UI components
-   API frameworks
-   Authentication implementations
-   Billing systems
-   SaaS dashboards

These concerns belong to higher layers built **on top of** the core.

---

## 📌 Roadmap Philosophy

> Build a strong, simple core.
> Optimize for correctness and extensibility.
> Defer complexity until it is unavoidable.

---

### Contributions

Bug reports and focused improvements are welcome.
Large feature requests should align with the roadmap and core philosophy.
