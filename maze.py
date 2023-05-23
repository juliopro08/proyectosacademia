from pygame import *
import pygame
pygame.init()
mixer.init()
oro = list()
rulam = 'up'    

clock = time.Clock()
FPS = 60

ventana = display.set_mode((800,600))
ventana.unlock()
display.set_caption('Laberinto')
background = transform.scale(image.load('background.jpg'), (800,600))
ventana.blit(background,(0,0))
derrota = False

comecocos_bueno = transform.scale(image.load('hero.png'), (60, 60))
comecocos_malo = transform.scale(image.load('cyborg.png'), (60, 60))
tesoro = transform.scale(image.load('treasure.png'), (40, 40))
x_bueno = 0
y_bueno = 0
x_malo = 580
y_malo = 100
events = event.get()
rular = True
key_pressed = key.get_pressed()
bot = 1
mixer.music.load('jungles.ogg')
mixer.music.play()


dificultad = 5
dificultad_bot = 1



ventana = display.set_mode((800,600))
display.set_caption('Laberinto')
background = transform.scale(image.load('background.jpg'), (800,600))
ventana.blit(background,(0,0))


comecocos_bueno = transform.scale(image.load('hero.png'), (60, 60))
comecocos_malo = transform.scale(image.load('cyborg.png'), (60, 60))
tesoro = transform.scale(image.load('treasure.png'), (40, 40))
golpetazo = mixer.Sound('kick.ogg') 
x_bueno = 0
y_bueno = 0
x_malo = 580
y_malo = 100
events = event.get()
rular = True
key_pressed = key.get_pressed()
bot = 1
x_oro = 550
y_oro = 550
botvariable = 1
texto1 = True
texto2 = True
pygame.display.toggle_fullscreen()

font1_1 = pygame.font.SysFont('Arial', 50)
question = font1_1.render(
'Game over<<<<<<<<<press r to restart', texto1, (255, 0, 0)
)
font1_2 = pygame.font.SysFont('Arial', 50)
questionwin = font1_2.render(
'You won<<<<<<<press r to restart', texto2, (0, 255, 0)
)



dificultad = 5
dificultad_bot = 1

limxizq = -8
limxdcha = 748
limarriba = -1
limabjo = 547
limxizq1 = -20
limxdcha1 = 750
limarriba1 = -20
limabjo1 = 580
bots = list()
orovariable = 1
class laberinto():
    def __init__(self, name, fromx, fromy, tox, toy, color1, color2, color3):
        self.name = name
        self.fromx = fromx
        self.fromy = fromy
        self.tox = tox
        self.toy = toy
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
    def construccion(self):
        self.name = pygame.Rect(self.fromx, self.fromy, self.tox,self.toy)
        pygame.draw.rect(ventana, (self.color1, self.color2,self.color3), self.name)
    def muevete(self):
        global x_bueno
        global y_bueno
        global rular
        global x_oro
        global y_oro
        global orovariable
        global derrota
        global texto2
        global texto1
        self.fromx = x_bueno
        self.fromy = y_bueno
        for muro in pared:
            if self.name.colliderect(muro.name) and x_bueno> limxizq1 and x_bueno < limxdcha1 and y_bueno < limabjo1 and y_bueno> limarriba1:
                if rulam == 'left':
                    x_bueno -= 5
                elif rulam == 'right':
                    x_bueno += 5
                elif rulam == 'up':
                    y_bueno -= 5
                elif rulam == 'down':
                    y_bueno += 5
        for malo in bots:    
            if self.name.colliderect(malo.name):
                ventana.blit(question,(250, 250))
                derrota = True
                texto2 = True
                texto1 = True
        for oros in oro:
            if self.name.colliderect(oros.name):
                if orovariable == 1 and derrota != True:
                    x_oro = 0
                    y_oro = 0
                    orovariable = 2
                    golpetazo.play()
            if self.name.colliderect(oros.name) and x_oro == 0 and y_oro == 0 and x_bueno < 200:
                ventana.blit(questionwin, ( 250, 250))
                derrota = True
                texto1 = True
                texto2 = True
              


    def automuevete(self):
        self.fromx = x_malo
        self.fromy = y_malo
    def mueverecompensa(self):
        self.fromx = x_oro
        self.fromy = y_oro

perseguido = True
    
