import pygame as pg


class Object:
    def __init__(
        self,
        window: pg.Surface,
        size: list[int],
        position: list[int],
        colors: list[list[int] | str],
        images_url: list[str] = None,
        border_radius: int = -1,
    ):
        self.collider = False
        self.start = True
        self.fill_index = 0
        self.fill_image = None
        self.window = window
        self.window_size = self.window.get_size()
        self.size = size
        self.pos = position
        self.colors = colors
        self.images_url = images_url
        self.border_radius = border_radius
        self.can_move_to_up = True
        self.can_move_to_right = True
        self.can_move_to_down = True
        self.can_move_to_left = True

    async def oneStart(self):
        if self.start:
            self.start = False

    async def draw(self, objects: list['Object']=None):
        if objects:
            self.can_move_to_up = True
            self.can_move_to_right = True
            self.can_move_to_down = True
            self.can_move_to_left = True

            for o in objects:
                if o != self and o.collider and self.collider and -200 < o.pos[0] < self.window_size[0]+200 and -200 < o.pos[1] < self.window_size[1]+200:
                    if self.can_move_to_up: self.can_move_to_up = o.pos[1]+o.size[1]-10 < self.pos[1] or o.pos[1] > self.pos[1] or o.pos[0]+o.size[0] < self.pos[0]+20 or o.pos[0] > self.pos[0]+self.size[0]-20
                    if self.can_move_to_right: self.can_move_to_right = o.pos[0]+10 > self.pos[0]+self.size[0] or o.pos[0] < self.pos[0] or o.pos[1]+o.size[1] < self.pos[1]+20 or o.pos[1] > self.pos[1]+self.size[1]-20
                    if self.can_move_to_down: self.can_move_to_down = o.pos[1]+10 > self.pos[1]+self.size[1] or o.pos[1] < self.pos[1] or o.pos[0]+o.size[0] < self.pos[0]+20 or o.pos[0] > self.pos[0]+self.size[0]-20
                    if self.can_move_to_left: self.can_move_to_left = o.pos[0]+o.size[0]-10 < self.pos[0] or o.pos[0] > self.pos[0] or o.pos[1]+o.size[1] < self.pos[1]+20 or o.pos[1] > self.pos[1]+self.size[1]-20

    async def setImages(self, new_images: list = None) -> list:
        if not self.images_url:
            return None

        images = [
            pg.image.load(i)
            for i in (self.images_url if not new_images else new_images)
        ]

        resized_images = []
        for img in images:
            resized_images.append(pg.transform.scale(img, self.size))

        if not new_images:
            self.fill_image = resized_images[0]

        return resized_images
