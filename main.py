import pygame, sys
from button import Button
import random
import numpy as np
from pygame.locals import *


global newr
global str_sum
global i_sum
global j_sum
global rp

global sz
global i_p
global i_r
global again
global m_r

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Pick The Rock")
transparent = (0, 0, 0, 0)

BG = pygame.image.load("assets/bg.jpg")
img = pygame.image.load("assets/rock.png")
img = pygame.transform.scale(img, (100, 50))
img.convert()
imar=np.empty((7,7), dtype=object)

def rocks(string,arr_x):
    

    for i in range(int(len(string))):
        r2=int(string[i])
        for j in range(r2):
           rec = img.get_rect()
           pl=620-(50*j)
           rec.center = arr_x[i], pl
           SCREEN.blit(img, rec)
    pygame.display.update()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font2.ttf", size)

def cal_sum(ss):
    pp=0
    for i in range(int(len(ss))):
        pp+=int(ss[i])
    return pp

def decision(strr,arr1,arr2,arr_x,player):
    moving=-1
    tt=0
    tt1=0
    while(True):
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        
        SCREEN.blit(BG, (0, 0))
        
        if(cal_sum(strr)==0):
            SCREEN.blit(BG, (0, 0))
            PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 50), 
                         text_input="Main Menu", font=get_font(45), base_color="#d7fcd4", hovering_color="#660000")
            QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(900, 50), 
                             text_input="QUIT", font=get_font(45), base_color="#d7fcd4", hovering_color="#660000")
     
             
            for button in [PLAY_BUTTON, QUIT_BUTTON]:
                button.changeColor(PLAY_MOUSE_POS)
                button.update(SCREEN)
            if(player==0 and tt==0):    
                PLAY_MOUSE_POS = pygame.mouse.get_pos()
                PLAY_TEXT = get_font(45).render("Computer Wins", True, "#660000")
                PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 160))
                SCREEN.blit(PLAY_TEXT, PLAY_RECT)
                print("Computer wins")
            elif(player==1 and tt1==0):
                PLAY_MOUSE_POS = pygame.mouse.get_pos()
                PLAY_TEXT = get_font(45).render("Human Wins", True, "#660000")
                PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 160))
                SCREEN.blit(PLAY_TEXT, PLAY_RECT)
                print("Human wins")
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if PLAY_BUTTON.checkForInput(PLAY_MOUSE_POS):
                            main_menu()
                        if QUIT_BUTTON.checkForInput(PLAY_MOUSE_POS):
                            pygame.quit()
                            sys.exit()
            pygame.display.update()
        
        if(player==0):
            par=1
            for i in range(int(len(strr))):
                rr=int(strr[i])
                if(rr==0):
                    continue
                for j in range(1,rr+1):
                    if(arr2[i][j]==0):
                        par=0
                        break
                if(par==0):
                    break
            if(par==1):
               PLAY_MOUSE_POS = pygame.mouse.get_pos()
               SCREEN.blit(BG, (0, 0))
               PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 50), 
                            text_input="Main Menu", font=get_font(45), base_color="#d7fcd4", hovering_color="#660000")
               QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(900, 50), 
                                text_input="QUIT", font=get_font(45), base_color="#d7fcd4", hovering_color="#660000")
        
                
               for button in [PLAY_BUTTON, QUIT_BUTTON]:
                   button.changeColor(PLAY_MOUSE_POS)
                   button.update(SCREEN)
               PLAY_TEXT = get_font(45).render("Human has no option, Computer Wins", True, "#660000")
               PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 160))
               SCREEN.blit(PLAY_TEXT, PLAY_RECT)
               tt=1
               print("Computer wins") 
               rocks(strr,arr_x)
               
               for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if PLAY_BUTTON.checkForInput(PLAY_MOUSE_POS):
                            main_menu()
                        
                        if QUIT_BUTTON.checkForInput(PLAY_MOUSE_POS):
                            pygame.quit()
                            sys.exit()
               pygame.display.update()

            else:
                #player=1-player
                p2=0
                
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #PLAY_MOUSE_POS = pygame.mouse.get_pos()
                        print(PLAY_MOUSE_POS)
                        print('j1')
                        for i in range(int(len(strr))):
                            r1=int(strr[i])
                            for j in range(r1):
                                rect = img.get_rect()
                                rect.center = arr_x[i],620-(50*j)
                                if rect.collidepoint(event.pos):
                                    print('j2')
                                    moving = j
                                    i_p=i
                                    i_r=r1
                                    m_r=rect
                                    again=r1-moving
                                    break
                            if(moving>0):
                                break
                    #rocks(strr,arr_x) 
                                 
                    if event.type == pygame.MOUSEBUTTONUP: 
                        print('j3')
                        print(moving)
                        if(moving>=0): 
                            print('j4')
                            print(i_p)
                            print(again)
                            if(arr2[i_p][again]==1):
                                
                                SCREEN.blit(BG, (0, 0))
                                PLAY_MOUSE_POS = pygame.mouse.get_pos()
                                PLAY_TEXT = get_font(45).render("It's already picked", True, "#660000")
                                PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 160))
                                SCREEN.blit(PLAY_TEXT, PLAY_RECT)
                                print("It's already picked") 
                                pygame.display.update()
                                rocks(strr,arr_x)
                                moving=-1
                            else:
                                print('jj')
                                arr2[i_p][again]=1
                                list1 = list(strr)
                                list1[i_p] = str(moving)
                                strr = ''.join(list1)
                                rocks(strr,arr_x)
                                moving=-1
                                player=1-player
                                break
                    
                    #rocks(strr,arr_x) 
                #rocks(strr,arr_x)               

            
            
            
        else:
            p=0
            sum=0
            pl=0
            for i in range(int(len(strr))): 
                rr=int(strr[i])
                if(rr==0):
                    continue
                for j in range(1,rr+1):
                    if(arr1[i][j]==0):
                        p=1
                        trs=strr
                        pp=str(rr-j)
                        list1 = list(trs)
                        list1[i] = pp
                        trs = ''.join(list1)
                        sum^=(j+1)
                        if(sum==0):
                            print("*******")
                            pl=1
                            arr1[i][j]=1
                            pygame.time.delay(300)
                            rocks(trs,arr_x)
                            print('robot = '+trs)
                            strr=trs
                            player=1-player
                            break
                        else:
                           str_sum=trs
                           i_sum=i
                           j_sum=j 
                if(pl==1):
                    break
            
            if(p==0):
                SCREEN.blit(BG, (0, 0))
                PLAY_MOUSE_POS = pygame.mouse.get_pos()
                PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 50), 
                            text_input="Main Menu", font=get_font(45), base_color="#d7fcd4", hovering_color="#660000")
                QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(900, 50), 
                                 text_input="QUIT", font=get_font(45), base_color="#d7fcd4", hovering_color="#660000")
        
                
                for button in [PLAY_BUTTON, QUIT_BUTTON]:
                    button.changeColor(PLAY_MOUSE_POS)
                    button.update(SCREEN)
                PLAY_TEXT = get_font(45).render("Computer cannot make any move, Human Wins", True, "#660000")
                PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 160))
                SCREEN.blit(PLAY_TEXT, PLAY_RECT)
                tt1=1
                print("Human wins")
                rocks(strr,arr_x)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if PLAY_BUTTON.checkForInput(PLAY_MOUSE_POS):
                            main_menu()
                        
                        if QUIT_BUTTON.checkForInput(PLAY_MOUSE_POS):
                            pygame.quit()
                            sys.exit()

                pygame.display.update()
                 
            elif(pl==0):
                arr1[i_sum][j_sum]=1
                rrr=int(strr[i_sum])
                
                strr=str_sum
                pygame.time.delay(300)
                rocks(strr,arr_x)
                print('robot 2 = '+str_sum)
                player=1-player
        
                
        
        

