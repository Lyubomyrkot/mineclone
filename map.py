from ursina import *
from perlin_noise import PerlinNoise
from ursina.shaders import basic_lighting_shader, lit_with_shadows_shader
from random import randint
from numpy import floor
import os
import pickle

BASE_DIR = os.getcwd()
TEXSTURE_DIR = os.path.join(BASE_DIR, 'blocks')

filename_list = os.listdir(TEXSTURE_DIR)
texture_list = []

for filename in filename_list:
    texture = load_texture(f'blocks/{filename}')
    texture_list.append(texture)






class Block_scrol(Entity):
    current = 0
    max_block = len(texture_list) - 1
    def __init__(self, pos, block_texture=0, **kwargs):
        super().__init__(
            model='cube', 
            scale=1,
            origin_y=-0.5,
            texture = texture_list[block_texture],
            position=(pos),
            shader= basic_lighting_shader,
            collider='box',
            **kwargs
        )
        scene.block_scrol[(self.x, self.y, self.z)] = block_texture

class Block(Entity):
    def __init__(self, pos, **kwargs):
        super().__init__(
            model='models/grass/scene.gltf', 
            scale=0.5,
            position=(pos),
            shader= basic_lighting_shader,
            collider='box',
            **kwargs
        )
        scene.block[(self.x, self.y, self.z)] = self

class Stone(Entity):
    def __init__(self, pos, **kwargs):
        super().__init__(
            model='models/stone/scene.gltf', 
            scale=0.5,
            position=(pos),
            shader= basic_lighting_shader,
            collider='box'
        )
        scene.stones[(self.x, self.y, self.z)] = self

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
        scene.trees[(self.x, self.y, self.z)] = self.scale

class Flower(Entity):
    def __init__(self, pos, **kwargs):
        super().__init__(
            model='models/flower/scene.gltf', 
            scale=1,
            position=(pos),
            shader= basic_lighting_shader,
            origin_y=0.5,
        )
        scene.flowers[(self.x, self.y, self.z)] = self

class Coal_ore(Entity):
    def __init__(self, pos, **kwargs):
        super().__init__(
            model='models/coal_ore/scene.gltf', 
            position=(pos),
            shader= basic_lighting_shader,
            collider='box',
            origin_x=0.5,
            origin_y=0.5,
            origin_z=0.5,
        )
        scene.coal_ore[(self.x, self.y, self.z)] = self


class Map(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        scene.block_scrol = {}# словник з блоками
        scene.block = {}
        scene.flowers = {}
        scene.trees = {}
        scene.stones = {}
        scene.coal_ore = {}

        self.noise = PerlinNoise(octaves=4, seed=2025)#шум перліна
        
        light = DirectionalLight(shadows=True)
        light.look_at(Vec3(1,-1,-1))
        

    def new_map(self, size = 15):
        for x in range(-size, size):
            for z in range(size):
                y = floor(self.noise([x/size, z/size]) * 6)
                block = Block(pos =(x, y-0.5, z))

                layer = 3
                while layer > 0:
                    pos = (x, y-layer, z)
                    stone = Stone(pos=pos)
                    layer -= 1
                    #self.blocks[pos] = stone

                n_tree = randint(1, 60)
                if n_tree == 1:
                    tree = Tree(pos=(x, y, z))

                n_flower = randint(1, 40)
                if n_flower == 1:
                    flower = Flower(pos=(x, y+1, z),)

                # n_coal_ore = randint(1, 10)
                # if n_coal_ore == 1:
                #     pos_coal_ore = (x, y-randint(1, 3), z)

                    # if pos_coal_ore in self.blocks:
                    #     destroy(self.blocks[pos_coal_ore])
                    #     del self.blocks[pos_coal_ore]

                    # coal_ore = Coal_ore(pos=pos_coal_ore)
                    # self.blocks[pos_coal_ore] = coal_ore
        
    def input(self, key):
        if key == "f":
            self.save_map()
        if key == "l":
            self.load_map()

    def save_map(self):
        game_data = {
            'player_pos': (self.player.x, self.player.y, self.player.z),
            'block_scrol_pos': [(pos, block_texture) for pos, block_texture in scene.block_scrol.items()],
            "trees_pos": [(pos, scale) for pos, scale in scene.trees.items()],

            "flowers_pos": [pos for pos, flowers in scene.flowers.items()],

            "stones_pos": [pos for pos, stones in scene.stones.items()],
            "coal_ore_pos": [pos for pos, coal_ore in scene.coal_ore.items()],
            "block_pos": [pos for pos, block in scene.block.items()],

        }
        with open('save_map.dat', 'wb') as f:
            pickle.dump(game_data, f)
        
    def load_map(self):
        with open('save_map.dat', 'rb') as f:
            game_data = pickle.load(f)
            self.player.position = game_data['player_pos']

            for pos, block_texture in game_data['block_scrol_pos']:
                Block_scrol(pos, block_texture)
            for pos in game_data['block_pos']:
                Block(pos)
            for pos, scale in game_data['trees_pos']:
                Tree(pos, scale=scale)
            for pos in game_data['flowers_pos']:
                Flower(pos)
            for pos in game_data['stones_pos']:
                Stone(pos)
            for pos in game_data['coal_ore_pos']:
                Coal_ore(pos)
            
