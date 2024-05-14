from GameFrame import RoomObject

class Goal_Keeper1(RoomObject):
    """
    A class for the player's Goal Keeper (the paddle)
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the Goal Keeper object
        """
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Goal_Keeper1.jpg")
        self.set_image(image,100,100)