# Architecture Overview

**Booking Engine Core**

## 1. مقدمة

**Booking Engine Core** هي نواة منطقية (Domain Core) لنظام حجز مواعيد، مصممة لتكون:

-   مستقلة عن أطر العمل (Framework-agnostic)
-   مستقلة عن البنية التحتية (Infrastructure-agnostic)
-   قابلة للتوسعة دون تعديل الكود الأساسي
-   مناسبة للاستخدام كنواة Open Source أو كأساس لمنصات SaaS

هذه النواة **ليست تطبيقًا جاهزًا**، بل محرك منطق أعمال يُبنى فوقه.

---

## 2. المبادئ المعمارية الأساسية

يعتمد التصميم على المبادئ التالية:

### 2.1 Domain-First Design

منطق الأعمال هو الأساس، وكل شيء آخر يأتي لاحقًا.

### 2.2 Explicit Business Rules

لا توجد قواعد ضمنية أو مخفية.
كل قرار حجز يمر عبر قواعد واضحة ومختبرة.

### 2.3 Stateless Services

جميع الخدمات الدومينية (Domain Services) عديمة الحالة (Stateless).

### 2.4 Extension over Modification

التوسعة تتم عبر Hooks و Policies، وليس بتعديل الكود الأساسي.

### 2.5 No Infrastructure Leakage

لا توجد:

-   قواعد بيانات
-   APIs
-   أطر عمل
-   أنظمة مصادقة

داخل النواة.

---

## 3. النظرة العامة على الطبقات (High-Level View)

```
┌────────────────────────────┐
│        Application          │  ← (خارج النواة)
│   API / Mobile / Web        │
└────────────▲───────────────┘
             │
┌────────────┴───────────────┐
│         Use Cases            │
│  (Create / Cancel / ...)     │
└────────────▲───────────────┘
             │
┌────────────┴───────────────┐
│           Domain             │
│ Entities • Rules • Policies  │
└────────────▲───────────────┘
             │
┌────────────┴───────────────┐
│        Extensions            │
│     Hooks (Before/After)     │
└────────────────────────────┘
```

---

## 4. Domain Layer

### 4.1 Entities

#### Booking

يمثل كيان الحجز ويحتوي على:

-   المعرّفات (booking_id, context_id, service_id)
-   الفترة الزمنية
-   الحالة (status)
-   منطق دورة الحياة (confirm, cancel, reschedule)

> الكيان مسؤول عن صحة حالته الداخلية فقط.

---

### 4.2 Value Objects

#### Context

يمثل السياق (شركة، عيادة، فريق…).

-   معرّف فريد
-   يستخدم لعزل البيانات والقواعد
-   أساس التوسعة المستقبلية

---

## 5. Booking Rules (Domain Services)

### BookingRulesService

خدمة دومينية Stateless مسؤولة عن:

-   التحقق من التوفر
-   منع التعارضات
-   تطبيق قواعد الحجز الخاصة بالسياق والخدمة

#### لماذا Service؟

لأن القواعد:

-   لا تنتمي لكيان واحد
-   تعتمد على بيانات متعددة
-   قابلة للتغيير

---

## 6. Use Cases Layer

تمثل حالات الاستخدام الفعلية للنظام.

### أمثلة:

-   CreateBooking
-   CancelBooking
-   RescheduleBooking

### خصائص Use Cases:

-   تنسّق بين Domain و Repositories
-   تطبق Authorization (إن وجد)
-   تستدعي Hooks
-   لا تحتوي منطق دوميني عميق

---

## 7. Policies & Configuration

### Policies

تمثل قرارات قابلة للإعداد مثل:

-   من يمكنه الإلغاء
-   من يمكنه إعادة الجدولة
-   شروط التعديل

### الهدف

فصل **القرار** عن **التنفيذ**
والسماح بتغيير السلوك بدون تعديل النواة.

---

## 8. Extensions System (Hooks)

### Lifecycle

كل Use Case يوفّر نقاط Hook:

-   Before Action
-   After Action

### خصائص النظام:

-   معزول حسب Context
-   أخطاء الإضافات لا تكسر النواة
-   لا يوجد اعتماد مباشر بين الإضافات

### الاستخدامات المتوقعة:

-   إشعارات
-   Logging
-   Analytics
-   Integrations

---

## 9. Repositories

### الدور

-   تجريد التخزين
-   توفير واجهة واضحة للنواة

### في V1

-   In-memory repositories فقط

### لاحقًا

-   يمكن ربطها بأي:

    -   SQL
    -   NoSQL
    -   API خارجي

بدون تغيير النواة.

---

## 10. ما هو خارج النواة (Out of Scope)

النواة **لن تحتوي أبدًا** على:

-   REST / GraphQL APIs
-   مصادقة المستخدمين
-   واجهات مستخدم
-   SaaS Billing
-   Dashboards

هذه تُبنى في طبقات أعلى.

---

## 11. كيف تُستخدم هذه النواة؟

### 11.1 تطبيق Backend

-   ربط Use Cases بـ API
-   تنفيذ Repositories حقيقية

### 11.2 تطبيقات Mobile (Flutter / React Native)

-   التواصل مع API مبني فوق النواة
-   النواة تضمن منطق الحجز

### 11.3 SaaS Platform

-   كل Tenant = Context
-   Policies + Extensions لكل عميل
-   النواة تبقى ثابتة

---

## 12. قابلية التطور المستقبلية

تم تصميم النواة لدعم:

-   DI / Application Layer لاحقًا
-   Advanced Rule Engine
-   Extensions Marketplace
-   Stronger Type System
-   Performance Optimizations

بدون كسر التوافق.

---

## 13. الخلاصة

> هذه النواة ليست مجرد كود
> بل **أساس معماري قابل للنمو**

القوة هنا ليست في كثرة الميزات
بل في **وضوح الحدود وسلامة التصميم**.
