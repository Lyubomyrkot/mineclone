from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import basic_lighting_shader, lit_with_shadows_shader
from map import Block_scrol, texture_list, Block, Stone, Flower, Tree, Coal_ore

class Player(FirstPersonController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speed = 5
        self.hand_block = Entity(parent=camera.ui, 
                                 model='cube', 
                                 texture=texture_list[Block_scrol.current],
                                 scale=0.2,
                                 shader=basic_lighting_shader,
                                 rotation=Vec3(30, -30, 10),
                                 position=Vec2(0.6, -0.4))

    def input(self, key):
        if key == 'left mouse down':
            aim = raycast(camera.world_position, camera.forward, distance=6)
            if aim.hit:
                if isinstance(aim.entity, Block_scrol):
                    x,y,z = aim.entity.x, aim.entity.y, aim.entity.z
                    del scene.block_scrol[(x,y,z)]
                if isinstance(aim.entity, Block):
                    x,y,z = aim.entity.x, aim.entity.y, aim.entity.z
                    del scene.block[(x,y,z)]
                if isinstance(aim.entity, Stone):
                    x,y,z = aim.entity.x, aim.entity.y, aim.entity.z
                    del scene.stones[(x,y,z)]
                if isinstance(aim.entity, Tree):
                    x,y,z = aim.entity.x, aim.entity.y, aim.entity.z
                    del scene.trees[(x,y,z)]
                if isinstance(aim.entity, Flower):
                    x,y,z = aim.entity.x, aim.entity.y, aim.entity.z
                    del scene.flowers[(x,y,z)]
                if isinstance(aim.entity, Coal_ore):
                    x,y,z = aim.entity.x, aim.entity.y, aim.entity.z
                    del scene.coal_ores[(x,y,z)]
                
                destroy(aim.entity)

        if key == 'right mouse down':
            aim = raycast(camera.world_position, camera.forward, distance=6)
            if aim.entity:
                block = Block_scrol(pos=aim.entity.position + aim.normal, block_texture=Block_scrol.current)
        
        if key == 'scroll up':
            Block_scrol.current += 1
            if Block_scrol.current >= Block_scrol.max_block:
                Block_scrol.current = 0
            self.hand_block.texture = texture_list[Block_scrol.current]
        
        if key == 'scroll down':
            Block_scrol.current -= 1
            if Block_scrol.current < 0:
                Block_scrol.current = Block_scrol.max_block
            self.hand_block.texture = texture_list[Block_scrol.current]
        
        if key == 'escape':
            application.quit()
        
        if key == 'left shift':
            self.speed = 7
        if key == 'left shift up':
            self.speed = 5

        if key == 'c':
            if self.gravity == 1:
                self.gravity = 0
            else:
                self.gravity = 1

        return super().input(key)