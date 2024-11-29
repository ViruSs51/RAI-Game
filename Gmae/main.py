import pygame as pg
import asyncio


class Game:
    __run = False

    def __init__(self, window_size: list[int]|tuple[int], title='RAI Game'):
        self.w_size = window_size

        pg.init()
        self.window = pg.display.set_mode(self.w_size)
        
        pg.display.set_caption(title)

    def run(self):
        self.__run = True

        asyncio.run(self.__asyncronRun())

    async def __asyncronRun(self):
        await self.__loop()
    
    async def __loop(self):
        while self.__run:
            for e in pg.event.get():
                self.__run = False if e.type == pg.QUIT else True

            await self.__functionLoader()

            pg.display.update()

    async def __functionLoader(self):
        '''
        Aceasta functie e pentru a indica ordinea de indiplinire a functiilor globale in joc
        '''
        pass

if __name__ == '__main__':
    game = Game(window_size=(700, 700))
    game.run()
