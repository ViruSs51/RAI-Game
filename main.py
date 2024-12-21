import pygame as pg
import asyncio
import json

from Game.Module import Scene as S
from Game.Module.Scene.scene import Scene
from Game.Module.DataType.scene import Scenes
from Game.Module.Scene.Interface import gameplay_ui


class Game:
    __run: bool = False
    __scene: str = "loading_scene"
    __config: dict = None

    def __init__(self):
        self.__config = self.__getConfig("Game/config.json")
        self.__w_size = self.__config["window"]["size"]

        pg.init()

        self.__window = self.__initWindow(window_size=self.__w_size)
        pg.display.set_caption(self.__config["window"]["title"])

        self.__gameplay_interface = gameplay_ui.GameplayInterface(
            window=self.__window, window_size=self.__w_size, config=self.__config
        )
        self.__player = S.init_player(window=self.__window, config=self.__config)
        self.__scenes = S.load_scenes(window=self.__window, window_size=self.__w_size, player=self.__player, config=self.__config)
    @staticmethod
    def __initWindow(window_size: str | list[int] | tuple[int]) -> pg.Surface:
        """
        Daca window_size contine o lista de 2 valori care reprezinta marimea la window, creaza un window de marimele date.
        Daca window_size are valoarea de 'FULLSCREEN', creaza un window pe tot ecranul.
        """

        if isinstance(window_size, (list, tuple)) and len(window_size) == 2:
            window = pg.display.set_mode(window_size)
        elif window_size == "FULLSCREEN":
            window = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        else:
            raise ValueError(
                "Invalid value for 'window_size': Expected a list, tuple, or the string 'FULLSCREEN'."
            )

        return window

    @staticmethod
    def __getConfig(file: str) -> dict:
        with open(file, "r", encoding="utf-8") as file_config:
            config = json.loads(file_config.read())

        config["characters"]["player"]["position"] = [
            config["window"]["size"][0] / 2
            - config["characters"]["player"]["size"][0] / 2,
            config["window"]["size"][1]
            - config["characters"]["player"]["size"][1]
            - 200,
        ]

        return config

    async def __callScene(self, object: Scenes | Scene):
        swap_scene = (
            await self.__scenes[self.__scene].loader()
            if type(object) is Scenes
            else await object.loader()
        )

        if swap_scene is not None and swap_scene in self.__scenes:
            self.__scene = swap_scene

    def run(self):
        self.__run = True

        asyncio.run(self.__asyncronRun())

    async def __asyncronRun(self):
        await self.__loop()

    async def __loop(self):
        while self.__run:
            self.__window.fill("black")

            # Verifica daca se apasa close la window, daca da, window se inchide
            for e in pg.event.get():
                self.__run = False if e.type == pg.QUIT else True

            await self.__functionLoader()

            pg.display.flip()

        pg.quit()

    async def __functionLoader(self):
        """
        Aceasta functie e pentru a indica ordinea de indiplinire a functiilor globale in joc
        """
        await self.__callScene(object=self.__scenes)

        if not self.__scene in self.__gameplay_interface.not_on_scenes:
            await self.__callScene(object=self.__gameplay_interface)

    def loadSounds(self):
        pg.mixer.music.load("Game Assets/sounds/background/background_cosmic_serenity.mp3")
        pg.mixer.music.set_volume(0.5)
        pg.mixer.music.play(loops=-1)

if __name__ == "__main__":
    game = Game()
    game.run()
