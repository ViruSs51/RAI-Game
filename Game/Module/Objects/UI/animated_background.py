import pygame as pg
from PIL import Image
import time
from ...Scene import scene 
from pygame import Surface

class AnimatedBackground():
    def __init__(self, gif_path, size):
        self.frames = []
        self.load_gif(gif_path, size)
        self.current_frame = 0
        self.last_update_time = time.time()
        self.frame_duration = 0.04  # Duration for each frame (in seconds)

    def load_gif(self, gif_path, size):
        """
        Load GIF frames using Pillow and resize them to the desired size.
        """
        gif = Image.open(gif_path)
        while True:
            # Convert each frame to a Pygame Surface
            frame = gif.convert("RGBA")
            mode = frame.mode
            size = frame.size
            data = frame.tobytes()

            pg_image = pg.image.fromstring(data, size, mode)
            pg_image = pg.transform.scale(pg_image, size)
            self.frames.append(pg_image)

            try:
                gif.seek(gif.tell() + 1)
            except EOFError:
                break

    async def update(self):
        """
        Update the current frame based on the time elapsed.
        """
        if time.time() - self.last_update_time > self.frame_duration:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.last_update_time = time.time()


    def get_current_frame(self):
        return self.frames[self.current_frame]