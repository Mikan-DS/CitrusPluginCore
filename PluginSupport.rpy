init -999 python in CitrusPluginSupport:

    import store

    class LOG_LEVELS:
        message = 0
        warning = 1
        error = 2

        symbols = "+?!"

    LOG_LEVEL = 0
    initialize_time = False

    class Plugin:
        def __init__(self, name, version, order=0):
            self.name = name
            self.version = version
            self.order = order

    core_plugin_config = {
        "version": "1.24.05.11.0",
        "name": "CitrusPluginSupport",
        "order": -1000
    }

    plugins = {}

    def init_plugin(plugin_config):

        name = plugin_config["name"]
        version = plugin_config["version"]

        if initialize_time:


            if name in plugins.keys():
                log(f"Some of the plugins trying to initialize more than once! \"{name}\" v{version} (initialized v{plugins[name].version})", message_type="?")
                return

            log(f"Start init for plugin \"{name}\" v{version}", core_plugin_config["name"])
            plugins[name] = Plugin(**plugin_config)
            setattr(getattr(store, name), "log", register_logger(name))
            log(f"Plugin initialized \"{name}\" v{version}", core_plugin_config["name"])
        else:
            log(f"Wrong time for initializing, it must be at init -997: \"{name}\" v{version}")
            raise Exception(f"Wrong time for initializing, it must be at init -997: \"{name}\" v{version}")

    def log(message, plugin_name="", message_type="+"):

        
        if LOG_LEVEL > LOG_LEVELS.symbols.find(message_type):
            return
        
        if plugin_name:
            plugin_name = f"[{plugin_name}] "
        else:
            try:
                plugin_name = f"[{__name__.replace('store.', '')}] "
            except:
                pass
        print(f"[{message_type}] {plugin_name} {message}")

    def register_logger(plugin_name):
        def logger(message, message_type="+"):
            log(message, plugin_name, message_type)
        return logger
    
    log(f"Plugin support initialized! Current version is {core_plugin_config['version']}")

init -998 python in CitrusPluginSupport:
    initialize_time = True
    log("Beginning plugins initialization phase")
init -996 python in CitrusPluginSupport:
    initialize_time = False
    log("Plugins initialization phase end")