def piles(turn):
    while True: 
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_TEXT = get_font(45).render("Choose pile number", True, "#660000")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 160))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        
       
        PLAY_2 = Button(image=pygame.image.load("assets/Num Rect.png"), pos=(360, 350), 
                            text_input="2", font=get_font(65), base_color="White", hovering_color="Green")

        PLAY_3 = Button(image=pygame.image.load("assets/Num Rect.png"), pos=(510, 350), 
                            text_input="3", font=get_font(55), base_color="White", hovering_color="Green")
        PLAY_4 = Button(image=pygame.image.load("assets/Num Rect.png"), pos=(660, 350), 
                            text_input="4", font=get_font(65), base_color="White", hovering_color="Green")
        
        PLAY_5 = Button(image=pygame.image.load("assets/Num Rect.png"), pos=(810, 350), 
                            text_input="5", font=get_font(65), base_color="White", hovering_color="Green")

        PLAY_6 = Button(image=pygame.image.load("assets/Num Rect.png"), pos=(960, 350), 
                            text_input="6", font=get_font(55), base_color="White", hovering_color="Green")

        PLAY_BACK = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(610, 550), 
                            text_input="BACK", font=get_font(55), base_color="White", hovering_color="Green")
        
        PLAY_2.changeColor(PLAY_MOUSE_POS)
        PLAY_3.changeColor(PLAY_MOUSE_POS)
        PLAY_4.changeColor(PLAY_MOUSE_POS)
        PLAY_5.changeColor(PLAY_MOUSE_POS)
        PLAY_6.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_2.update(SCREEN)
        PLAY_3.update(SCREEN)
        PLAY_4.update(SCREEN)
        PLAY_5.update(SCREEN)
        PLAY_6.update(SCREEN)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    play()
                if PLAY_2.checkForInput(PLAY_MOUSE_POS):
                    sz=2
                if PLAY_3.checkForInput(PLAY_MOUSE_POS):
                    sz=3
                if PLAY_4.checkForInput(PLAY_MOUSE_POS):
                    sz=4
                if PLAY_5.checkForInput(PLAY_MOUSE_POS):
                    sz=5
                if PLAY_6.checkForInput(PLAY_MOUSE_POS):
                    sz=6
                place(sz,turn)
        pygame.display.update()       

        



