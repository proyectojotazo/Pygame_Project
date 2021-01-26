import pygame as pg

import os, sys

from the_quest.title_screen.how_to import *

from config import *
from folders import *
from tools import *



class TitleScreen:

    

    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(GAME_TITLE)

        self.ship_img = load_image(SHIP_FOLDER, 'ship.xcf', rect=False)

        self.starting = True

        self.htp = How_To()

        # Vars initial animation
        self.x_pos_ship = 800
        self.y_pos_ship = 110
        self.x_pos_title = 848
        self.y_pos_title = 75

        # Option selected
        self.option = 0

        # Sounds
        self.title_sound = load_sound(SOUNDS_FOLDER, 'title-screen.wav')
        self.title_sound.set_volume(BACKGROUND_VOL)

        self.clock = pg.time.Clock()

    def title_screen(self):
        self.title_sound.play()
        self._intial_animation()        
        while self.starting:
            dt = self.clock.tick(FPS)
            self._handle_events()
            if self.starting:
                self._draw_screen()
            pg.display.flip()
        self.starting = True

    def _handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                self._keydown_events(event)

    def _keydown_events(self, event):
        if event.key == pg.K_DOWN:
            if self.option < 3:
                self.option += 1
                OPTION_SOUND.play()
        if event.key == pg.K_UP:
            if self.option > 0:
                self.option -= 1
                OPTION_SOUND.play()
        if event.key == pg.K_SPACE:
            SELECTED_SOUND.play()
            self._check_op(self.option)
        if event.key == pg.K_ESCAPE:
            pg.quit()
            sys.exit()

    def _check_op(self, option):
        if option == 0:
            # Start New Game
            self.starting = False
            self._fade_start()
            self.title_sound.stop()
        elif option == 1:
            # How To Play Screen
            self.htp.show_screen(self.screen)        
        elif option == 2:
            # Records Screen
            pass
        else:
            # Exit Game
            pg.quit()
            sys.exit()

    def _intial_animation(self):
        running = True
        while running:
            dt = self.clock.tick(FPS)

            self.screen.fill(BLACK)

            load_and_draw_image(self.screen, SHIP_FOLDER, 'ship-title.png', x=self.x_pos_ship, y=self.y_pos_ship)
            create_draw_text(self.screen, TITLE, 120, 'THE QUEST', WHITE, pos_x=self.x_pos_title, pos_y=self.y_pos_title)
            self.x_pos_ship -= 5
            if self.x_pos_title > 66.0:
                self.x_pos_title -= 5
                print(self.x_pos_title)
            else:
                pass
            if self.x_pos_ship <= -55:
                running = False
            
            pg.display.flip()
            
    def _draw_screen(self):

        self.screen.fill(BLACK)
        self._draw_title()
        self._draw_options()
        
    def _draw_title(self):
        create_draw_text(self.screen, TITLE, 120, 'THE QUEST', WHITE, position='topcenter', width=WIDTH, height=HEIGHT)

    def _draw_options(self):
        if self.option == 0:
            create_draw_text(self.screen, SPACE, 24, 'New Game', RED, position='center', width=WIDTH, height=HEIGHT)
            create_draw_text(self.screen, SPACE, 24, 'How To Play', WHITE, position='closecenterbottom', width=WIDTH, height=HEIGHT)
            create_draw_text(self.screen, SPACE, 24, 'Records', WHITE, position='closecenterbottom2', width=WIDTH, height=HEIGHT)
            create_draw_text(self.screen, SPACE, 24, 'Exit', WHITE, position='closecenterbottom3', width=WIDTH, height=HEIGHT)
        elif self.option == 1:
            create_draw_text(self.screen, SPACE, 24, 'New Game', WHITE, position='center', width=WIDTH, height=HEIGHT)
            create_draw_text(self.screen, SPACE, 24, 'How To Play', RED, position='closecenterbottom', width=WIDTH, height=HEIGHT)
            create_draw_text(self.screen, SPACE, 24, 'Records', WHITE, position='closecenterbottom2', width=WIDTH, height=HEIGHT)
            create_draw_text(self.screen, SPACE, 24, 'Exit', WHITE, position='closecenterbottom3', width=WIDTH, height=HEIGHT)
        elif self.option == 2:
            create_draw_text(self.screen, SPACE, 24, 'New Game', WHITE, position='center', width=WIDTH, height=HEIGHT)
            create_draw_text(self.screen, SPACE, 24, 'How To Play', WHITE, position='closecenterbottom', width=WIDTH, height=HEIGHT)
            create_draw_text(self.screen, SPACE, 24, 'Records', RED, position='closecenterbottom2', width=WIDTH, height=HEIGHT)
            create_draw_text(self.screen, SPACE, 24, 'Exit', WHITE, position='closecenterbottom3', width=WIDTH, height=HEIGHT)
        else:
            create_draw_text(self.screen, SPACE, 24, 'New Game', WHITE, position='center', width=WIDTH, height=HEIGHT)
            create_draw_text(self.screen, SPACE, 24, 'How To Play', WHITE, position='closecenterbottom', width=WIDTH, height=HEIGHT)
            create_draw_text(self.screen, SPACE, 24, 'Records', WHITE, position='closecenterbottom2', width=WIDTH, height=HEIGHT)
            create_draw_text(self.screen, SPACE, 24, 'Exit', RED, position='closecenterbottom3', width=WIDTH, height=HEIGHT)

    def _fade_start(self):
        fade = pg.Surface((WIDTH, HEIGHT))
        fade.fill((BLACK))
        bg_img = load_image(IMAGES_FOLDER, 'background.xcf', rect=False)
        alpha = 0
        vol = BACKGROUND_VOL
        for alpha in range(0, 255):
            fade.set_alpha(alpha)
            vol -= 0.00075
            self.title_sound.set_volume(vol)
            self._draw_screen()
            self.screen.blit(fade, (0,0))
            pg.display.flip()
            pg.time.delay(5)
        for alpha in range(255, 0, -1):
            fade.set_alpha(alpha)
            self.screen.blit(bg_img, (0,0))
            self.screen.blit(fade, (0,0))
            pg.display.flip()
            pg.time.delay(5)