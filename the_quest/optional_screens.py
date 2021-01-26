import pygame as pg

import os, sys

from config import *
from folders import *
from tools import *

class PauseScreen:
    
    def __init__(self):

        self.option = 0
        self.paused = True
        self.reset = False

    def on_pause(self, screen):
        '''
        Mainloop of Pause
        '''
        self.reset = False
        pg.mixer.pause()
        while self.paused:
            self._handle_events()
            self._draw_paused_menu(self.option, screen)
        self.paused = True
        self.option = 0
        return self.reset

    def _handle_events(self):
        '''
        Handling events
        '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                self._keydown_events(event)

    def _keydown_events(self, event):
        '''
        Handling keydown events
        '''
        if event.key == pg.K_ESCAPE:
            self.paused = False
        if event.key == pg.K_DOWN:
            if self.option < 2:
                OPTION_SOUND.play()
                self.option += 1
        if event.key == pg.K_UP:
            if self.option > 0:
                OPTION_SOUND.play()
                self.option -= 1
        if event.key == pg.K_RETURN:
            SELECTED_SOUND.play()
            self._check_op(self.option)

    def _check_op(self, option):
        '''
        Method that checks the option selected
        Selected Continue -> option = 0
        Selected Restart -> option = 1
        Selected Quit -> option = 2
        '''
        if option == 0:
            self.paused = False
            pg.mixer.unpause()
        if option == 1:
            self.paused = False
            self.reset = True
        if option == 2:
            pg.quit()
            sys.exit()

    def _draw_paused_menu(self, option, screen):
        #TODO: Try to refactor this
        '''
        Method that draws the Pause menu
        Draws with red color the selected option
        '''

        load_and_draw_image(screen, IMAGES_FOLDER, 'pause1.png', x=200, y=170)

        if option == 0:
            create_draw_text(screen, SPACE, 24, 'Continue', RED, position='center', width=WIDTH, height=HEIGHT)
            create_draw_text(screen, SPACE, 24, 'Restart', WHITE, position="closecenterbottom", width=WIDTH, height=HEIGHT)
            create_draw_text(screen, SPACE, 24, 'Quit', WHITE, position="closecenterbottom2", width=WIDTH, height=HEIGHT)
        elif option == 1:
            create_draw_text(screen, SPACE, 24, 'Continue', WHITE, position='center', width=WIDTH, height=HEIGHT)
            create_draw_text(screen, SPACE, 24, 'Restart', RED, position="closecenterbottom", width=WIDTH, height=HEIGHT)
            create_draw_text(screen, SPACE, 24, 'Quit', WHITE, position="closecenterbottom2", width=WIDTH, height=HEIGHT)
        else:
            create_draw_text(screen, SPACE, 24, 'Continue', WHITE, position='center', width=WIDTH, height=HEIGHT)
            create_draw_text(screen, SPACE, 24, 'Restart', WHITE, position="closecenterbottom", width=WIDTH, height=HEIGHT)
            create_draw_text(screen, SPACE, 24, 'Quit', RED, position="closecenterbottom2", width=WIDTH, height=HEIGHT)

        create_draw_text(screen, SPACE2, 48, 'PAUSE', WHITE, position='closecenterup', width=WIDTH, height=HEIGHT)
        pg.display.flip()

class BlackScreen:
    
    def __init__(self):
        self.start = False
        self.ship_img, self.ship_rect = load_image(SHIP_FOLDER, 'ship.xcf')
        self.ticks = 0

    def on_black(self, screen, lifes):
        '''
        Mainloop for black screen
        '''
        while not self.start:
            dt = pg.time.Clock().tick(FPS)
            self.ticks += dt
            self._handle_events()
            self._update_screen(screen, lifes)
        self.start = False
        self.ticks = 0

    def _handle_events(self):
        '''
        Handling events
        '''
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.start = True
    
    def _update_screen(self, screen, lifes):
        # TODO: Function for blink text
        '''
        Method that draws and update the black screen
        '''
        screen.fill(BLACK)

        create_draw_text(screen, SPACE2, 32, 'Level 1 - 1', WHITE, position='closecenterup', width=WIDTH, height=HEIGHT)
        create_draw_text(screen, SPACE, 16, 'Lifes - ', WHITE, position='closecenterleft', width=WIDTH, height=HEIGHT)

        x_pos_lifes = 0
        for life in range(lifes):
            screen.blit(self.ship_img, ((WIDTH/2-(self.ship_rect.w/2))+x_pos_lifes, HEIGHT/2-(self.ship_rect.w/2)))
            x_pos_lifes += self.ship_rect.w

        if self.ticks <= 500:
            create_draw_text(screen, SPACE, 16, 'Press < SPACE > to start', WHITE, position='bottomcenter', width=WIDTH, height=HEIGHT)
        elif self.ticks <= 1000:
            pass
        else:
            self.ticks = 0

        pg.display.flip()