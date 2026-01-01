## ✅ README.md (English – Landing Page)

يمكنك استبدال محتوى `README.md` بالكامل بهذا النص:

---

# 🧠 Booking Engine Core

> An open-source, framework-agnostic **domain core** for appointment booking systems
> Clean architecture • Explicit business rules • Built for extensibility

---

## 📌 What is this project?

**Booking Engine Core** is a **business-logic engine** for appointment booking.

It is designed to be the **foundation** for building:

-   Backend applications
-   Mobile-backed systems (Flutter, React Native, etc.)
-   Custom booking platforms
-   SaaS products (built _on top_ of the core)

❗ This is **not** a ready-made application.
It is a **clean, reusable core** that enforces correct booking behavior.

---

## 🎯 Why does this exist?

Most booking systems today are:

-   Tightly coupled to frameworks
-   Hard to customize
-   Mixing business logic with APIs and UI
-   Difficult to reuse across projects

### Booking Engine Core solves this by design:

✔ Pure domain logic
✔ No framework dependency
✔ No database assumption
✔ No SaaS assumptions
✔ Extension-friendly architecture

---

## 🧩 What does the core provide?

### ✅ Core Features (V1)

-   Create booking
-   Cancel booking
-   Reschedule booking
-   Availability validation
-   Conflict detection
-   Configurable booking policies
-   Extension hooks (before / after use cases)
-   Context-based isolation (multi-tenant ready)
-   Strong domain-level test coverage

---

## 🏗️ Architecture Overview

The core follows a layered, domain-driven architecture:

```
Client (API / Mobile / Web)
        ↓
     Use Cases
        ↓
      Domain
        ↓
 Repositories & Extensions
```

-   **Domain** → Entities & business rules
-   **Use Cases** → Application orchestration
-   **Policies** → Configurable decisions
-   **Extensions** → Hooks for customization
-   **Repositories** → Storage abstraction

📖 See: `docs/ARCHITECTURE.md`

---

## 🔌 Extensions System

The core supports extensions without modifying its code:

-   Notifications
-   Logging
-   Analytics
-   External integrations
-   Context-specific behavior

Each extension is:

-   Isolated
-   Safe by default
-   Non-breaking to the core flow

---

## 📱 Mobile & Frontend Integration

Mobile apps (Flutter, React Native, etc.) **do not use the core directly**.

Typical flow:

1. Core runs inside a backend service
2. API exposes booking operations
3. Mobile apps consume the API
4. Core guarantees booking correctness

➡️ No duplicated rules
➡️ No client-side booking logic
➡️ Single source of truth

---

## 🚫 What this core does NOT include

This project will **never** include:

-   REST / GraphQL APIs
-   Authentication providers
-   Databases or ORMs
-   Frontend or UI code
-   SaaS billing or dashboards

All of these belong **outside the core**.

---

## 🗺️ Roadmap

-   V1 → Stable core engine ✅
-   V2 → Domain maturity, policies, advanced hooks
-   Future → Evolution without bloat

📌 See: `ROADMAP.md`

---

## 🤝 Contributing

Contributions are welcome **if they respect the core philosophy**.

Please read:

-   `CONTRIBUTING.md`
-   `CONTRIBUTING_EN.md`

---

## 🧠 Philosophy

> Strong core
> Clear boundaries
> Explicit rules
> Deferred complexity

This is not a quick library.
It is a **long-term architectural foundation**.

---

## 📄 License

MIT License
Free for commercial and open-source use.

---

## ⭐ Support the project

-   Star the repository ⭐
-   Share it with other engineers
-   Build something serious on top of it

---

## 📬 Discussions

Use GitHub Issues for:

-   Architecture discussions
-   Design questions
-   Improvement proposals
