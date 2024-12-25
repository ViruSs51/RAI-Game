from ..Objects.objects import Object

from time import time
import pygame as pg
import asyncio


class Animation(Object):
    def __init__(
        self,
        window: pg.Surface,
        size: list[int],
        position: list[int],
        images_url: list[str],
        colors: list[list[int] | str] = None,
        delay: int = 1,
    ):
        self.all_images = images_url
        self.current_delay = 0
        self.max_delay = 0
        self.images = []

        super().__init__(window, size, position, colors, images_url[0], -1)

        self.save_get_damage = None
        self.save_perspective_full_animation = None
        self.finish_full_animation = True

        self.d = delay
        self.max_dalay = time() + self.d

    async def draw(
        self,
        perspective: int = 0,
        objects: list[Object] = None,
        special_sizes: list = None,
        get_damage: bool = None,
    ):
        if self.start:
            for i, pi in enumerate(self.all_images):
                self.images.append(
                    await self.setImages(
                        new_images=pi,
                        new_size=(
                            special_sizes[str(i)]
                            if special_sizes and str(i) in special_sizes.keys()
                            else None
                        ),
                    )
                    if i != 0
                    else await self.setImages()
                )

        if (
            get_damage != None
            and get_damage
            and (get_damage != self.save_get_damage and get_damage)
        ):
            self.finish_full_animation = True

        if get_damage != self.save_get_damage:
            self.save_get_damage = get_damage

        if 12 <= perspective or not self.finish_full_animation:
            await self.delayFullAnimation(perspective=perspective)
        else:
            await self.delay(perspective=perspective)

        self.window.blit(self.fill_image, self.pos)

        await self.oneStart()

    async def delayFullAnimation(self, perspective: int):
        if self.finish_full_animation:
            self.save_perspective_full_animation = perspective
            self.finish_full_animation = False
            self.fill_index = 0

        elif time() >= self.max_dalay:
            if self.fill_index >= len(
                self.images[self.save_perspective_full_animation]
            ):
                self.fill_index = 0
                self.save_perspective_full_animation = None
                self.finish_full_animation = True
            else:
                self.fill_image = self.images[self.save_perspective_full_animation][
                    self.fill_index
                ]
            self.max_dalay = time() + self.d
            self.fill_index += 1

    async def delay(self, perspective: int):
        if time() >= self.max_dalay:
            if self.fill_index >= len(self.images[perspective]):
                self.fill_index = 0

            self.fill_image = self.images[perspective][self.fill_index]
            self.max_dalay = time() + self.d
            self.fill_index += 1
