'''
Folders settings for help to reduce the code
'''
import os

# Folders Settings

## Main folder
MAIN_FOLDER = os.path.dirname(__file__)

## Resources directory
RESOURCES_FOLDER = os.path.join(MAIN_FOLDER, 'resources')

## Resources subdirectories
FONTS_FOLDER = os.path.join(RESOURCES_FOLDER, 'fonts')
IMAGES_FOLDER = os.path.join(RESOURCES_FOLDER, 'images')
SOUNDS_FOLDER = os.path.join(RESOURCES_FOLDER, 'sounds')

### Images subdirectories
SHIP_FOLDER = os.path.join(IMAGES_FOLDER, 'ship')
METEORS_FOLDER = os.path.join(IMAGES_FOLDER, 'meteors')

#### Ship subdirectories
EXPLOSION_FOLDER = os.path.join(SHIP_FOLDER, 'explosion_animation')