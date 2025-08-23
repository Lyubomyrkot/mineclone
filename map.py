from ursina import *
from perlin_noise import PerlinNoise
from ursina.shaders import basic_lighting_shader, lit_with_shadows_shader
from random import randint
from numpy import floor

class Block(Entity):
    def __init__(self, pos, **kwargs):
        super().__init__(
            model='cube', 
            scale=1, 
            texture='blocks/0.png', 
            position=(pos),
            shader= basic_lighting_shader,
            collider='box'
        )

class Map(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.blocks = {}# словник з блоками
        self.noise = PerlinNoise(octaves=4, seed=2025)#шум перліна
        
        light = DirectionalLight(shadows=True)
        light.look_at(Vec3(1,-1,-1))
        

    def new_map(self, size = 15):
        for x in range(-size, size):
            for z in range(size):
                y = floor(self.noise([x/size, z/size]) * 6)
                block = Block(pos =(x, y, z))



        