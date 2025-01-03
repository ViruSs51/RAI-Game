import pygame as pg

from ..Objects.objects import Object
from ..Objects.Character.Player.player import Player
from ..Objects.UI.Hotbar import health_bar, stamina_bar


class Scene:
    objects: list[Object] = []
    swap_scene = None
    returned = []

    def __init__(
        self,
        window: pg.Surface,
        window_size: str | list[int] | tuple[int],
        config: dict,
        player: Player = None,
    ):
        self.objects = []
        self._window = window
        self._w_size = window_size
        self._player = player
        self.config = config
        self.chunk_dimension = self.config["game"]["chunk_dimension"]
        self.monsters_in_chunck = 0
        self.max_monster_in_chunk = self.config["game"]["max_monsters_in_chunk"]

    def addObject(self, objects: list):
        for o in objects:
            self.objects.append(o)

    async def loader(self):
        """
        Se indica toate obiectele si logica pe scena
        """
        self.monsters_in_chunck = 0

        obstacles = []
        new_objects = []
        self.returned = []
        for o in self.objects:
            if (
                -o.size[0] < o.pos[0] < self._w_size[0] + o.size[0]
                and -o.size[1] < o.pos[1] < self._w_size[1] + o.size[1]
            ):
                self.returned.append(await o.draw(objects=self.objects))

            else:
                try:
                    await o.processing()
                except:
                    pass

            if (
                self.chunk_dimension[0][0] < o.pos[0] < self.chunk_dimension[0][1]
                and self.chunk_dimension[1][0] < o.pos[1] < self.chunk_dimension[1][1]
            ):
                if o.ctype == "monster":
                    self.monsters_in_chunck += 1
                o.in_chunk = True

            else:
                o.in_chunk = False

            if type(o) == health_bar.HealthBar:
                await o.updateHp(self._player.life)

            elif type(o) == stamina_bar.StaminaBar:
                await o.updateStamina(stamina=self._player.stamina)

            if o.ctype != "monster" or (
                (o.ctype == "monster" and o.in_chunk)
                and (o.life != None and o.life > 0 and o.ctype == "monster")
            ):
                new_objects.append(o)
            if o.ctype != "player":
                obstacles.append(o)
        self.objects = new_objects

        for o in self.objects:
            if o.ctype == "monster":
                await o.health_bar.draw()
                await o.thinking2(self._player.pos, self._player.size)

        return self.swap_scene
