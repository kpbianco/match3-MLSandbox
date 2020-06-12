'''
Kian's ML Match 3 Playground
A simple match three game that enables a reinforcement learning model for demo

https://github.com/kpbianco/match3-MLSandbox
Released under the GNU General Public License
'''

VERSION = "0.2"

try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    from socket import*
    from pygame.locals import *


# Says which module couldn't load properly if there is one
except ImportError as err:
    print(f"couldn't load module {err}".format(err))
    sys.exit(2)


#  Resources
class images:

    def load_png(name):
        fullname = os.path.join('./static', name)
        try:
            image = pygame.image.load(fullname)

            if image.get_alpha() is None:
                image = image.convert()

        except pygame.error as message:
            print('Cannot load image:' + fullname)
            raise SystemExit(message)
        return image, image.get_rect()


class sounds:

    def load_sound(name):

        class NoneSound:
            def play(self):
                pass

        if not pygame.mixer:
            return NoneSound()

        fullname = os.path.join('./static', name)
        try:
            sound = pygame.mixer.Sound(fullname)

        except pygame.error as message:
            #  Double check this "wav" is the right thing
            print('Cannot load sound:' + wav)
            raise SystemExit(message)
        return sound


#  Game Objects
class falling_board:
    '''
    A 9x9 array storing the gems, with a 81 gem buffer above the other 81 sized
    board, it includes checking matches, and shifting the matches down after
    success
    '''
    board_array = []

    def __init__(self):
        self.board_array = [0] * 162

        for i in range(len(self.board_array)):
            self.board_array[i] = random.randint(1, 6)

    def check_if_match_horizontal(self, lowest):
        #  The max index that needs to be checked is 117 out of the 162, no error there
        if self.board_array[lowest] == self.board_array[lowest + 18] == self.board_array[lowest + 36] == self.board_array[lowest + 54] == self.board_array[lowest + 72] == self.board_array[lowest + 90] == self.board_array[lowest + 108] == self.board_array[lowest + 126] == self.board_array[lowest + 144]:
            return 9
        elif self.board_array[lowest] == self.board_array[lowest + 18] == self.board_array[lowest + 36] == self.board_array[lowest + 54] == self.board_array[lowest + 72] == self.board_array[lowest + 90] == self.board_array[lowest + 108] == self.board_array[lowest + 126]:
            return 8
        elif self.board_array[lowest] == self.board_array[lowest + 18] == self.board_array[lowest + 36] == self.board_array[lowest + 54] == self.board_array[lowest + 72] == self.board_array[lowest + 90] == self.board_array[lowest + 108]:
            return 7
        elif self.board_array[lowest] == self.board_array[lowest + 18] == self.board_array[lowest + 36] == self.board_array[lowest + 54] == self.board_array[lowest + 72] == self.board_array[lowest + 90]:
            return 6
        elif self.board_array[lowest] == self.board_array[lowest + 18] == self.board_array[lowest + 36] == self.board_array[lowest + 54] == self.board_array[lowest + 72]:
            return 5
        elif self.board_array[lowest] == self.board_array[lowest + 18] == self.board_array[lowest + 36] == self.board_array[lowest + 54]:
            return 4
        elif self.board_array[lowest] == self.board_array[lowest + 18] == self.board_array[lowest + 36]:
            return 3
        else:
            return -1

    def check_if_match_vertical(self, lowest):
        if self.board_array[lowest] == self.board_array[lowest + 1] == self.board_array[lowest + 2] == self.board_array[lowest + 3] == self.board_array[lowest + 4] == self.board_array[lowest + 5] == self.board_array[lowest + 6] == self.board_array[lowest + 7] == self.board_array[lowest + 8]:
            return 9
        elif self.board_array[lowest] == self.board_array[lowest + 1] == self.board_array[lowest + 2] == self.board_array[lowest + 3] == self.board_array[lowest + 4] == self.board_array[lowest + 5] == self.board_array[lowest + 6] == self.board_array[lowest + 7]:
            return 8
        elif self.board_array[lowest] == self.board_array[lowest + 1] == self.board_array[lowest + 2] == self.board_array[lowest + 3] == self.board_array[lowest + 4] == self.board_array[lowest + 5] == self.board_array[lowest + 6]:
            return 7
        elif self.board_array[lowest] == self.board_array[lowest + 1] == self.board_array[lowest + 2] == self.board_array[lowest + 3] == self.board_array[lowest + 4] == self.board_array[lowest + 5]:
            return 6
        elif self.board_array[lowest] == self.board_array[lowest + 1] == self.board_array[lowest + 2] == self.board_array[lowest + 3] == self.board_array[lowest + 4]:
            return 5
        elif self.board_array[lowest] == self.board_array[lowest + 1] == self.board_array[lowest + 2] == self.board_array[lowest + 3]:
            return 4
        elif self.board_array[lowest] == self.board_array[lowest + 1] == self.board_array[lowest + 2]:
            return 3
        else:
            return -1

    def delete_match(self, h_or_v, lowest, length):
        if length == -1:
            return  # implement gem going back to original position and adding score

        if h_or_v == 'h':
            for i in length:
                self.board_array[lowest + (i * 16)] = 0
            if length == 3:
                multiplier.increase_mult()
                # add score
            if length == 4:
                multiplier.big_mult(2)
                # add score
                multiplier.revert_mult()
            if length == 5:
                multiplier.big_mult(5)
                # add score
                multiplier.revert_mult()
            if length == 6:
                multiplier.big_mult(10)
                # add score
                multiplier.revert_mult()
            if length == 7:
                multiplier.big_mult(15)
                # add score
                multiplier.revert_mult()
            if length == 8:
                multiplier.big_mult(25)
                # add score
                multiplier.revert_mult()
            if length == 9:
                multiplier.big_mult(50)
                # add score
                multiplier.revert_mult()

        if h_or_v == 'v':
            for i in length:
                self.board_array[lowest + i] = 0  # implement adding score and multiplier after
            if length == 3:
                multiplier.increase_mult()
                # add score
            if length == 4:
                multiplier.big_mult(2)
                # add score
                multiplier.revert_mult()
            if length == 5:
                multiplier.big_mult(5)
                # add score
                multiplier.revert_mult()
            if length == 6:
                multiplier.big_mult(10)
                # add score
                multiplier.revert_mult()
            if length == 7:
                multiplier.big_mult(15)
                # add score
                multiplier.revert_mult()
            if length == 8:
                multiplier.big_mult(25)
                # add score
                multiplier.revert_mult()
            if length == 9:
                multiplier.big_mult(50)
                # add score
                multiplier.revert_mult()

    def shift_down(self, h_or_v, lowest):
        if h_or_v == 'h':
            next_val = self.board_array[lowest]
            while next_val == 0:
                for i in range(18 - (lowest % 18)):
                    try:
                        self.board_array[lowest] == self.board_array[(lowest + i)]
                        lowest += 1
                    except IndexError:
                        self.board_array[i] = random.randint(1, 6)
                next_val += 16
                lowest = next_val

        if h_or_v == 'v':
            next_val = self.board_array[lowest]
            while next_val == 0:
                self.board_array[lowest] == self.board_array[(lowest + 1)]
                lowest += 1
            for i in range(18 - (lowest % 18)):
                try:
                    self.board_array[lowest] == self.board_array[(lowest + i)]
                    lowest += 1
                except IndexError:
                    self.board_array[i] = random.randint(1, 6)


