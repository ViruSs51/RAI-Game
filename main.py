import pygame as pg
import asyncio

from  Game.Module import Scene



def get_developing_window_size():
    infoObject = pg.display.Info()
    return [infoObject.current_w/1.5, infoObject.current_h/1.5]

class Game:
    __run = False
    __scene = 'main_menu'

    def __init__(self, window_size: str|list[int]|tuple[int], title='RAI Game'):
        self.__w_size = window_size

        pg.init()

        self.__w_size = get_developing_window_size()

        self.__window = self.initWindow(window_size=self.__w_size)
        pg.display.set_caption(title)

        self.__scenes = Scene.load_scenes(window=self.__window, window_size=self.__w_size)

    @staticmethod
    def initWindow(window_size: str|list[int]|tuple[int]) -> pg.Surface:
        '''
        Daca window_size contine o lista de 2 valori care reprezinta marimea la window, creaza un window de marimele date.
        Daca window_size are valoarea de 'FULLSCREEN', creaza un window pe tot ecranul.
        '''

        if isinstance(window_size, (list, tuple)) and len(window_size) == 2:
            window = pg.display.set_mode(window_size)
        elif window_size == 'FULLSCREEN':
            window = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        else:
            raise ValueError('Invalid value for \'window_size\': Expected a list, tuple, or the string \'FULLSCREEN\'.')
        
        return window

    def run(self):
        self.__run = True

        asyncio.run(self.__asyncronRun())

    async def __asyncronRun(self):
        await self.__loop()
    
    async def __loop(self):
        while self.__run:
            self.__window.fill('black')
            
            # Verifica daca se apasa close la window, daca da, window se inchide
            for e in pg.event.get(): 
                self.__run = False if e.type == pg.QUIT else True

            await self.__functionLoader()

            pg.display.update()

    async def __functionLoader(self):
        '''
        Aceasta functie e pentru a indica ordinea de indiplinire a functiilor globale in joc
        '''
        await self.__scenes[self.__scene].loader()
        


if __name__ == '__main__':
    game = Game(window_size=(700, 700))
    game.run()