lab1 = laberinto('1',100,0, 20, 500,6, 12, 98)
lab2 = laberinto('2',200,100, 20, 500,6, 12, 98)
lab3 = laberinto('3',300,0, 20, 500,6, 12, 98)
lab4 = laberinto('4',400,100, 20, 500,6, 12, 98)
lab5 = laberinto('5',420,100, 50, 20,6, 12, 98)
lab6 = laberinto('6',300,0, 170, 20,6, 12, 98)
lab7 = laberinto('7',0,580, 200, 20,6, 12, 98)
lab8 = laberinto('8',100,0, 200, 20,6, 12, 98)
lab9 = laberinto('9',200,580, 200, 20,6, 12, 98)
bueno = laberinto('bueno', 0, 0 ,60, 60, 0, 0, 0)
malos = laberinto('malo', 580, 100,60, 60, 0, 0, 0 )
tesorin = laberinto('tesoro', x_oro, y_oro, 40, 40, 0, 0, 0)


variable = 'si'
while rular == True:
    for e in event.get():
        if e.type == QUIT:
            rular = False
    
    
    bueno.construccion()
    
    malos.construccion()
    malos.automuevete()
    tesorin.construccion()
    ventana.blit(background,(0,0))
    ventana.blit(comecocos_bueno,(x_bueno, y_bueno))
    ventana.blit(comecocos_malo,(x_malo, y_malo))
    ventana.blit(tesoro,(x_oro,y_oro))
    pared = list()
    lab1.construccion()
    lab2.construccion()
    lab3.construccion()
    lab4.construccion()
    lab5.construccion()
    lab6.construccion()
    lab7.construccion()
    lab8.construccion()
    lab9.construccion()
    paredno = 1
    
    if paredno == 1:
        pared.append(lab1)
        pared.append(lab2)
        pared.append(lab3)
        pared.append(lab4)
        pared.append(lab5)
        pared.append(lab6)
        pared.append(lab7)
        pared.append(lab8)
        pared.append(lab9)
        bots.append(malos)
        oro.append(tesorin)


        paredno = 2
    bueno.muevete()
    tesorin.mueverecompensa()

    
    events = event.get()


    #movimiento de tu personaje y dificulad
    key_pressed = key.get_pressed()
    if derrota == False:
        if key_pressed[K_UP] and y_bueno > limarriba:
            y_bueno -= dificultad
            rulam = 'down'

        if key_pressed[K_DOWN] and y_bueno < limabjo:
            y_bueno += dificultad
            rulam ='up'
        if key_pressed[K_LEFT] and x_bueno > limxizq:
            x_bueno -= dificultad
            rulam ='right'
        if key_pressed[K_RIGHT] and x_bueno < limxdcha:
            x_bueno += dificultad
            rulam = 'left'
    
    
    if key_pressed[K_q]:
        dificultad = 10
    if key_pressed[K_w]:
        dificultad = 20
    if key_pressed[K_a]:
        dificultad = 5
    if key_pressed[K_s]:
        dificultad = 1
    
    if key_pressed[K_1]:
        dificultad_bot = 1
    if key_pressed[K_2]:
        dificultad_bot = 2
    if key_pressed[K_3] or x_oro == 0:
        dificultad_bot = 5
    if key_pressed[K_4]:
        dificultad_bot = 10
    if key_pressed[K_ESCAPE]:
        rular = False
    if key_pressed[K_r]:
        derrota = False
        x_bueno = 0
        y_bueno = 0
        x_oro = 550
        y_oro = 550
        orovariable = 3
        botvariable = 1
        texto1 = False
        texto2 = False
        dificultad_bot = 1
        perseguido = True
    tesorin.mueverecompensa()
    

    #movimiento del bot      
    if x_oro == 550 and derrota == False:
        if botvariable == 1:
            x_malo = 580
            y_malo = 100
            botvariable = 2
        bot == 1
        if bot == 1:
            if x_malo > 510:
                x_malo -= dificultad_bot
            else:
                bot = 2
        if bot == 3:
            if x_malo < 590:
                x_malo += dificultad_bot
                if orovariable == 3:
                    orovariable = 1
            else:
                bot = 4
        if bot == 2:
            if y_malo < 200:
                y_malo += dificultad_bot
            else:
                bot = 3
        if bot == 4:
            if y_malo > 100:
                y_malo -= dificultad_bot
            else:
                bot = 1 
    elif x_oro == 0 and derrota == False:
        if perseguido == True:
            x_malo = 450
            y_malo = 450
            perseguido = False
        if rulam == 'right' and x_malo > limxizq:
            x_malo -= 3
        if rulam == 'left' and x_malo < limxdcha:
            x_malo += 3
        if rulam == 'up' and y_malo < limabjo:
            y_malo += 3
        if rulam == 'down' and y_malo > limarriba:
            y_malo -= 3

    if key_pressed[K_m]:
        if variable == 'si':
            mixer.music.pause()
            variable = 'no'
        else:
            mixer.music.unpause()
            variable = 'si'
        

     

    





    display.update()
    clock.tick(FPS)








