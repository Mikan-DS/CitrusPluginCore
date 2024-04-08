init -999 python in CitrusPluginSupport:

    import store

    LOG_LEVEL = 0

    class Plugin:
        def __init__(self, name, version, order=0):
            self.name = name
            self.version = version
            self.order = order

    core_plugin_config = {
        "version": "1.24.04.08.0",
        "name": "CitrusPluginSupport",
        "order": -1000
    }

    plugins = {}

    def init_plugin(plugin_config):
        name = plugin_config["name"]
        version = plugin_config["version"]

        log(f"Start init for plugin \"{name}\" v{version}", core_plugin_config["name"])
        plugins[name] = Plugin(**plugin_config)
        setattr(getattr(store, name), "log", register_logger(name))
        log(f"Plugin initialized \"{name}\" v{version}", core_plugin_config["name"])

    def log(message, plugin_name="", message_type="+"):
        if plugin_name:
            plugin_name = f"[{plugin_name}] "
        if not LOG_LEVEL:
            print(f"[{message_type}] {plugin_name} {message}")

    def register_logger(plugin_name):
        def logger(message, message_type="+"):
            log(message, plugin_name, message_type)
        return logger

