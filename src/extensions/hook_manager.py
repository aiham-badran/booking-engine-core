class HookManager:
    def __init__(self):
        # structure:
        # {
        #   action: {
        #       context_id: {
        #           "before": [callables],
        #           "after": [callables]
        #       }
        #   }
        # }
        self._hooks = {}

    def register_before(self, action: str, context_id: str, hook):
        self._register(action, context_id, "before", hook)

    def register_after(self, action: str, context_id: str, hook):
        self._register(action, context_id, "after", hook)

    def _register(self, action, context_id, timing, hook):
        self._hooks.setdefault(action, {})
        self._hooks[action].setdefault(context_id, {"before": [], "after": []})
        self._hooks[action][context_id][timing].append(hook)

    def run_before(self, action: str, context_id: str, payload):
        for hook in self._get_hooks(action, context_id, "before"):
            hook(context_id, payload)

    def run_after(self, action: str, context_id: str, payload):
        for hook in self._get_hooks(action, context_id, "after"):
            hook(context_id, payload)

    def _get_hooks(self, action, context_id, timing):
        return (
            self._hooks
                .get(action, {})
                .get(context_id, {})
                .get(timing, [])
        )
