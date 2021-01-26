import pygame as pg
import sys, os

from tools import *
from folders import *
from config import *

class How_To:

    def __init__(self):
        self.running = True

    def show_screen(self, screen):
        while self.running:
            self._handle_events()
            if self.running:
                self._draw_screen(screen)
        self.running = True

    def _handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                self._keydown_events(event)

    def _keydown_events(self, event):
        if event.key == pg.K_ESCAPE:
            self.running = False

    def _draw_screen(self, screen):
        screen.fill(BLUE)
        create_draw_text(screen, SPACE2, 54, 'INSTRUCCTIONS', WHITE, position='topcenter', width=WIDTH, height=HEIGHT)

        pg.display.update()
