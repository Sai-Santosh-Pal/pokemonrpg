from settings import *
from pytmx.util_pygame import load_pygame
from os.path import join
from os.path import dirname
from os.path import abspath

from sprites import Sprite, AnimatedSprite
from entities import Player, Character
from groups import AllSprites

from support import *

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('PokemonRPG')
        self.clock = pygame.time.Clock()

        self.all_sprites = AllSprites()

        self.import_assets()
        self.setup(self.tmx_maps['world'], 'house')

    def import_assets(self):
        BASE_DIR = dirname(abspath(__file__))
        self.tmx_maps = {
            'world': load_pygame(join(BASE_DIR, '..', 'data', 'maps', 'world.tmx')),
            'hospital': load_pygame(join(BASE_DIR, '..', 'data', 'maps', 'hospital.tmx')),
            }
        # print("\n")
        # print("\n")
        # print(BASE_DIR, '..', 'graphics', 'tilesets', 'coast')
        # print("\n")
        # print("\n")

        self.overworld_frames = {
            'water': import_folder(BASE_DIR, '..', 'graphics', 'tilesets', 'water'),
            'coast': coast_importer(24, 12, BASE_DIR, '..', 'graphics', 'tilesets', 'coast'),
            'characters': all_character_import(BASE_DIR, '..', 'graphics', 'characters')
        }
        
    def setup(self, tmx_map, player_start_pos):
        for layer in ['Terrain', 'Terrain Top']:
            for x,y, surf in tmx_map.get_layer_by_name(layer).tiles():
                Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites, WORLD_LAYERS['bg'])

        for x,y, surf in tmx_map.get_layer_by_name('Terrain Top').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)

        for obj in tmx_map.get_layer_by_name('Water'):
            for x in range(int(obj.x), int(obj.x + obj.width), TILE_SIZE):
                for y in range(int(obj.y), int(obj.y + obj.height), TILE_SIZE):
                    AnimatedSprite((x,y), self.overworld_frames['water'], self.all_sprites, WORLD_LAYERS['water'])

        for obj in tmx_map.get_layer_by_name('Coast'):
            terrain = obj.properties['terrain']
            side = obj.properties['side']
            # print(self.overworld_frames['coast'])
            AnimatedSprite((obj.x, obj.y), self.overworld_frames['coast'][terrain][side], self.all_sprites, WORLD_LAYERS['bg'])

        for obj in tmx_map.get_layer_by_name('Objects'):
            if obj.name == 'top':
                Sprite((obj.x, obj.y), obj.image, self.all_sprites, WORLD_LAYERS['top'])
            else:
                Sprite((obj.x, obj.y), obj.image, self.all_sprites)

        for obj in tmx_map.get_layer_by_name('Monsters'):
            Sprite((obj.x, obj.y), obj.image, self.all_sprites)
        
        for obj in tmx_map.get_layer_by_name("Entities"):
            if obj.name == "Player":
                if obj.properties['pos'] == player_start_pos:
                    self.player = Player(
                        pos = (obj.x, obj.y), 
                        frames = self.overworld_frames['characters']['player'], 
                        groups = self.all_sprites,
                        facing_direction = obj.properties['direction'])
            else:
                Character(
                    pos = (obj.x, obj.y), 
                    frames = self.overworld_frames['characters'][obj.properties['graphic']], 
                    groups = self.all_sprites,
                    facing_direction = obj.properties['direction'])


    def run(self):
        while True:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.exit()
                    exit()

            self.all_sprites.update(dt)
            self.display_surface.fill('black')
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()

