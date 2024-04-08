# The Citrus Plugin Core

# RU
Это ядро для плагинов семейства `Citrus` сделанных под игры на движке Ren'Py.

Оно определяет стандартные и часто используемые фичи из плагинов, а так-же создает стандарты для реализаций.
Стандарты необходимы для быстрой и удобной комбинации и переиспользования плагинов.

## Архитектура плагина

Плагин - это субмодуль (гита) в основном проекте игры.
Он должен находится в папке `game/plugins`, название субмодуля должно соответствовать названию плагина.

Для примеров ниже, имя плагина `MyPlugin`, необходимо поменять на настоящее название плагина.
Плагин состоит из следующих компонентов чтобы следовать текущему стандарту:

### Plugin config

Рекомендуется использовать название файла `plugin_config.rpy`.
Этот компонент "подключает" модуль к ядру плагинов, сообщая при этом свои настройки.

Код состоит из двух частей: объявления и инициализатора

Объявление должно происходить в init -998 (или раньше).
И выглядеть примерно так:
```
init -998 python in MyPlugin:
    import store
    plugin_config = {
        "version": "0.24.04.08.1", 
        "name": "MyPlugin",
        "order": 0
    }
```

На данный момент обязательными настройками являются:
- name (название плагина)
- version (версия плагина, сооветуется использовать паттерн [релиз (0 или 1)].[год (два числа)].[месяц (два числа)].[день (два числа)].[номер сборки])

Инициализация должна происходить в init -997.

```
init -997 python in MyPlugin:

    try:
        from store import CitrusPluginSupport
        CitrusPluginSupport.init_plugin(plugin_config)
    except Exception as e:
        raise Exception("[-] This project don't have plugin support. Contact Mikan_DS.")
```

## Constants

Эта часть необходима для настройки внутренних констант приложения, которые возможно поменять.

Рекомендуется использовать файл `constants.rpy`. Код выполняется на init -999 (или раньше)
```
init -999 python in MyPlugin:
    pass # ваши настройки
```

Помимо этого, если в вашем плагине имеются константы которые высчитываются из других констант (которые могут быть изменены), то необходимо добавить дополнительный блок
на init -997.
```
init -997 python in MyPlugin:
    pass # ваши настройки
```

## Demo
Это необязательная часть, но советуется если есть возможность продемонстрировать работу вашего плагина.
Необходимо добавить экран `[Название вашего плагина]Demo`, на котором/с которого возможно продемонстрировать работу плагина. 

Рекомендуется использовать файл `demo.rpy`, в папке `demo`.

Помимо этого прописать в файле настройку для ренпая о том что в итоговый билд эти файлы вставлять не надо.

```
init python in MyPlugin:
    build.classify('plugins/MyPlugin/demo/*', None)
```

## Основная логика плагина

На данный момент, все что есть в правилах:
- Использовать неймспейс соответствующий названию плагина
- Ядро гарантирует что все константы готовы на init -995, а все общие модули на init -990

## Рекомендации

Советуем для хорошего тона писать документации `README.md` с описыванием как работает плагин, его зависимости и константы :)

Для репозиториев имеется проверенный временем `.gitignore`:
```rpy
*.rpyc
*.rpymc
*.0rpy
*.DS_Store
*.zip
*.rar
*.bak
```

---

# EN

This is the core for the `Citrus` family of plugins made for games running on the Ren'Py engine.

It defines the standard and often used features from plugins, as well as creates standards for implementations.
Standards are necessary for fast and convenient combination and reuse of plugins.

## Plugin architecture

A plugin is a submodule (git) in the main game project.
It should be located in the `game/plugins` folder, the submodule name should match the plugin name.

For the examples below, the plugin name is `MyPlugin`, you need to change this to the actual plugin name.
A plugin consists of the following components to follow the current standard:

### Plugin config

It is recommended to use the filename `plugin_config.rpy`.
This component "connects" the module to the core of plugins, while reporting its settings.

The code consists of two parts: declarations and an initializer

The declaration should occur in init -998 (or earlier).
And it looks something like this:

```
init -998 python in MyPlugin:
    import store
    plugin_config = {
        "version": "0.24.04.08.1",
        "name": "MyPlugin",
        "order": 0
    }

```

At the moment, the mandatory settings are:

- name (plugin name)
- version (plugin version, it is advisable to use the pattern [release (0 or 1)].[year (two digits)].[month (two digits)].[day (two digits)].[build number])

Initialization should occur in init -997.

```
init -997 python in MyPlugin:

    try:
        from store import CitrusPluginSupport
        CitrusPluginSupport.init_plugin(plugin_config)
    except Exception as e:
        raise Exception("[-] This project don't have plugin support. Contact Mikan_DS.")

```

## Constants

This part is necessary to configure the internal constants of the application, which can possibly be changed.

It is recommended to use the `constants.rpy` file. The code runs at init -999 (or earlier)

```
init -999 python in MyPlugin:
    pass # your settings

```

In addition to this, if your plugin has constants that are calculated from other constants (which can be changed), then you need to add an additional block
at init -997.

```
init -997 python in MyPlugin:
    pass # your settings

```

## Demo

This is an optional part, but it is advisable if there is an opportunity to demonstrate the work of your plugin.
You need to add a screen `[Name of your plugin]Demo`, on which/from which you can demonstrate the operation of the plugin.

It is recommended to use the `demo.rpy` file, in the `demo` folder.

In addition to this, write in the file the setting for renpy that these files should not be inserted into the final build.

```
init python in MyPlugin:
    build.classify('plugins/MyPlugin/demo/*', None)

```

## Main plugin logic

At the moment, all that is in the rules:

- Use the namespace corresponding to the name of the plugin
- The core guarantees that all constants are ready at init -995, and all common modules at init -990

## Recommendations

It is advised for good tone to write `README.md` documentation describing how the plugin works, its dependencies, and constants :)

For repositories, there is a time-tested `.gitignore`:

```
*.rpyc
*.rpymc
*.0rpy
*.DS_Store
*.zip
*.rar
*.bak
```
