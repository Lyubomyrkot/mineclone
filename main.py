from ursina import *

app = Ursina()

sky = Sky(texture = 'sky_sunset',)

grass = Entity(model='models/grass/scene',
               position=(0, -0.5, 1),
               scale=0.5,)

grass1 = Entity(model='models/grass/scene',
                position=(0, -0.5, -1),
                scale=0.5,)

grass2 = Entity(model='models/grass/scene',
                position=(0, -0.5, 0),
                scale=0.5,)

grass3 = Entity(model='models/grass/scene',
                position=(1, -0.5, 0),
                scale=0.5,)

grass4 = Entity(model='models/grass/scene',
                position=(-1, -0.5, 0),
                scale=0.5,)

tree = Entity(model='models/tree/scene',
               position=(-0.5, -2.5, 0.5),
               scale=7,)
    
EditorCamera()
app.run()