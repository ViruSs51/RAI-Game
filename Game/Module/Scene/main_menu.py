from pygame import Surface,image,transform, font
from .scene import Scene
from ..Objects.UI import animated_background, menu
import asyncio

class MainMenu(Scene, menu.Menu):

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
        self.settings_button = self.create_button(text="Settings", position=(border_distance, self.height//10.8 + initial_button_distance + btn_distance))
        self.exit_button = self.create_button(text="Exit", position=(border_distance, setting_button_pos))
        

    async def loader(self): 
        await self.background.update()
        
        self._window.blit(transform.scale(self.background.get_current_frame(), (self._window.get_size())), (0,0))
        self._window.blit(transform.scale(image.load("Game Assets\main_assets\logo.png"), (int(self.width*0.20), int(self.height*0.22))), (12,12))
        await asyncio.gather(
            self.play_button.draw(),
            self.settings_button.draw(),
            self.exit_button.draw()
        )   


    