class gems:
    '''
    Create an object that can store one of six values, which is the color
    of the gem and make it movable horizontally and vertically by one space,
    check if match with falling board and revert if none occurs; it follows the
    board's physics and contributes to the score
    '''

    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = images.load_png('./static/gem.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector

    def horizontal_swap(self):
        mouse = pygame.mouse

        if mouse.get_pressed():
            if mouse.get_rel(-10, 0) or mouse.get_rel(10, 0):
                # gem at start mouse position switches to the Left or right
                if check_if_match_vertical() is not -1:
                    length = check_if_match_vertical()
                    falling_board.delete_match('v', find a way to determine lowest based off of the swapped direction, length )
                    falling_board.shift_down('v', use lowest from above)
                if check_if_match_horizontal() is not -1:
                    length = check_if_match_horizontal()
                    falling_board.delete_match('h', find a way to determine lowest based off of the swapped direction, length )
                    falling_board.shift_down('h', use lowest from above)
                else:
                    self.failed_swap()

    def vertical_swap(self):
        if mouse.get_rel(0, -10) or mouse.get_rel(0, 10):
            # gem at start mouse position switches to the Left or right
            if check_if_match_vertical() is not -1:
                length = check_if_match_vertical()
                falling_board.delete_match('v', find a way to determine lowest based off of the swapped direction, length)
                falling_board.shift_down('v', use lowest from above)
            if check_if_match_horizontal() is not -1:
                length = check_if_match_horizontal()
                falling_board.delete_match('h', find a way to determine lowest based off of the swapped direction, length)
                falling_board.shift_down('h', use lowest from above)
            else:
                self.failed_swap()

    def failed_swap(self):
        # basic rebound effect visually
        pass

    def update(self):
        # blip the swaps
        newpos = self.calcnewpos(self.rect, self.vector)
        self.rect = newpos
        (angle, z) = self.vector


class multiplier:
    '''
    Keep track of the current multiplier and keep it as an updating variable
    for use
    '''

    def __init__(self):
        self.score_multiplier = 1.0
        self.tmp = 0

    def increase_mult(self):
        self.score_multiplier += 0.1

    def decrease_mult(self):
        self.score_multiplier -= 0.1

    def big_mult(self, value):
        self.tmp = self.score_multiplier
        self.score_multiplier *= value

    def revert_mult(self):
        self.score_multiplier = self.tmp

    def reset_mult(self):
        self.score_multiplier = 1.0


class menu:
    '''
    Create an text object at the top of the screen, still in the window but
    seperate from the falling board, that counts the matches, with a given
    multiplier, housing the score and the timer
    '''
    # Do this after all logic is finished and I learn to blip

    def __init__(self):
        pass


class clock:
    '''
    Keeps track of current time and fps related things
    '''

    def __init__(self):
        self.clock = pygame.time.Clock


#  Game Functions
def scoreboard():
    # Could make this class
    '''
    Shows the current game score, time, multiplier, and game score in menu class area
    '''
    pass


def timer():
    # Could make this class
    '''
    Continous timer that shows remaining time left
    '''
    timer = pygame.time
    # define what endgame is
    timer.set_timer(endgame, 90000)


def menu_content():
    # idk
    '''
    Select try again, quit etc...
    '''
    pass


#  Initialize game here
def main():
    '''
    Initialize game, create objects for classes, check for user input, update..
    '''
# ---------------------------------------- Hello there thing
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Hedge Match Three')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello There", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()
# -----------------------------------------------

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

    #  Change this for mouse and movement of gems
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            '''
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    player.moveup()
                if event.key == K_DOWN:
                    player.movedown()
            elif event.type == KEYUP:
                if event.key == K_UP or event.key == K_DOWN:
                    player.movepos = [0,0]
                    player.state = "still"
            '''

    screen.blit(background, (0, 0))
    pygame.display.flip()


if __name__ == '__main__':
    main()
