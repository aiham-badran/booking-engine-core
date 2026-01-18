class FakePluginManager:
    def __init__(self):
        self.events = []

    def dispatch(self, event):
        self.events.append(event)
