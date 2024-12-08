from pygame import Surface,image,transform, font
from .scene import Scene
from ..Objects.UI import button, animated_background
import asyncio

class MainMenu(Scene):

    def __init__(self, window: Surface):
        super().__init__(window=window)
        self.width, self.height = self._window.get_size()
        self.font = font.Font("Game Assets\casual_passion.ttf", 25)

        self.background = animated_background.AnimatedBackground(rf"Game Assets\main_assets\animated_background.gif", 255)

        btn_distance = 12*2 # I took 12 as base for distance 
        initial_button_distance = (self.height * 0.225 + self.height * 0.22)
        border_distance = 12 
        setting_button_pos =  (2 * (self.height//10.8 )) + initial_button_distance + (2 * btn_distance)
        
        self.play_button = self.create_button(text="Play Game", position=(border_distance, initial_button_distance))
        self.settings_button = self.create_button(text="Settings", position=(12, self.height//10.8 + initial_button_distance + btn_distance))
        self.exit_button = self.create_button(text="Exit", position=(12, setting_button_pos))
        


    def create_button(self, text, position, font="Game Assets\casual_passion.ttf"):
        width, height =self.get_text_size(text)
        return button.Button(
            window=self._window,
            size=(self.width/3.65, self.height//10.8),
            position= position,
            text_position=(((self.width//3.65)// 2) - (width// 2) + position[0], ((self.height//10.8)// 2) - (height// 2)+position[1]),
            text=text,
            font_size=24,
            font=font,
            border_radius=12,
            colors=[(181, 159, 120), (201, 176, 130), (125, 99,54)],
            text_colors=[(42,54,99), (53,68,125), (30,39, 72)]
            
        )

    def get_text_size(self,text, font_name="Game Assets\casual_passion.ttf", font_size=24):
        """
        Returns the width and height of the rendered text for the given font.

        Args:
            text (str): The text to render.
            font_name (str): The name of the font (None for default font).
            font_size (int): The size of the font.

        Returns:
            tuple: (width, height) of the text rectangle.
        """

        text_surface = self.font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        return text_rect.width, text_rect.height


    async def loader(self): 
        await self.background.update()
        
        self._window.blit(transform.scale(self.background.get_current_frame(), (self._window.get_size())), (0,0))
        self._window.blit(transform.scale(image.load("Game Assets\main_assets\logo.png"), (int(self.width*0.20), int(self.height*0.22))), (12,12))
        await asyncio.gather(
            self.play_button.draw(),
            self.settings_button.draw(),
            self.exit_button.draw()
        )   


    
