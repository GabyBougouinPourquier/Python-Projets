import pyscroll
import pytmx
from player import Player
from screen import Screen


class Map:
    def __init__(self, screen: Screen):
        self.screen: Screen = screen
        self.tmx_data: pytmx.TiledMap
        self.map_layer: pyscroll.BufferedRenderer
        self.group: pyscroll.PyscrollGroup

        self.switch_map("map1")
        self.player: Player

    def switch_map(self, map: str):
        self.tmx_data = pytmx.load_pygame(f"../assets/map/{map}.tmx")
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size())
        self.map_layer.zoom = 3
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=7)

    def add_player(self, player) -> None:
        self.group.add(player)
        self.player = player
        self.player.align_hitbox()

    def update(self) -> None:
        self.group.update()
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen.get_display())
