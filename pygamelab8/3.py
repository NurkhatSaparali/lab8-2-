#  python C:\Users\Nurhat\OneDrive\Desktop\pygamelab8\3.py
import pygame
pygame.init()

#параметры окна
width=800
height=600
screen=pygame.display.set_mode((width,height))
screen.fill((255,255,255))  #заливка фона белым
#настройки рисования
thickness=5
lmbpressed=False
last_pos=None
start_pos=None
mode="line" #по умолчанию линия

#цвета
color_red=(255,0,0)
color_blue=(0,0,255)
color_black=(0,0,0)
color_white=(255,255,255)
color_green=(0,255,0)
color_yellow=(255,255,0)
color_purple=(128,0,128)
color_orange=(255,165,0)

current_color=color_black #черный цвет по умолчанию

#Управление 
print("""
Управление:
0 - белый
1 - красный
2 - синий
3 - черный
4 - зеленый
5 - желтый
6 - фиолетовый
7 - оранжевый

L - линия
R - прямоугольник
C - круг
E - ластик
""")

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        #смена цвета и режима
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                mode="rectangle"
            elif event.key==pygame.K_c:
                mode="circle"
            elif event.key==pygame.K_l:
                mode="line"
            elif event.key==pygame.K_e:
                mode="eraser"
            elif event.key==pygame.K_0:
                current_color=color_white; mode="line"
            elif event.key==pygame.K_1:
                current_color=color_red; mode="line"
            elif event.key==pygame.K_2:
                current_color=color_blue; mode="line"
            elif event.key==pygame.K_3:
                current_color=color_black; mode="line"
            elif event.key==pygame.K_4:
                current_color=color_green; mode="line"
            elif event.key==pygame.K_5:
                current_color=color_yellow; mode="line"
            elif event.key==pygame.K_6:
                current_color=color_purple; mode="line"
            elif event.key==pygame.K_7:
                current_color=color_orange; mode="line"

        #начало рисования    
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                lmbpressed=True
                start_pos=event.pos
                last_pos=event.pos
        #процесс рисования
        if event.type==pygame.MOUSEMOTION:
            if lmbpressed:
                if mode=="line":
                    pygame.draw.line(screen,current_color,last_pos,event.pos,thickness)
                elif mode=="eraser":
                    pygame.draw.line(screen,color_white,last_pos,event.pos,thickness*3)  
                last_pos=event.pos
        #завершения рисование фигур
        if event.type==pygame.MOUSEBUTTONUP:
            if event.button==1:
                lmbpressed=False
                if mode=="rectangle":
                    x1,y1=start_pos
                    x2,y2=event.pos
                    rect=pygame.Rect(min(x1,x2),min(y1,y2),abs(x2-x1),abs(y2-y1))
                    pygame.draw.rect(screen,current_color,rect,thickness)
                elif mode=="circle":
                    x1,y1=start_pos
                    x2,y2=event.pos
                    radius=int(((x2-x1)**2+(y2-y1)**2)**0.5)
                    pygame.draw.circle(screen,current_color,start_pos,radius,thickness)
    pygame.display.flip()
pygame.quit()
