from pygame import Surface


class Scene:

    def __init__(self, window: Surface):
        self._window = window


    async def loadAssets(self):
        pass
    async def loader(self):
        '''
        Se indica toate obiectele si logica pe scena
        '''