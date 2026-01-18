# Core Boundaries – Booking Engine Core

## الهدف من هذه الوثيقة

هذه الوثيقة تُعرّف الحدود الصارمة (Non‑Negotiable Boundaries) لنواة **Booking Engine Core**.

الغرض منها:

- حماية النواة من التلوّث التقني
- ضمان قابلية التوسعة طويلة المدى
- منع كسر المعمارية عند إضافة ميزات أو Plugins

أي كود داخل المشروع **يجب أن يلتزم بهذه الوثيقة**. أي مخالفة تُعد خطأ معماريًا.

---

## ما هو Booking Engine Core؟

Booking Engine Core هو:

- نواة منطقية (Business Core)
- مستقلة تمامًا عن أي تقنية تشغيل
- لا تمثل تطبيقًا جاهزًا
- لا تتعامل مع العالم الخارجي مباشرة

النواة ليست:

- API
- Backend App
- SaaS
- Framework

---

## What Core DOES (ما الذي تفعله النواة)

النواة مسؤولة فقط عن **منطق الحجز العام**، وتشمل:

### 1. Business Rules

- قواعد إنشاء الحجز
- قواعد تعديل وإلغاء الحجز
- سياسات الحجز (Policies)
- منع التعارضات

### 2. Booking Lifecycle

- إدارة دورة حياة الحجز (Create / Update / Cancel)
- التحقق من صحة الانتقالات المنطقية

### 3. Availability Logic

- حساب الأوقات المتاحة
- التحقق من التوفر
- احترام إعدادات العمل

### 4. Multi‑Tenancy Logic

- عزل البيانات منطقيًا حسب المؤسسة
- تمرير `organization_id` في كل Use Case

### 5. Domain Modeling

- Entities
- Value Objects
- Domain Policies

### 6. Extension Points (Conceptual)

- تعريف Events
- تعريف Hooks
- بدون تنفيذ Plugins داخل النواة

---

## What Core NEVER Does (محظورات مطلقة)

النواة **ممنوع** أن تحتوي أو تعتمد على أي مما يلي:

### ❌ HTTP / API

- Controllers
- Routers
- Request / Response

### ❌ Authentication / Authorization

- JWT
- Sessions
- Roles enforcement

### ❌ Database Implementation

- ORM
- SQL / NoSQL Queries
- Drivers

### ❌ External Services

- Email
- SMS
- Payment
- Webhooks

### ❌ Frameworks

- FastAPI
- Django
- Flask
- Any Web Framework

### ❌ Runtime / Environment Concerns

- Config files
- ENV variables
- Deployment logic

📌 أي ظهور لما سبق داخل `core/` = **خطأ معماري**

---

## حدود الطبقات (Layer Boundaries)

### Domain Layer

**مسموح:**

- Entities
- Value Objects
- Policies

**ممنوع:**

- IO
- DB
- External Calls

---

### Application Layer

**مسموح:**

- Use Cases
- Application Services
- Ports (Interfaces)

**ممنوع:**

- DB implementation
- HTTP
- Framework code

---

### Infrastructure Layer

**مسموح:**

- Adapters
- Implementations للـ Ports

**ممنوع:**

- Business Logic
- Domain Rules

---

### SDK Layer

**الدور:**

- Facade رسمي للنواة
- Gatekeeper
- Input Validation
- Enforcing correct flow

**ممنوع:**

- Business Logic داخلي
- تجاوز Core rules

---

### Plugins

**مسموح:**

- الاشتراك في Events
- التفاعل عبر Hooks

**ممنوع:**

- تعديل Core state مباشرة
- كسر invariants
- الوصول للبنية الداخلية

---

## قاعدة ذهبية

> Core must be usable without knowing **how** it will be used.

أي كود يحتاج معرفة:

- من يستعمله
- أو كيف يُشغّل
- أو أين يُنشر

❌ لا مكان له داخل النواة.

---

## التزام المساهمين

- أي Pull Request يخالف هذه الوثيقة يُرفض
- أي Feature جديدة تُقاس على هذه الحدود
- Plugins و SDK تبقى خارج Core دائمًا

---

## الخلاصة

هذه الوثيقة هي **العقد المعماري** للمشروع.

- النواة = منطق فقط
- كل شيء آخر = قابل للتغيير

كسر هذه الحدود يعني كسر المشروع على المدى الطويل.
