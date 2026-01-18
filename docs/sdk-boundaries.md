# SDK Boundaries (Facade / Gatekeeper)

## 1. Purpose

The SDK is the **only official entry point** to interact with the Core.
It acts as a **Facade + Gatekeeper** that protects the Core from misuse and enforces architectural rules.

Any consumer (API, SaaS, CLI, Plugin, External App) **must** communicate with the Core exclusively through the SDK.

---

## 2. What the SDK DOES

The SDK is responsible for:

1. Acting as the **single entry point** to the Core
2. Input validation (structure, required fields, basic sanity checks)
3. Mapping external input to **Core DTOs**
4. Enforcing **Organization / Tenant context**
5. Normalizing and exposing **controlled exceptions**
6. Orchestrating Core use cases safely
7. Providing a stable interface for external integrations

---

## 3. What the SDK NEVER does

The SDK must **never**:

- Contain business rules or decision-making logic
- Modify or override Core behavior
- Access the database directly
- Perform authentication or authorization
- Call external services
- Expose internal Core structures (Entities, Repositories, Use Cases)

---

## 4. Forbidden Access Rules

The following access patterns are **strictly forbidden**:

- Importing Core Use Cases outside the SDK
- Instantiating Domain Entities from API / App layers
- Calling Application Services directly
- Passing raw, unvalidated input into the Core

The SDK is the **only allowed bridge**.

---

## 5. Allowed Dependency Direction

```
External App / API / Plugin
            ↓
           SDK
            ↓
           Core
```

Reverse or lateral access is not allowed.

---

## 6. Exception Handling Contract

- Core throws **domain-level exceptions** only
- SDK catches and translates them into:
  - SDK-level exceptions
  - Consumer-friendly error messages

Consumers must **never** depend on Core exception types.

---

## 7. DTO Boundary Rules

- SDK defines the public DTOs
- Core defines internal DTOs if needed
- Mapping between them happens **inside the SDK only**

No DTO defined in Core is exposed externally.

---

## 8. Stability & Versioning

- SDK is the versioned surface of the platform
- Core can evolve internally without breaking consumers
- Breaking changes are managed at the SDK level only

---

## 9. Compliance Rule

Any feature, plugin, or integration that bypasses the SDK is considered:

> ❌ Architecturally invalid

No exception.

---

## 10. Enforcement (Next Phases)

This document will be enforced through:

- Import restrictions
- Access modifiers
- Static analysis
- Runtime guards (where needed)

Implementation comes **after** architectural approval.
