flowchart TB

    Client[Client Applications<br/>Mobile • Web • Backend API]

    Client --> UC[Use Cases<br/>Create / Cancel / Reschedule]

    UC --> Auth[Authorization<br/>(Optional)]
    UC --> Hooks[Extensions Hooks<br/>Before / After]

    UC --> Domain[Domain Layer]

    Domain --> Booking[Entity: Booking]
    Domain --> Context[Value Object: Context]
    Domain --> Rules[Domain Service:<br/>BookingRulesService]
    Domain --> Policy[Policies & Configuration]

    UC --> Repo[Repositories]

    Repo --> BookingRepo[BookingRepository]
    Repo --> UserRepo[UserRepository]

    Hooks --> Ext1[Extension A]
    Hooks --> Ext2[Extension B]

    subgraph Core Engine
        UC
        Domain
        Hooks
        Repo
    end
