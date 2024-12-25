import pygame as pg
from time import time
from ...Objects.objects import Object
from ..animation import Animation
from ..Controller.controller import Controller


class Character(Object):

    def __init__(
        self,
        window: pg.Surface,
        size: list[int],
        position: list[int],
        images_url: list[str],
        ctype: str,
        max_life: int=10,
        speed: float=0.35,
        running_speed: float=0.8,
        special_sizes: list[int]=None,
        attack_range: list[int]=None,
        damage: float=1,
        knockback: dict=None
    ):
        super().__init__(
            window, size, position, colors=None, images_url=images_url, border_radius=-1
        )
        self.character: pg.Rect
        self.perspective: int = 0
        self.type_animation: int = 0
        self.main_speed = speed
        self.speed = self.main_speed
        self.knockback_speed = knockback['speed']
        self.knockback_perspective = 0
        self.running_speed = running_speed
        self.max_life = max_life
        self.life = self.max_life
        self.dead = False
        self.damages = damage
        self.special_sizes = special_sizes
        self.attack_range = attack_range
        self.main_speed = speed
        self.speed = self.main_speed
        self.running_speed = running_speed
        self.controller: Controller = None
        self.monster_kills = None

        self.ctype = ctype
        self.press_w = False
        self.press_s = False
        self.press_d = False
        self.press_a = False
        self.press_shift = False
        

        self.toUp = lambda: self.pos[1] - self.speed
        self.toRight = lambda: self.pos[0] + self.speed 
        self.toDown = lambda: self.pos[1] + self.speed
        self.toLeft = lambda: self.pos[0] - self.speed

        self.window_size = window.get_size()

        self.attack_delay = 3
        self.attack_max_delay = time() + self.attack_delay
        self.damage_delay = 2
        self.damage_max_delay = time() + self.damage_delay
        self.get_damage_delay = knockback['delay']
        self.get_damage_max_delay = time() + self.damage_delay

        self.main_pos = self.pos
        self.animation = Animation(
            window=window,
            size=self.size,
            position=self.pos,
            images_url=images_url,
            delay=0.09,
        )

    async def draw(self, objects: list[Object]=None):
        await self.oneStart()
        await super().draw(objects=objects)
                

    async def Animated(self):
        await self.animation.draw(
            perspective=self.perspective + 4 * self.type_animation,
            special_sizes=self.special_sizes,
            get_damage=self.get_damage
        )

    async def control(self, with_controller: bool=False):
        self.give_damage = False

        if time() > self.get_damage_max_delay:
            self.get_damage = False
        else:
            self.can_move_to_up, self.can_move_to_right, self.can_move_to_down, self.can_move_to_left = False, False, False, False

        if time() < self.get_damage_max_delay/2:
            if self.knockback_perspective == 0: self.pos[1] -= self.knockback_speed 
            if self.knockback_perspective == 1: self.pos[0] += self.knockback_speed
            if self.knockback_perspective == 2: self.pos[1] += self.knockback_speed
            if self.knockback_perspective == 3: self.pos[0] -= self.knockback_speed
            


        if with_controller:
            self.press_w = await self.controller.getPressed("w")
            self.press_s = await self.controller.getPressed("s")
            self.press_d = await self.controller.getPressed("d")
            self.press_a = await self.controller.getPressed("a") 
            self.press_shift = await self.controller.getPressed("shift")
            self.click_left_button = await self.controller.getClick(button=0)      

        self.not_action = set((self.press_w, self.press_s, self.press_d, self.press_a)) == {0}

        if self.press_w and self.can_move_to_up:
            self.pos[1] = self.toUp()
            self.perspective = 0
            self.type_animation = 1

        elif self.press_s and self.can_move_to_down:
            self.pos[1] = self.toDown()
            self.perspective = 2
            self.type_animation = 1

        if self.press_d and self.can_move_to_right:
            self.pos[0] = self.toRight()
            self.perspective = 1
            self.type_animation = 1

        elif self.press_a and self.can_move_to_left:
            self.pos[0] = self.toLeft()
            self.perspective = 3
            self.type_animation = 1

        if self.press_shift and not self.not_action:
            self.type_animation = 2
            self.speed = self.running_speed

        else:
            self.speed = self.main_speed

        if not self.damaged and time() >= self.damage_max_delay:
            self.give_damage, self.damaged = True, True

        if self.click_left_button and time() >= self.attack_max_delay or self.get_damage:
            self.type_animation = 3 if self.type_animation == 0 else 4 if self.type_animation == 1 else 5 if self.type_animation == 2 else self.type_animation
            self.attack_max_delay = time() + self.attack_delay
            self.give_damage, self.damaged = False, False

        elif self.not_action:
            self.type_animation = 0

    async def processing(self, *args, **kwargs):
        await self.control(*args, **kwargs)

    async def checkCoincideTwoAxes(self, axe1_side1, axe1_side2, axe2_side1, axe2_side2):
        return (axe1_side1<= axe2_side2 and axe1_side2 >= axe2_side2) or (axe1_side1 <= axe2_side1 and axe1_side2 >= axe2_side1) or (axe2_side1 <= axe1_side1 and axe1_side2 <= axe2_side2)

    async def checkCoincideTwoPlaces(self, axe1_side1, axe1_side2, axe2_side1, axe2_side2, axe3_side1, axe3_side2, axe4_side1, axe4_side2):
        checked_two_x_axes = await self.checkCoincideTwoAxes(
            axe1_side1=axe1_side1, 
            axe1_side2=axe1_side2,
            axe2_side1=axe2_side1,
            axe2_side2=axe2_side2
        )
        checked_two_y_axes = await self.checkCoincideTwoAxes(
            axe1_side1=axe3_side1, 
            axe1_side2=axe3_side2,
            axe2_side1=axe4_side1,
            axe2_side2=axe4_side2
        )

        return checked_two_x_axes and checked_two_y_axes

    async def damage(self, object: Object):
        if self.click_left_button and self.life != None:
            if self.perspective == 0:
                attack_range_x = self.centers[0]-self.attack_range[0]/2, self.centers[0]+self.attack_range[0]/2
                attack_range_y = self.pos[1]-self.attack_range[1], self.pos[1]+self.size[1]/2
                #pg.draw.rect(self.window, 'red', (attack_range_x[0], attack_range_y[0], attack_range_x[1]-attack_range_x[0], attack_range_y[1]-attack_range_y[0]))
                
                coincide_two_places = await self.checkCoincideTwoPlaces(
                    axe1_side1=object.pos[0], 
                    axe1_side2=object.pos[0]+object.size[0],
                    axe2_side1=attack_range_x[0],
                    axe2_side2=attack_range_x[1],
                    axe3_side1=object.pos[1], 
                    axe3_side2=object.pos[1]+object.size[1],
                    axe4_side1=attack_range_y[0],
                    axe4_side2=attack_range_y[1]
                )

            elif self.perspective == 1:
                attack_range_x = self.centers[0], self.pos[0]+self.size[0]+self.attack_range[1]
                attack_range_y = self.centers[1]-self.attack_range[0]/2, self.centers[1]+self.attack_range[0]/2
                #pg.draw.rect(self.window, 'red', (attack_range_x[0], attack_range_y[0], attack_range_x[1]-attack_range_x[0], attack_range_y[1]-attack_range_y[0]))
                
                coincide_two_places = await self.checkCoincideTwoPlaces(
                    axe1_side1=object.pos[0], 
                    axe1_side2=object.pos[0]+object.size[0],
                    axe2_side1=attack_range_x[0],
                    axe2_side2=attack_range_x[1],
                    axe3_side1=object.pos[1], 
                    axe3_side2=object.pos[1]+object.size[1],
                    axe4_side1=attack_range_y[0],
                    axe4_side2=attack_range_y[1]
                )

            elif self.perspective == 2:
                attack_range_x = self.centers[0]-self.attack_range[0]/2, self.centers[0]+self.attack_range[0]/2
                attack_range_y = self.pos[1]+self.size[1]/2, self.pos[1]+self.size[1]+self.attack_range[1]
                #pg.draw.rect(self.window, 'red', (attack_range_x[0], attack_range_y[0], attack_range_x[1]-attack_range_x[0], attack_range_y[1]-attack_range_y[0]))
                
                coincide_two_places = await self.checkCoincideTwoPlaces(
                    axe1_side1=object.pos[0], 
                    axe1_side2=object.pos[0]+object.size[0],
                    axe2_side1=attack_range_x[0],
                    axe2_side2=attack_range_x[1],
                    axe3_side1=object.pos[1], 
                    axe3_side2=object.pos[1]+object.size[1],
                    axe4_side1=attack_range_y[0],
                    axe4_side2=attack_range_y[1]
                )

            elif self.perspective == 3:
                attack_range_x = self.pos[0]-self.attack_range[1], self.centers[0]
                attack_range_y = self.centers[1]-self.attack_range[0]/2, self.centers[1]+self.attack_range[0]/2
                #pg.draw.rect(self.window, 'red', (attack_range_x[0], attack_range_y[0], attack_range_x[1]-attack_range_x[0], attack_range_y[1]-attack_range_y[0]))
                
                coincide_two_places = await self.checkCoincideTwoPlaces(
                    axe1_side1=object.pos[0], 
                    axe1_side2=object.pos[0]+object.size[0],
                    axe2_side1=attack_range_x[0],
                    axe2_side2=attack_range_x[1],
                    axe3_side1=object.pos[1], 
                    axe3_side2=object.pos[1]+object.size[1],
                    axe4_side1=attack_range_y[0],
                    axe4_side2=attack_range_y[1]
                )

            if coincide_two_places:
                await object.giveDamage(damage=self.damages, perspective=self.perspective)

                if self.monster_kills != None and object.life < 0.01: 
                    object.dead = True
                    self.monster_kills += 1
    
    async def giveDamage(self, damage: int = 1, perspective: int=None):
        self.life -= damage
        self.get_damage = True
        self.get_damage_max_delay = time() + self.get_damage_delay
        self.type_animation = 6

        self.knockback_perspective = perspective