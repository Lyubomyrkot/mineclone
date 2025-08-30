from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from map import Block

class Player(FirstPersonController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speed = 5

    def input(self, key):
        if key == 'left mouse down':
            aim = raycast(camera.world_position, camera.forward, distance=6)
            if aim.entity:
                destroy(aim.entity)

        if key == 'right mouse down':
            aim = raycast(camera.world_position, camera.forward, distance=6)
            if aim.entity:
                block = Block(pos=aim.entity.position + aim.normal)

        return super().input(key)