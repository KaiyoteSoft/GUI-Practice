import sgc
from sgc.locals import *

import pygame, sys
from pygame.locals import *

pygame.display.init()
pygame.font.init()
pygame.init()



class MyButton(sgc.Button):
    def on_click(self):
        self.level = 2
        print(self.level)

        
class QuitButton(sgc.Button):
    def on_click(self):
        pygame.quit()
        sys.exit()
    
class MapBox(sgc.Combo):
    def on_select(self):
        print(event)
        
        
        
clock = pygame.time.Clock()


windowSurface = sgc.surface.Screen((480, 320))
bloody = pygame.font.Font("fonts/BLOODY.ttf", 32)



btn = MyButton(label = "Next",
               pos = (350, 250))
btn.level = 1

btn2 = QuitButton(label = "Quit", pos = (20, 250),
                  col = (255, 0, 0), label_font = bloody,
                  label_col = (0, 255, 0))

#### combo box
combo = MapBox(pos = (250, 100), values = ("Forest", "Ocean", "Castle"),
               selection = 0)

#### radio button
radio_1 = sgc.Radio(label = "Pistol",
                    group = "weapon", active = True,
                    label_side = "right")

radio_2 = sgc.Radio(label = "Shotgun",
                    group = "weapon")

radio_3 = sgc.Radio(label = "Sniper",
                    group = "weapon")


radio_box = sgc.VBox(widgets = (radio_1, radio_2, radio_3), pos = (50, 50))

### switch
switch = sgc.Switch(label = "Limit Bullets", pos = (300, 200),
                   label_side = "top")

## slider
slider = sgc.Scale(label = "Number of Monsters", pos = (10, 200),
                   label_side = "top", label_col = (255, 255, 0))

label = sgc.Label(text = "This is a zombie shooter game \n" +
                  "in which you journey through eight \n" +
                  "levels to save a girl from \n" +
                  "monsters. Good Luck!", pos = (10, 10), font = bloody,
                  col = (255, 0, 0))

btn.add(0)
btn2.add(1)
combo.add(2)
radio_box.add(3)
switch.add(4)
slider.add(5)


while True:
    time = clock.tick(30)
    for event in pygame.event.get():
        sgc.event(event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    if btn.level == 2:
        btn.remove(fade = False)
        combo.remove(fade = False)
        radio_box.remove(fade = False)
        switch.remove(fade = False)
        slider.remove(fade = False)
        label.add(6)
    
    windowSurface.fill((0, 0, 0))        
    sgc.update(time)
    pygame.display.update()