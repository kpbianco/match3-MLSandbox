#!/usr/bin/env python
#
# Kian's ML Match 3 Playground
# A simple match three game that enables a reinforcement learning model for practice
# github link
#
# Released under the GNU General Public License

VERSION = "0.0"

try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    from socket import*
    from pygame.locals import *

except ImportError as err:
    print(f"couldn't load module {0}".format(err))
    sys.exit(2)


#  Resources


class images:

    def load_png(name):
        fullname = os.path.join('./static', name)
        try:
            image = pygame.image.load(fullname)

            if image.get_alpha() is None:
                image = image.convert()

            else:
                image = image.convert_alpha()

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


class cursor:
    '''
    game cursor for interaction
    '''

    def __init__(self):
        pass


class falling_board:
    '''
    Create new stack array of 3x3 size full of gems where
    the gems automatically fall from the top to fill spaces
    and check if there are adjacents that are 3+ for a match
    and delete them as needs
    '''

    def __init__(self):
        pass


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

    def update(self):
        newpos = self.calcnewpos(self.rect, self.vector)
        self.rect = newpos
        (angle, z) = self.vector

        # Collisions to change for my implementation
        '''
        if not self.area.contains(newpos):
            tl = not self.area.collidepoint(newpos.topleft)
            tr = not self.area.collidepoint(newpos.topright)
            bl = not self.area.collidepoint(newpos.bottomleft)
            br = not self.area.collidepoint(newpos.bottomright)
            if tr and tl or (br and bl):
                angle = -angle
            if tl and bl:
                # self.offcourt()
                angle = math.pi - angle
            if tr and br:
                angle = math.pi - angle
                # self.offcourt()
        else:
            # Deflate the rectangles so you can't catch a ball behind the bat
            player1.rect.inflate(-3, -3)
            player2.rect.inflate(-3, -3)

            # Do ball and bat collide?
            # Note I put in an odd rule that sets self.hit to 1 when they collide, and unsets it in the next
            # iteration. this is to stop odd ball behaviour where it finds a collision *inside* the
            # bat, the ball reverses, and is still inside the bat, so bounces around inside.
            # This way, the ball can always escape and bounce away cleanly
            if self.rect.colliderect(player1.rect) == 1 and not self.hit:
                angle = math.pi - angle
                self.hit = not self.hit
            elif self.rect.colliderect(player2.rect) == 1 and not self.hit:
                angle = math.pi - angle
                self.hit = not self.hit
            elif self.hit:
                self.hit = not self.hit
        self.vector = (angle,z)
        '''

    #  Use my own method for moving this is for hitting
    def calcnewpos(self, rect, vector):
        (angle, z) = vector
        (dx, dy) = (z * math.con(angle), z * math.sin(angle))
        return rect.move(dx, dy)


#  Double check if this needs to be a class or a function or just a component
class multiplier:
    '''
    Keep track of the current multiplier and keep it as an updating variable
    for use
    '''

    def __init__(self):
        pass


class menu:
    '''
    Create an text object at the top of the screen, still in the window but
    seperate from the falling board, that counts the matches, with a given
    multiplier, housing the score and the timer
    '''

    def __init__(self):
        pass


#  Game Functions


def scoreboard():
    '''
    Shows the current game score, multiplier, and game score in menu class area
    '''
    pass


def timer():
    '''
    Continous timer that shows remaining time left
    '''
    pass


def menu_content():
    '''
    Select try again, quit etc...
    '''
    pass


#  Initialize game here


def main():
    '''
    Initialize game, create objects for classes, check for user input, update..
    '''

    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Basic Pygame program')

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
