from ursina import *
from perlin_noise import PerlinNoise
from ursina.shaders import basic_lighting_shader, lit_with_shadows_shader
from random import randint
from numpy import floor

class Block(Entity):
    def __init__(self, pos, **kwargs):
        super().__init__(
            model='models/grass/scene.gltf', 
            scale=0.5,
            position=(pos),
            shader= basic_lighting_shader,
            collider='box'
        )
class Stone(Entity):
    def __init__(self, pos, **kwargs):
        super().__init__(
            model='models/stone/scene.gltf', 
            scale=0.5,
            position=(pos),
            shader= basic_lighting_shader,
            collider='box'
        )

class Tree(Entity):
    def __init__(self, pos, **kwargs):
        super().__init__(
            model='models/tree/scene.gltf', 
            scale=randint(5, 8),
            position=(pos),
            shader= basic_lighting_shader,
            collider='box',
            origin_y=0.5
        )

class Flower(Entity):
    def __init__(self, pos, **kwargs):
        super().__init__(
            model='models/flower/scene.gltf', 
            scale=1,
            position=(pos),
            shader= basic_lighting_shader,
            origin_y=0.5,
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
                block = Block(pos =(x, y-0.5, z))
                stone = Stone(pos =(x, y-1, z))

                n_tree = randint(1, 60)
                if n_tree == 1:
                    tree = Tree(pos=(x, y, z))

                n_flower = randint(1, 40)
                if n_flower == 1:
                    flower = Flower(pos=(x, y+1, z),)

                # n_stone = randint(1, 40)
                # if n_stone == 1:
                #     stone = Stone(pos=(x, y+1, z),)








        