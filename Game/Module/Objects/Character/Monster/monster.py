from pygame import Surface
from ..character import Character
from ...objects import Object
from ..Player.player import Player
from ...UI.Hotbar.health_bar import HealthBar
from ....AI.QLearning.Pathfinding import pathfinding
from copy import deepcopy
from time import time


class Monster(Character):
    def __init__(
        self,
        window: Surface,
        size: list[int],
        position: list[int],
        images_url: list[str],
        max_life: int = 10,
        speed: float = 0.32,
        running_speed: float = 0.52,
        special_sizes: list[int] = None,
        attack_range: list[int] = None,
        damage: float = 1,
        knockback: dict = None,
        stamina: int = 4,
    ):
        super().__init__(
            window,
            size,
            position,
            images_url,
            ctype="monster",
            max_life=max_life,
            speed=speed,
            running_speed=running_speed,
            special_sizes=special_sizes,
            attack_range=attack_range,
            damage=damage,
            knockback=knockback,
            stamina=stamina,
        )
        self.collider = True
        self.health_bar_size = [100, 10]
        self.health_bar = HealthBar(
            window=self.window,
            size=self.health_bar_size,
            position=[
                self.pos[0] + self.size[0] / 2 - self.health_bar_size[0] / 2,
                self.pos[1] - 25 - self.health_bar_size[1],
            ],
            border_radius=-1,
            hp=self.life,
            maxhp=self.max_life,
        )

        self.pathfinding_model = pathfinding.QLearningGame(
            grid_size=[100, 100], player_pos=[0, 0], obstacles=[]
        )

    async def helthBarPosition(self):
        return [
            self.pos[0] - abs(self.size[0] - self.health_bar_size[0]) / 2,
            self.pos[1] - 25 - self.health_bar_size[1],
        ]

    async def draw(self, objects: list[Object] = None):
        if not self.dead:
            self.click_left_button = True
            self.character = await self.Animated()
            if not self.start:
                await self.processing()
            await super().draw(objects=objects)
            await self.health_bar.updateHp(self.life)
            await self.health_bar.updatePosition(position=await self.helthBarPosition())

    async def thinking2(self, player_position: list[int], player_size: list[int]):
        move_to = "stay"
        if self.pos[0] < player_size[0]:
            move_to = "left"
            self.press_a, self.press_d = True, False
        elif self.size[0] > player_position[0]:
            move_to = "right"
            self.press_d, self.press_a = True, False
        else:
            self.press_d, self.press_a = False, False

        if self.pos[1] < player_size[1]:
            move_to = "up"
            self.press_w, self.press_s = True, False
        elif self.size[1] > player_position[1]:
            move_to = "down"
            self.press_s, self.press_w = True, False
        else:
            self.press_s, self.press_w = False, False

        print(move_to)

    async def thinking(
        self,
        obstacles: list[Object],
        player_position: list[int],
        player_size: list[int],
    ):
        difference = [
            abs(self.pos[0]) if self.pos[0] < 0 else 0,
            abs(self.pos[1]) if self.pos[1] < 0 else 0,
        ]
        difference2 = [
            (
                player_position[0] - self.pos[0]
                if player_position[0] > self.pos[0]
                else self.pos[0] - player_position[0]
            ),
            (
                player_position[1] - self.pos[1]
                if player_position[1] > self.pos[1]
                else self.pos[1] - player_position[1]
            ),
        ]
        grid_size = [
            (
                player_position[0] + difference[0] + player_size[0]
                if self.pos[0] < 0
                else abs(
                    player_position[0] + player_size[0] + self.pos[0] - difference[0]
                )
            ),
            (
                player_position[1] + difference[1] + player_size[1]
                if self.pos[1] < 0
                else abs(
                    player_position[1] + player_size[1] + self.pos[1] - difference[1]
                )
            ),
        ]
        player_position = [
            player_position[0] + difference[0],
            player_position[1] + difference[1],
        ]

        new_obstacles = []
        for o in obstacles:
            new_obstacle = pathfinding.Obstacle(
                pos=[o.pos[0] + difference[0], o.pos[1] + difference[1]],
                size=[o.size[0] + difference[0], o.size[1] + difference[1]],
            )

            if (
                new_obstacle.pos[0] >= 0
                and new_obstacle.pos[0] + new_obstacle.size[0] < grid_size[0]
                and new_obstacle.pos[1] >= 0
                and new_obstacle.pos[1] + new_obstacle.size[1] <= grid_size[1]
            ):
                new_obstacles.append(new_obstacle)

        try:
            await self.pathfinding_model.load_q_table()
        except:
            pass

        await self.pathfinding_model.reset_environment(
            grid_size=grid_size,
            new_player_pos=player_position,
            new_obstacles=new_obstacles,
        )

        monster_pos = [abs(int(self.pos[0])), abs(int(self.pos[1]))]

        await self.pathfinding_model.train(
            monster_pos=monster_pos, episodes=1, max_steps=1
        )

        await self.pathfinding_model.retrain(
            monster_pos=monster_pos, episodes=1, max_steps=1
        )

        await self.pathfinding_model.save_q_table()

        next_move = await self.pathfinding_model.next_action(
            monster_pos, player_position, obstacles
        )
        move_to = "stay"
        if next_move[0] == -1:
            move_to = "left"
            self.press_a, self.press_d, self.press_w, self.press_s = (
                True,
                False,
                False,
                False,
            )
        elif next_move[0] == 1:
            move_to = "right"
            self.press_d, self.press_a, self.press_w, self.press_s = (
                True,
                False,
                False,
                False,
            )
        elif next_move[1] == -1:
            move_to = "up"
            self.press_w, self.press_d, self.press_a, self.press_s = (
                True,
                False,
                False,
                False,
            )
        elif next_move[1] == 1:
            move_to = "down"
            self.press_s, self.press_d, self.press_w, self.press_a = (
                True,
                False,
                False,
                False,
            )
        else:
            self.press_s, self.press_d, self.press_w, self.press_a = (
                False,
                False,
                False,
                False,
            )
