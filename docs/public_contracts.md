# Public Contracts – Stable Interfaces

## 1. Purpose

This document defines what is considered a **public, stable contract** of the platform and what is **internal and volatile**.

Public Contracts are the **only parts allowed to be depended on** by external systems.
They are versioned, protected, and backward-compatible.

---

## 2. Definition of Public Contract

A Public Contract is any interface that:

- Is exposed outside the Core
- Is consumed by API layers, SDK consumers, or Plugins
- Must remain stable across Core refactors

Breaking a Public Contract is considered a **platform-breaking change**.

---

## 3. What IS Public (Allowed to Depend On)

### 3.1 SDK Public Surface (Primary Contract)

The following are **public and stable**:

- SDK entry methods (engine / client methods)
- SDK-level DTOs
- SDK-level exceptions
- SDK configuration objects

These form the **official API of the platform**.

---

### 3.2 Domain Concepts (Read-Only Semantics)

- Business terms and invariants (conceptual only)
- Domain language used in DTO naming

❌ Domain entities themselves are NOT public.

---

## 4. What is NOT Public (Internal Only)

The following must be treated as **strictly internal**:

- Core Domain Entities
- Application Use Cases
- Repositories
- Database schemas
- Internal DTOs
- Validation rules
- Business logic flows

Any dependency on these is a violation.

---

## 5. Contract Stability Rules

- Public Contracts must be:
  - Explicit
  - Documented
  - Versioned

- Internal code may change freely

- Refactoring Core must never break SDK consumers

SDK absorbs all change impact.

---

## 6. Versioning Strategy

- SDK versions represent platform versions
- Core has no external versioning guarantee
- Breaking changes require:
  - New SDK major version
  - Explicit migration path

---

## 7. Change Classification

### Safe Changes (Allowed Anytime)

- Internal refactors
- Performance improvements
- New use cases
- New internal entities

---

### Breaking Changes (Restricted)

- Modifying SDK method signatures
- Removing SDK DTO fields
- Changing exception contracts

These require version bump.

---

## 8. Plugin Compatibility Rule

Plugins depend ONLY on:

- SDK Public Contracts

Plugins must remain compatible across Core updates.

---

## 9. Enforcement

This contract will be enforced via:

- Module boundaries
- Import rules
- Code reviews
- Automated checks (later phases)

---

## 10. Compliance Statement

Any code that bypasses Public Contracts is:

> ❌ Architecturally invalid

No exception.
