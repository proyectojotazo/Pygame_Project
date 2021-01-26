from the_quest.game_screen.game import *
from the_quest.title_screen.title import *

if __name__ == "__main__":
    i = TitleScreen()
    i.title_screen()
    game = Screen()
    game.new_game()