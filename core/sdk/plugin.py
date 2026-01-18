# core/sdk/plugin.py

class Plugin:
    """
    Base class for all plugins.
    """

    def handle(self, event):
        raise NotImplementedError

# core/sdk/plugin.py

class PluginManager:
    def __init__(self):
        self._plugins = []

    def register(self, plugin: Plugin):
        self._plugins.append(plugin)

    def dispatch(self, event):
        for plugin in self._plugins:
            plugin.handle(event)
