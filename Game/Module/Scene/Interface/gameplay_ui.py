import pygame as pg

from ...Scene.scene import Scene
from ...Objects.objects import Object
from ...Objects.UI import text, button
from ...Objects.Character.Player.player import Player


class GameplayInterface(Scene):
    not_on_scenes = ["main_menu", "loading_scene"]

    def __init__(
        self,
        window: pg.Surface,
        window_size: str | list[int] | tuple[int],
        config: dict,
    ):
        super().__init__(window, window_size, config)

        self.addObject(
            # Pause button
            button.Button(
                self._window,
                size=[70, 70],
                position=[10, 10],
                images_url=[
                    "Game Assets/objects/ui_1/button-pause.png",
                    "Game Assets/objects/ui_1/button-pause.png",
                    "Game Assets/objects/ui_1/button-pause.png",
                ],
            )
        )

    async def loader(self):
        parent = await super().loader()

        if self.returned and self.returned[0]:
            self.swap_scene = "main_menu"

        else:
            self.swap_scene = None

        return parent
