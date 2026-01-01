sequenceDiagram

    participant Client
    participant UseCase
    participant Policy
    participant Rules
    participant Repo
    participant Hooks

    Client->>UseCase: create_booking()
    UseCase->>Policy: can_user_book?
    Policy-->>UseCase: allowed

    UseCase->>Repo: load existing bookings
    Repo-->>UseCase: bookings

    UseCase->>Rules: can_book()
    Rules-->>UseCase: approved

    UseCase->>Hooks: before_create
    Hooks-->>UseCase: ok

    UseCase->>Repo: save booking
    UseCase->>Hooks: after_create

    UseCase-->>Client: Booking Created
