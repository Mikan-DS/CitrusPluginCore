# The Citrus Plugin Core

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
```
*.rpyc
*.rpymc
*.0rpy
*.DS_Store
*.zip
*.rar
*.bak
```