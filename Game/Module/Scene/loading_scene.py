from pygame import Surface, image, transform
from .scene import Scene
import threading


class Loading(Scene):
    swap_scene = "main_menu"

    def __init__(
        self, window: Surface, window_size: str | list[int] | tuple[int], config: dict
    ):
        super().__init__(window=window, window_size=window_size, config=config)
        self.bg_image = image.load("Game Assets\main_assets\loading_image.png")
        self.width, self.height = self._window.get_size()
        self.WORK = 3000000
        self.distance = 12

        self._window.blit(
            transform.scale(self.bg_image, (self._window.get_size())), (0, 0)
        )
        self._window.blit(
            transform.scale(
                image.load("Game Assets\main_assets\logo.png"),
                (int(self.width * 0.20), int(self.height * 0.22)),
            ),
            (12, 12),
        )
        self.create_loading_bar()
        threading.Thread(target=self.doWork).start()

    def create_loading_bar(self):
        self.loading_bg = image.load("Game Assets\main_assets\loading_bar_bg.png")
        self.loading_bg_width = 526
        self.loading_bg_height = 100
        self.load_position_bg = (
            self.width - self.loading_bg_width - (self.distance * 2),
            self.height - self.loading_bg_height - (self.distance * 2),
        )

        self.loading_bar_width = 516
        self.loading_bar_height = 90
        self.load_position_bar = (
            self.width - self.loading_bar_width - (self.distance * 2),
            self.height - self.loading_bar_height - (self.distance * 2),
        )
        self.loading_bar = image.load("Game Assets\main_assets\loading_bar.png")

        self.loading_finished = False
        self.loading_progress = 0
        self.loading_bar_width = 8

    def runningLoadingBar(self):
        if not self.loading_finished:
            self.loading_bar_width = self.loading_progress / self.WORK * 506

            scaled_loading_bar = transform.scale(
                self.loading_bar, (int(self.loading_bar_width), 80)
            )

            self._window.blit(self.bg_image, (0, 0))  # Redraw the full background
            self._window.blit(
                transform.scale(
                    image.load("Game Assets\main_assets\logo.png"),
                    (int(self.width * 0.20), int(self.height * 0.22)),
                ),
                (12, 12),
            )

            self._window.blit(
                self.loading_bg, self.load_position_bg
            )  # Redraw the loading bar background

            self._window.blit(scaled_loading_bar, self.load_position_bar)

    # Do work function
    def doWork(self):
        for i in range(self.WORK):
            math_equation = 403194 / 41834 * 89655
            self.loading_progress = i

        self.loading_finished = True

    async def loader(self):
        if self.loading_finished:
            return await super().loader()
        self.runningLoadingBar()
