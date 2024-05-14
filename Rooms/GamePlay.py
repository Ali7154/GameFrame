from GameFrame import Level
from Objects.Goal_Keeper1 import Goal_Keeper1

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Background.png")

        # add objects
        self.add_room_object(Goal_Keeper1(self, 25, 50))