from config import *
from game.scripting.action import Action

class MoveActorsAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script):
        ship = cast.get_first_actor(SHIP_GROUP)
        ship.move_next()

        projectiles = cast.get_actors(PROJECTILE_GROUP)
        for projectile in projectiles:
            projectile.move_next()

        alien_grid = cast.get_first_actor(ALIEN_GROUP)
        for row in alien_grid:
            for alien in row:
                alien.move_next()