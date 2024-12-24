from pygame import Surface
from ...Character.Monster.monster import Monster
from ...objects import Object
import random


class MonsterGenerator(Object):
    def __init__(self, window: Surface, images_url: dict[dict[list]], chunk_dimension: dict, monster_counts: int=100):
        super().__init__(window, [0, 0], [0, 0], None, images_url=images_url)
        self.chunk_dimension = chunk_dimension
        self.monster_counts = monster_counts
        self.monsters: list[Monster] = self.generateMonsters(monster_counts=self.monster_counts)
    
    def generateMonster(self):
        monster_type = random.choice(list(self.images_url.keys()))

        x = random.choice([random.randint(self.chunk_dimension[0][0], 0), random.randint(self.window_size[0], self.chunk_dimension[0][1])])
        y = random.choice([random.randint(self.chunk_dimension[1][0], 0), random.randint(self.window_size[1], self.chunk_dimension[1][1])])

        return Monster(
            window=self.window,
            size=self.images_url[monster_type]['size'],
            position=[x, y],
            images_url=self.images_url[monster_type]["samples"],
            max_life=self.images_url[monster_type]['max_life'],
            speed=self.images_url[monster_type]['speed'],
            running_speed=self.images_url[monster_type]['running_speed'],
            special_sizes=self.images_url[monster_type]['special_sizes'],
            attack_range=self.images_url[monster_type]['attack_range'],
            damage=self.images_url[monster_type]['damage'],
            knockback=self.images_url[monster_type]['knockback']
        ) 

    def generateMonsters(self, monster_counts: int=100):
         self.monster_counts = monster_counts
         return [self.generateMonster() for m in range(self.monster_counts)]