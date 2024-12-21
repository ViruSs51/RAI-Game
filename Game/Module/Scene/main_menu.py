from pygame import Surface, image, transform, font
from .scene import Scene
from ..Objects.UI import animated_background, menu
import asyncio
import threading


class MainMenu(Scene, menu.Menu):

    def __init__(
        self, window: Surface, window_size: str | list[int] | tuple[int], config: dict
    ):
        super().__init__(window=window, window_size=window_size, config=config)
        self.width, self.height = self._window.get_size()
        self.font = font.Font("Game Assets\casual_passion.ttf", 25)

        btn_distance = 12 * 2  # I took 12 as base for distance
        initial_button_distance = self.height * 0.225 + self.height * 0.22
        border_distance = 12
        setting_button_pos = (
            (2 * (self.height // 10.8)) + initial_button_distance + (2 * btn_distance)
        )

        self.background = None
        self.t1 = threading.Thread(target=self.loadAssets)
        self.t1.start()
        self.play_button = self.createButton(
            text="Play Game", position=(border_distance, initial_button_distance)
        )
        self.settings_button = self.createButton(
            text="Settings",
            position=(
                border_distance,
                self.height // 10.8 + initial_button_distance + btn_distance,
            ),
        )
        self.exit_button = self.createButton(
            text="Exit", position=(border_distance, setting_button_pos)
        )

    def loadAssets(self):

        self.background = animated_background.AnimatedBackground(
            rf"Game Assets\main_assets\animated_background.gif", 255
        )

    async def loader(self):
        if self.background:
            await self.background.update()
            self._window.blit(
                transform.scale(
                    self.background.get_current_frame(), (self._window.get_size())
                ),
                (0, 0),
            )

        self._window.blit(
            transform.scale(
                image.load("Game Assets\main_assets\logo.png"),
                (int(self.width * 0.20), int(self.height * 0.22)),
            ),
            (12, 12),
        )
        buttons_press = await asyncio.gather(
            self.play_button.draw(),
            self.settings_button.draw(),
            self.exit_button.draw(),
        )

        if buttons_press[0]:
            self.swap_scene = "spaceship_control_room"
        else:
            self.swap_scene = None

        return await super().loader()
