import glob
import os
import random
import sys
from math import hypot
from HeartRateAnalysis import computeBias, stimuliEnd, stimuliStart, initSensors

import pygame
from pygame.locals import *
# from pygame import display,movie

# Image data path
IMG_DIR = os.path.join(os.path.abspath(__file__), "img")

# Color Consts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen size
SCREEN_HEIGHT = 750
SCREEN_WIDTH = 1333

# Setup pygame window
pygame.init()
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Current screen index
CURRENT_GAME_STATE = "00.png" # OG start screen
NUM_GAME_SATES = 7

captain_1 = False
captain_2 = False
captain_3 = False
captain_4 = False
firstLieut_1 = False
firstLieut_2 = False
firstLieut_3 = False
firstLieut_4 = False
secondLieut_1 = False
secondLieut_2 = False
secondLieut_3 = False
secondLieut_4 = False
doctor_1 = False
doctor_2 = False
doctor_3 = False
doctor_4 = False
engineer_1 = False
engineer_2 = False
engineer_3 = False
engineer_4 = False
placeholderfor6_1 = False
placeholderfor6_2 = False
placeholderfor6_3 = False
placeholderfor6_4 = False
placeholderfor7_1 = False
placeholderfor7_2 = False
placeholderfor7_3 = False
placeholderfor7_4 = False

selected_heads = []

PATH = os.getcwd()

def side_bar():
    pygame.font.init()  # you have to call this at the start,
    clock = pygame.time.Clock()
    counter, text = 60, '60'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)

    # if you want to use this module.
    while True:
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONUP:
                break
            if e.type == pygame.USEREVENT:
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else 'boom!'
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        else:
            DISPLAYSURF.blit(font.render(text, True, (102, 255, 51)), (238, 392))
            pygame.display.flip()
            clock.tick(60)
            continue

def distance(first,second):
    (x1,y1)=first
    (x2,y2)=second
    return hypot(x2-x1, y2-y1)

# def _load_next_img():
#     """ Load a random image from the image set at pos (0,0)
#     """
#     # Select a random image from the png files in the data folder
#     global CURRENT_GAME_STATE
#     CURRENT_GAME_STATE += 1
#     if CURRENT_GAME_STATE > NUM_GAME_SATES:
#         sys.exit(0)
#     img = pygame.image.load(os.path.join(PATH,'imgs',str(CURRENT_GAME_STATE)+".png"))
#     DISPLAYSURF.blit(pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))


StartRect = Rect(457,589,400,200)
OPTION1 = Rect(422,331,100,70)
OPTION2 = Rect(659,331,100,70)
OPTION3 = Rect(886,331,100,70)
OPTION4 = Rect(1122,331,100,70)

MAIN_LOOP = 0;
VID_1 = 0;
VID_2 = 0;
INTRO = 0;

