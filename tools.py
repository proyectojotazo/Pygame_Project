'''
Tools for help to load and draw some stuff
'''

import pygame as pg

import os

# IMAGES TOOLS

def load_image(path, img, x=0, y=0, rect=True):
    '''
    Function that returns image and rect.
    path = It's a "os" folder
    img = name of the image that we want to load
    x,y = If we don't change it's equals to 0, it works when we need to choose a different x,y for our rect
    rect = The rect parameter works:
        - If we want the rect of the image, we use as default True
        - If we only need to take the image, we use rect=False, then, only returns the image
    '''

    if rect:
        img = pg.image.load(os.path.join(path, img))
        rect = img.get_rect(x=x, y=y)

        return img, rect

    else:
        img = pg.image.load(os.path.join(path, img))

        return img

def load_and_draw_image(screen, path, img, x=0, y=0):
    '''
    Method that loads and draws the image at same time
    '''
    img = pg.image.load(os.path.join(path, img))
    rect = img.get_rect()

    screen.blit(img, (x, y))

# TEXT TOOLS

def create_draw_text(screen, font, size, text, color, position='', pos_x=0, pos_y=0, width=0, height=0, antialias=True):
    '''
    Function that draws text on the screen
    screen = the surface where we want to draw the text
    font = path where we have the font and the font name
    size = size for the text
    color = color for the text
    ---default params---
    position:
        If we want an specific position for the text we have to
        indicate, as, topcenter, center, closecenterup, closecenterleft,
        and bottomcenter.
            topcenter= takes the center of text size and puts centered in width
                        and top of the screen
            center = puts the text on the center of the screen
            closecenterup = takes the center of text size and puts centered in width
                        and centered in height but more closer to top
            closecenterleft = puts the text shifted a little bit to left
            closecenterbottom = takes the center of text size and puts centered in width
                        and centered in height but more closer to bottom
            closecenterbottom2 = same as closecenterbottom but a little bit lower
            closecenterbottom3 = same as closecenterbottom2 but a little bit lower
            bottomcenter = puts the text centered on width and closer to bottom
                        margin of the screen
        If we choose to add position param, we must to use also width and height
        and recommendable to use also pos_x and pos_y
        width and height are the params we use to move the text centered
        pos_x and pos_y are the initial pos that we want to draw our text    
    '''
    
    msg_font = pg.font.Font(font, size)
    msg_txt = msg_font.render(text, antialias, color)

    if position == 'topcenter':
        pos_x = width/2-(msg_txt.get_size()[0]//2)
        pos_y = 75
    if position == 'center':
        pos_x = width/2-(msg_txt.get_size()[0]//2)
        pos_y = height/2-(msg_txt.get_size()[1]//2)
    if position == 'closecenterup':
        pos_x = width/2-(msg_txt.get_size()[0]//2)
        pos_y = (height/2)//1.5
    if position == 'closecenterleft':
        pos_x = width/2-(msg_txt.get_size()[0]//0.8)
        pos_y = height/2-(msg_txt.get_size()[1]//2)
    if position == 'closecenterbottom':
        pos_x = width/2-(msg_txt.get_size()[0]//2)
        pos_y = height//1.7-(msg_txt.get_size()[1]//2)
    if position == 'closecenterbottom2':
        pos_x = width/2-(msg_txt.get_size()[0]//2)
        pos_y = height//1.49-(msg_txt.get_size()[1]//2)
    if position == 'closecenterbottom3':
        pos_x = width/2-(msg_txt.get_size()[0]//2)
        pos_y = height//1.32-(msg_txt.get_size()[1]//2)
    if position == 'bottomcenter':
        pos_x = width/2-(msg_txt.get_size()[0]//2)
        pos_y = height/1.2-(msg_txt.get_size()[1]//2)

    # if position:
    #     screen.blit(msg_txt, (positions[position][pos_x], positions[position][pos_y]))
    # else:
    screen.blit(msg_txt, (pos_x, pos_y))

# SOUNDS TOOLS
    
def load_sound(path, sound):
    '''
    Function that returns a sound loaded.
    path = It's the path of the sound
    sound = name of the sound that we want to load. Ex: 'sound.wav'
    '''

    sound = pg.mixer.Sound(os.path.join(path, sound))

    return sound