dic = {}
summ = {}

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        
        SCREEN.blit(BG, (0, 0))
        PLAY_TEXT = get_font(45).render("Choose turn", True, "#660000")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 160))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        
        PLAY_C = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 300), 
                            text_input="Computer", font=get_font(65), base_color="White", hovering_color="Green")
        
        PLAY_H = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(900, 300), 
                            text_input="Human", font=get_font(65), base_color="White", hovering_color="Green")

        PLAY_BACK = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 550), 
                            text_input="BACK", font=get_font(55), base_color="White", hovering_color="Green")

        PLAY_C.changeColor(PLAY_MOUSE_POS)
        PLAY_H.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_C.update(SCREEN)
        PLAY_H.update(SCREEN)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if PLAY_C.checkForInput(PLAY_MOUSE_POS):
                    piles(1)
                if PLAY_H.checkForInput(PLAY_MOUSE_POS):
                    piles(0)

        pygame.display.update()
        
def place(n,turn):
    SCREEN.blit(BG, (0, 0))
        
    arr_x=np.zeros(7)
    arr1=np.zeros((7,7),np.uint8)
    arr2=np.zeros((7,7),np.uint8)
    c=1280/(n+1)
    d=c
    for i in range(n+1):
        arr_x[i]=c
        c+=d
    string=""
    for i in range(n):
        r=int(random.randint(1,6))
        string+=str(r)
    print(string)    
    while(1):
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0, 0))        
        rocks(string,arr_x)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                decision(string,arr1,arr2,arr_x,turn)
                     
    pygame.display.update()    
        
        
    

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Pick The Rock", True, "#660000")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 200))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 400), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="#660000")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(900, 400), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="#660000")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()