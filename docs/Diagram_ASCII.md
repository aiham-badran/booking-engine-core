┌──────────────────────────────────────────────┐
│ Client Applications │
│ │
│ Mobile Apps (Flutter / RN) │
│ Web Apps │
│ Backend APIs │
└───────────────────────▲──────────────────────┘
│
│ Calls Use Cases
│
┌───────────────────────┴──────────────────────┐
│ Use Cases │
│ │
│ CreateBooking │
│ CancelBooking │
│ RescheduleBooking │
│ │
│ - Authorization (optional) │
│ - Trigger Extensions (Hooks) │
└───────────────────────▲──────────────────────┘
│
│ Orchestrates
│
┌───────────────────────┴──────────────────────┐
│ Domain │
│ │
│ Entities: │
│ - Booking │
│ - Context │
│ │
│ Domain Services: │
│ - BookingRulesService │
│ │
│ Policies: │
│ - BookingPolicy │
└───────────────────────▲──────────────────────┘
│
│
┌───────────────┴───────────────┐
│ │
┌───────┴────────┐ ┌───────┴────────┐
│ Repositories │ │ Extensions │
│ │ │ (Hooks) │
│ BookingRepo │ │ Before / After│
│ UserRepo │ │ Per Context │
└────────────────┘ └────────────────┘
