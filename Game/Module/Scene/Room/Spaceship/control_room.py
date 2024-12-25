import pygame as pg
from copy import deepcopy
from ...Room.room import Room
from ....Objects.Character.Player.player import Player
from ....Objects.Generator.Monster.monster_generator import MonsterGenerator
from ....Objects.Character.Monster.monster import Monster


class ControlRoom(Room):

    def __init__(
        self,
        window: pg.Surface,
        window_size: str | list[int] | tuple[int],
        config: dict,
        player: Player,
    ):
        super().__init__(
            window=window, window_size=window_size, config=config, player=player
        )
        self.initFloor()

        self.monster_generator = MonsterGenerator(
            window=window,
            images_url=config["characters"]["monsters"],
            chunk_dimension=config["game"]["chunk_dimension"],
            monster_counts=self.max_monster_in_chunk,
        )
        self.addObject(self.monster_generator.monsters + [self._player])

    def initFloor(self):
        self.floor_image = "Game Assets/tiles/space_station_1/floor/floor_50.png"
        self.floor_size = [32, 32]
        self.floor_initial_pos = [-self.floor_size[0], -self.floor_size[0]]
        self.floor_pos = deepcopy(self.floor_initial_pos)

        total_width = (self._w_size[0] // self.floor_size[0] + 3) * self.floor_size[0]
        total_height = (self._w_size[1] // self.floor_size[1] + 3) * self.floor_size[1]
        self.floor_surface = pg.Surface((total_width, total_height))

        floor_tile = pg.image.load(self.floor_image).convert_alpha()

        for x in range(0, total_width, self.floor_size[0]):
            for y in range(0, total_height, self.floor_size[1]):
                self.floor_surface.blit(floor_tile, (x, y))

    async def loader(self):
        self._window.blit(self.floor_surface, self.floor_pos)

        await self.movementPlayer()

        returned = await super().loader()

        if self.monsters_in_chunck < self.max_monster_in_chunk:
            self.objects = (
                self.monster_generator.generateMonsters(
                    monster_counts=self.max_monster_in_chunk - self.monsters_in_chunck
                )
                + self.objects
            )

        return returned
