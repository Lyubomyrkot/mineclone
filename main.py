from ursina import *
from map import Map
from player import Player

app = Ursina()

sky = Sky(texture = 'sky_sunset',)
map = Map()
#map.new_map(20)
 
player = Player(position = (0, 15, 0))
map.player = player

map.load_map()

window.fullscreen = True
app.run()

# grass = Entity(model='models/grass/scene',
#                position=(0, -0.5, 1),
#                scale=0.5,)

# tree = Entity(model='models/tree/scene',
#                position=(-0.5, -2.5, 1.5),
#                scale=7,)

# bed = Entity(model='models/bed/scene',
#                 position=(0, 0.5, 1.5),
#                 scale=0.6,)

# coal_ore = Entity(model='models/coal_ore/scene',
#                 origin_y = 0.5,
#                 position=(-0.5, 1, 1.5),)

# cobblestone = Entity(model='models/cobblestone/scene',
#                position=(-0.5, 0.5, 1.5),)

# stone = Entity(model='models/stone/scene',
#                position=(0, 1, 1),
#                scale=0.5,)

# diamond_block = Entity(model='models/diamond_block/scene',
#                position=(-1.5, -0.5, 1.5),)

# diamond_ore = Entity(model='models/diamond_ore/scene',
#                 position=(-1.5, -0.5, -0.5),)


# EditorCamera()