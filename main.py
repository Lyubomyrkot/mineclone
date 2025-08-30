from ursina import *
from map import Map
from player import Player

app = Ursina()

sky = Sky(texture = 'sky_sunset',)

map = Map()
map.new_map(30)

player = Player(position = (0, 15, 0))

# grass = Entity(model='models/grass/scene',
#                position=(0, -0.5, 1),
#                scale=0.5,)

# grass1 = Entity(model='models/grass/scene',
#                 position=(0, -0.5, -1),
#                 scale=0.5,)

# grass2 = Entity(model='models/grass/scene',
#                 position=(0, -0.5, 0),
#                 scale=0.5,)

# grass3 = Entity(model='models/grass/scene',
#                 position=(1, -0.5, 0),
#                 scale=0.5,)

# grass4 = Entity(model='models/grass/scene',
#                 position=(-1, -0.5, 0),
#                 scale=0.5,)

# tree = Entity(model='models/tree/scene',
#                position=(-0.5, -2.5, 0.5),
#                scale=7,)

# bed = Entity(model='models/bed/scene',
#                 position=(2, 0, 2),
#                 scale=0.5,)

# coal_ore = Entity(model='models/coal_ore/scene',
#                 position=(0.5, -0.5, -0.5),)

# cobblestone = Entity(model='models/cobblestone/scene',
#                position=(0.5, -0.5, 1.5),)

# diamond_block = Entity(model='models/diamond_block/scene',
#                position=(-1.5, -0.5, 1.5),)

# diamond_ore = Entity(model='models/diamond_ore/scene',
#                 position=(-1.5, -0.5, -0.5),)
#EditorCamera()
app.run()