init -999 python in CitrusPluginSupport:

    def debug_on_displayable(render, text, pos=(0, 0)):
        render.blit(
            renpy.render(
                store.Text(str(text).replace("{", "{{")), 1000, 1000, 0, 0
            ),
            pos
        )