def main_loop_next():
    global MAIN_LOOP
    imgnum = "%03d" % (MAIN_LOOP)
    img = pygame.image.load(os.path.join(PATH, 'imgs', 'main loop', "ST_01" + str(imgnum) + ".jpg"))
    DISPLAYSURF.blit(pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
    pygame.display.flip()
    MAIN_LOOP += 10

def intro_next():
    global INTRO
    imgnum = "%04d" % (INTRO)
    img = pygame.image.load(os.path.join(PATH, 'imgs', 'Game_Video', "Game Video_01_1" + str(imgnum) + ".jpg"))
    DISPLAYSURF.blit(pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
    pygame.display.flip()
    INTRO += 7

def interior_next_1():
    global VID_1
    imgnum = "%04d" % (VID_1)
    img = pygame.image.load(os.path.join(PATH, 'imgs', 'Interior Vid 1', "Interior Video_01" + str(imgnum) + ".jpg"))
    DISPLAYSURF.blit(pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
    pygame.display.flip()
    VID_1 += 7

def interior_next_2():
    global VID_2
    imgnum = "%03d" % (VID_2)
    img = pygame.image.load(os.path.join(PATH, 'imgs', 'Interior Vid 2', "Interior Video_02" + str(imgnum) + ".jpg"))
    DISPLAYSURF.blit(pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
    pygame.display.flip()
    VID_2 += 7

def update_screen_and_state(new_state):

    if (new_state == "v1.png"):
        stimuliStart("Screen1")
        global MAIN_LOOP
        clicked = False
        while (MAIN_LOOP < 590):
            if clicked:
                break
            for e in pygame.event.get():
                if e.type == pygame.MOUSEBUTTONUP:
                    clicked = True
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            main_loop_next()
        update_screen_and_state("01.png") ##
        stimuliEnd()
    elif (new_state == "v2.png"):
        stimuliStart("Screen2")
        global INTRO
        clicked = False
        while (INTRO < 5390):
            if clicked:
                break
            for e in pygame.event.get():
                if e.type == pygame.MOUSEBUTTONUP:
                    clicked = True
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            intro_next()
        update_screen_and_state("01.png")
        stimuliEnd()
    elif (new_state == "v3.png"):
        stimuliStart("Screen3")
        global VID_1
        clicked = False
        while (VID_1 < 900):
            if clicked:
                break
            for e in pygame.event.get():
                if e.type == pygame.MOUSEBUTTONUP:
                    clicked = True
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            interior_next_1()
        update_screen_and_state("02.png")
        stimuliEnd()
    elif (new_state == "v4.png"):
        stimuliStart("Screen4")
        global VID_2
        clicked = False
        while (VID_2 < 530):
            if clicked:
                break
            for e in pygame.event.get():
                if e.type == pygame.MOUSEBUTTONUP:
                    clicked = True
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            interior_next_2()
        update_screen_and_state("06.png")
        stimuliEnd()
    else:
        global CURRENT_GAME_STATE
        img = pygame.image.load(os.path.join(PATH,'imgs',new_state))
        DISPLAYSURF.blit(pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
        CURRENT_GAME_STATE = new_state
        pygame.display.update()


        pygame.font.init()  # you have to call this at the start,
        clock = pygame.time.Clock()
        counter, text = 60, '60'.rjust(3)
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        font = pygame.font.SysFont('Consolas', 60)
        clicked = False



        # if you want to use this module.
        while True:
            if counter == 0:
                break
            if clicked:
                break
            for e in pygame.event.get():
                if e.type == pygame.MOUSEBUTTONUP:
                    clicked = True
                if e.type == pygame.USEREVENT:
                    counter -= 1
                    text = str(counter).rjust(3) if counter > 0 else 'boom!'
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                break
            else:
                DISPLAYSURF.blit(pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
                xOff = 0
                yOff = 0
                count = 0
                for head in selected_heads:
                    img_head = pygame.image.load(os.path.join(PATH,'heads',head))
                    DISPLAYSURF.blit(pygame.transform.scale(img_head,(50,50)),(30+xOff,430+yOff))
                    if count < 3:
                        xOff += 60
                        count += 1
                    else:
                        count = 0
                        xOff = 0
                        yOff += 60

                DISPLAYSURF.blit(font.render(text, True, (102, 255, 51)), (100, 250))
                pygame.display.flip()
                clock.tick(60)
                continue


def _handle_click(click_pos):
    global CURRENT_GAME_STATE

    """ Handle a click event
    """
    # START SCREEN: HIT PLAY!
    if CURRENT_GAME_STATE == "00.png":
        if StartRect.collidepoint(click_pos):
            update_screen_and_state("v2.png")
    # CAPTAIN SCREEN
    elif CURRENT_GAME_STATE == "01.png":
        print ("in here\n")
        if OPTION1.collidepoint(click_pos):
            captain_1 = True
            selected_heads.append("01_h1.png")
        elif OPTION2.collidepoint(click_pos):
            captain_2 = True
            selected_heads.append("01_h2.png")

        elif OPTION3.collidepoint(click_pos):
            captain_3 = True
            selected_heads.append("01_h3.png")

        else:
            captain_4 = True
            selected_heads.append("01_h4.png")

        update_screen_and_state("v3.png")
    elif CURRENT_GAME_STATE == "02.png":
        if OPTION1.collidepoint(click_pos):
            firstLieut_1 = True
            selected_heads.append("02_h1.png")

        elif OPTION2.collidepoint(click_pos):
            firstLieut_2 = True
            selected_heads.append("02_h2.png")

        elif OPTION3.collidepoint(click_pos):
            firstLieut_3 = True
            selected_heads.append("02_h3.png")

        else:
            firstLieut_4 = True
            selected_heads.append("01_h4.png")

        update_screen_and_state("03.png")
    elif CURRENT_GAME_STATE == "03.png":
        if OPTION1.collidepoint(click_pos):
            secondLieut_1 = True
            selected_heads.append("03_h1.png")
        elif OPTION2.collidepoint(click_pos):
            secondLieut_2 = True
            selected_heads.append("03_h2.png")

        elif OPTION3.collidepoint(click_pos):
            secondLieut_3 = True
            selected_heads.append("03_h3.png")
        else:
            secondLieut_4 = True
            selected_heads.append("03_h4.png")
        update_screen_and_state("04.png")
    elif CURRENT_GAME_STATE == "04.png":
        if OPTION1.collidepoint(click_pos):
            doctor_1 = True
            selected_heads.append("04_h1.png")
        elif OPTION2.collidepoint(click_pos):
            doctor_2 = True
            selected_heads.append("04_h2.png")
        elif OPTION3.collidepoint(click_pos):
            doctor_3 = True
            selected_heads.append("04_h3.png")
        else:
            doctor_4 = True
            selected_heads.append("04_h4.png")
        update_screen_and_state("05.png")
    elif CURRENT_GAME_STATE == "05.png":
        if OPTION1.collidepoint(click_pos):
            engineer_1 = True
            selected_heads.append("05_h1.png")
        elif OPTION2.collidepoint(click_pos):
            engineer_2 = True
            selected_heads.append("05_h2.png")
        elif OPTION3.collidepoint(click_pos):
            engineer_3 = True
            selected_heads.append("05_h3.png")
        else:
            engineer_4 = True
            selected_heads.append("05_h4.png")
        update_screen_and_state("v4.png") # PLACE HOLDER! (CHANGE TO 06.PNG)
    elif CURRENT_GAME_STATE == "06.png": # PLACE HOLDER CHANGE TO 06
        if OPTION1.collidepoint(click_pos):
            placeholderfor6_1 = True
            selected_heads.append("06_h1.png")
        elif OPTION2.collidepoint(click_pos):
            placeholderfor6_2 = True
            selected_heads.append("06_h2.png")
        elif OPTION3.collidepoint(click_pos):
            placeholderfor6_3 = True
            selected_heads.append("06_h3.png")
        else:
            placeholderfor6_4 = True
            selected_heads.append("06_h4.png")
        update_screen_and_state("07.png") # PLACE HOLDER! CHANGE TO 07
    elif CURRENT_GAME_STATE == "07.png": # PLACE HOLDER CHANGE TO 07
        if OPTION1.collidepoint(click_pos):
            placeholderfor7_1 = True
            selected_heads.append("07_h1.png")
        elif OPTION2.collidepoint(click_pos):
            placeholderfor7_2 = True
            selected_heads.append("07_h2.png")
        elif OPTION3.collidepoint(click_pos):
            placeholderfor7_3 = True
            selected_heads.append("07_h3.png")
        else:
            placeholderfor7_4 = True
            selected_heads.append("07_h4.png")
        update_screen_and_state("v1.png") # PLACE HOLDER! CHANGE TO END?


    # _load_next_img()
    # # Check if there was a collision with the next buttonn
    
    
    #     _load_next_img()




def main():
    # Set caption
    initSensors()
    print("Hello")
    pygame.display.set_caption('Game Demo!')

    img = pygame.image.load(os.path.join(PATH,'imgs',"00.png"))
    DISPLAYSURF.blit(pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))


    # img = pygame.image.load(os.path.join(PATH,'imgs',str(CURRENT_GAME_STATE)+".png"))
    # DISPLAYSURF.blit(pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
    # global CURRENT_GAME_STATE
    CURRENT_GAME_STATE = "00.png"

    # Main event loop
    while True:
        # Check for new events
        for event in pygame.event.get():

            # Recv quit event
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # Recv click event
            if event.type == pygame.MOUSEBUTTONUP:
                # print ("kfajs;ldfja\n")
                # _load_next_img
                click_pos = pygame.mouse.get_pos()
                # print (str(click_pos) + "\n")
                _handle_click(click_pos)

        # Update the display based on current state after reading events
        pygame.display.update()


if __name__ == "__main__":
    main()
