import random
from components.obstacles.obstacle import Obstacle

class Shoe(Obstacle):
    def __init__(self, image):
        self.index = random.randint(0,2)
        super().__init__(image, self.index)
        self.rect.y = 240
        self.rect.x = 2000